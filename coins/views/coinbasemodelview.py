import os
import json
import requests as r
import re
from django.views.decorators.csrf import csrf_exempt
from coins.serializers.coinbasemodelserializer import (
    CoinBaseModelSerializer,
    CoinSkusOnlySerializer,
)
from coins.models.coinbasemodel import CoinBaseModel

from rest_framework.response import Response
from rest_framework import mixins, generics
from rest_framework import status
from django.http import JsonResponse
from coins.models.grading import CoinGrades, GradingServices
from coins.models.strike import Strike
from coins.models.mints import SelectOneMint
from coins.models.denominations import CoinFamily, Denominations, CoinTypeName


class CoinBaseModelSerializerView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = CoinBaseModel.objects.all()
    serializer_class = CoinBaseModelSerializer

    def get(self, request, *args, **kwargs):
        is_deleted_param = request.query_params.get("is_deleted", None)

        if is_deleted_param is not None:
            if is_deleted_param.lower() == "true":
                self.queryset = self.queryset.filter(is_deleted=True)
            elif is_deleted_param.lower() == "false":
                self.queryset = self.queryset.filter(is_deleted=False)

        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class OneCoinBaseModelSerializerView(
    mixins.UpdateModelMixin,
    generics.GenericAPIView,
):
    queryset = CoinBaseModel.objects.all()
    serializer_class = CoinBaseModelSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        coin_instance = self.get_object()
        serializer = self.get_serializer(coin_instance)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        coin_instance = self.get_object()
        if "toggle_soft_delete" in request.data:
            coin_instance.soft_delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # remove sku from data because it was invalidating serializer
        # got to be a better way than this though
        del request.data["sku"]

        serializer = self.get_serializer(
            coin_instance,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():
            print("Serializer is valid")
            serializer.save()
            return Response(serializer.data)
        else:
            print("Serializer errors:", serializer.errors)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CoinTypeSerializerView(
    mixins.ListModelMixin,
    generics.GenericAPIView,
):
    queryset = CoinBaseModel.objects.all()
    serializer_class = CoinBaseModelSerializer
    lookup_field = "coin_type"

    def get(self, request, *args, **kwargs):
        coin_types = kwargs.get("coin_type")
        if coin_types is not None:
            queryset = self.queryset.filter(
                coin_type=coin_types,
                is_deleted=False,
            )
        else:
            queryset = self.queryset.all()

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class GetAllSkusView(
    mixins.ListModelMixin,
    generics.GenericAPIView,
):
    queryset = CoinBaseModel.objects.all()
    serializer_class = CoinSkusOnlySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


@csrf_exempt
def pcgs_coin_data(request, *args, **kwargs):
    pcgs_api_key = os.environ.get("PCGS_API_KEY")
    grading_service = ""
    coin_data = ""
    headers = {"authorization": f"bearer {pcgs_api_key}"}
    result = {}
    if isinstance(request, dict):
        pcgs_no = request.get("pcgs_no")
    else:
        pcgs_no = json.loads(request.body).get("pcgs_no")
    if pcgs_no is None:
        return None
    # For PCGS number entered manually:
    if len(pcgs_no) <= 8:
        url = (
            f"https://api.pcgs.com/publicapi/coindetail/GetCoinFactsByCertNo/{pcgs_no}"
        )
        coin_data = r.get(url, headers=headers).json()
        grading_service = "PCGS"
    if len(pcgs_no) > 8 and len(pcgs_no) < 17:
        grading_service = "PCGS"
        scan_url = f"https://api.pcgs.com/publicapi/coindetail/GetCoinFactsByBarcode?barcode={pcgs_no}&gradingService={grading_service}"
        coin_data = r.get(scan_url, headers=headers).json()
    if len(pcgs_no) > 16:
        grading_service = "NGC"
        scan_url = f"https://api.pcgs.com/publicapi/coindetail/GetCoinFactsByBarcode?barcode={pcgs_no}&gradingService={grading_service}"
        coin_data = r.get(scan_url, headers=headers).json()

    """
    Import info from response:
    PCGSNo - str
    CertNo - certification number str
    Name - year-mm denon - str
    Year - int
    Denomination - str
    MintMark - str
    MintLocation - str
    Grade - str - need to get the numeric grade and if +
    PriceGuideValue - float
    CoinFactsNotes - str - add to description?
    """

    result["pcgs_number"] = int(coin_data["PCGSNo"])
    if coin_data["CertNo"] != "":
        result["sku"] = coin_data["CertNo"]
    result["title"] = coin_data["Name"]
    result["year"] = coin_data["Year"]
    result["sale_price"] = coin_data["PriceGuideValue"]
    result["grading"] = GradingServices.objects.get(name=grading_service).id
    mint = coin_data["MintLocation"]
    mints = SelectOneMint.objects.all()
    for m in mints:
        if mint in m.coin_mint:
            result["mint"] = m.id
    # Strike and Grade
    regex_pattern = r"^([A-Za-z]+)(\d+)([A-Za-z+]+)?$"
    strike_and_grade = coin_data["Grade"]
    matches = re.match(regex_pattern, strike_and_grade)
    if matches:
        strike = matches.group(1)  # "MS"
        grade = int(matches.group(2))  # 66
        extra = matches.group(3)  # "FB"
        if extra == "+":
            grade = f"{grade}+"
        strike_id = Strike.objects.get(strike=strike).id
        result["strike"] = strike_id
        grade_id = CoinGrades.objects.get(grade=grade).id
        result["grade"] = grade_id
    else:
        result["strike"] = None
        result["grade"] = None
    # Family
    metal = coin_data["MetalContent"]
    if "Gold" in metal:
        result["family"] = CoinFamily.objects.get(type="Gold").id
    elif "Silver" in metal:
        result["family"] = CoinFamily.objects.get(type="Silver").id
    elif "Clad" in metal:
        result["family"] = CoinFamily.objects.get(type="Clad").id
    elif "Nickel" in metal:
        result["family"] = CoinFamily.objects.get(type="Nickel").id
    elif "Copper" in metal:
        result["family"] = CoinFamily.objects.get(type="Copper").id
    # Denomination
    denomination = coin_data["Denomination"]
    result["denomination"] = Denominations.objects.get(
        denomination_of_coin=denomination, family=result["family"]
    ).id
    # Coin Type
    try:
        coin_type = coin_data["SeriesName"][0]
        coin_types_db = CoinTypeName.objects.all()
        for ct in coin_types_db:
            if (
                coin_type in ct.coin_type
                and ct.denominations.id == result["denomination"]
            ):
                result["coin_type"] = ct.id
    except:
        pass
    return JsonResponse(result)
