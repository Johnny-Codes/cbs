import os
import base64
import json
import uuid
import requests as r
import re
from PIL import Image
from io import BytesIO
from rest_framework.generics import ListAPIView
from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from coins.serializers.coinbasemodelserializer import (
    CoinBaseModelSerializer,
    CoinSkusOnlySerializer,
)
from coins.models.coinbasemodel import CoinBaseModel
from images.models import Images
from rest_framework.response import Response
from rest_framework import mixins, generics
from rest_framework import status
from django.http import JsonResponse
from coins.models.grading import CoinGrades, GradingServices
from coins.models.strike import Strike
from coins.models.mints import SelectOneMint
from coins.models.denominations import CoinFamily, Denominations, CoinTypeName
from coins.openai_calls import (
    get_product_description_from_text,
    get_product_description_from_photos,
)


class CoinBaseModelSerializerView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    """
    A view for handling the retrieval and creation of CoinBaseModel instances.

    This view supports listing all CoinBaseModel instances and creating new ones.
    It also supports filtering the queryset based on the `is_deleted` field.

    Attributes:
        queryset: The initial queryset that this view will use to list or filter instances.
        serializer_class: The serializer class this view will use to validate and convert data.

    Methods:
        get: Handles GET requests. Supports filtering the queryset based on the `is_deleted` field.
        post: Handles POST requests. Supports creating new CoinBaseModel instances.
    """

    queryset = CoinBaseModel.objects.all()
    serializer_class = CoinBaseModelSerializer

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests.

        If the `is_deleted` query parameter is provided, filter the queryset based on its value.

        Args:
            request: The request instance.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            A list of CoinBaseModel instances.
        """
        is_deleted_param = request.query_params.get("is_deleted", None)

        if is_deleted_param is not None:
            if is_deleted_param.lower() == "true":
                self.queryset = self.queryset.filter(is_deleted=True)
            elif is_deleted_param.lower() == "false":
                self.queryset = self.queryset.filter(is_deleted=False)

        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests.

        Create a new CoinBaseModel instance.

        Args:
            request: The request instance.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            The created CoinBaseModel instance.
        """
        return self.create(request, *args, **kwargs)


class OneCoinBaseModelSerializerView(
    mixins.UpdateModelMixin,
    generics.GenericAPIView,
):
    """
    A view for handling the retrieval and update of a single CoinBaseModel instance.

    This view supports retrieving a CoinBaseModel instance by its ID and updating its fields.
    It also supports a custom "soft delete" operation, which can be triggered by including
    "toggle_soft_delete" in the request data.

    Attributes:
        queryset: The initial queryset that this view will use to retrieve instances.
        serializer_class: The serializer class this view will use to validate and convert data.
        lookup_field: The model field to use for looking up an instance.

    Methods:
        get: Handles GET requests. Returns the CoinBaseModel instance with the given ID.
        put: Handles PUT requests. Updates the CoinBaseModel instance with the given ID.
    """

    queryset = CoinBaseModel.objects.all()
    serializer_class = CoinBaseModelSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests.

        Retrieve the CoinBaseModel instance with the given ID.

        Args:
            request: The request instance.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            The retrieved CoinBaseModel instance.
        """
        coin_instance = self.get_object()
        serializer = self.get_serializer(coin_instance)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        """
        Handle PUT requests.

        If "toggle_soft_delete" is included in the request data, perform a "soft delete"
        operation on the CoinBaseModel instance with the given ID. Otherwise, update its fields.

        Args:
            request: The request instance.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            The updated CoinBaseModel instance, or a 204 No Content response if a "soft delete"
            operation was performed.
        """
        coin_instance = self.get_object()
        if "toggle_soft_delete" in request.data:
            coin_instance.soft_delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        try:
            del request.data["sku"]
        except KeyError:
            pass

        serializer = self.get_serializer(
            coin_instance,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CoinTypeSerializerView(
    mixins.ListModelMixin,
    generics.GenericAPIView,
):
    """
    A view for handling the retrieval of CoinBaseModel instances based on coin type.

    This view supports listing all CoinBaseModel instances of a specific coin type.
    It also supports filtering the queryset based on the `is_deleted` field.

    Attributes:
        queryset: The initial queryset that this view will use to list or filter instances.
        serializer_class: The serializer class this view will use to validate and convert data.
        lookup_field: The model field to use for looking up an instance.

    Methods:
        get: Handles GET requests. Returns the CoinBaseModel instances of the given coin type.
    """

    queryset = CoinBaseModel.objects.all()
    serializer_class = CoinBaseModelSerializer
    lookup_field = "coin_type"

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests.

        If the `coin_type` argument is provided, filter the queryset based on
        its value and the `is_deleted` field.
        Otherwise, return all CoinBaseModel instances.

        Args:
            request: The request instance.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            A list of CoinBaseModel instances.
        """
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
    """
    A view for handling the retrieval of all SKUs from CoinBaseModel instances.

    This view supports listing all SKUs from CoinBaseModel instances.

    Attributes:
        queryset: The initial queryset that this view will use to list instances.
        serializer_class: The serializer class this view will use to convert data.

    Methods:
        get: Handles GET requests. Returns all SKUs from CoinBaseModel instances.
    """

    queryset = CoinBaseModel.objects.all()
    serializer_class = CoinSkusOnlySerializer

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests.

        Retrieve all SKUs from CoinBaseModel instances.

        Args:
            request: The request instance.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            A list of SKUs from CoinBaseModel instances.
        """
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
    print("coin data", coin_data)
    try:
        result["pcgs_number"] = int(coin_data["PCGSNo"])
    except KeyError:
        pass
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
        try:
            strike_id = Strike.objects.get(strike=strike).id
            result["strike"] = strike_id
        except Strike.DoesNotExist:
            result["strike"] = Strike.objects.get(strike="MS").id
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


def get_true_view_images(request, id):
    pcgs_api_key = os.environ.get("PCGS_API_KEY")
    coin = CoinBaseModel.objects.get(id=id)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {pcgs_api_key}",
    }
    url = f"https://api.pcgs.com/publicapi/coindetail/GetCoinFactsByCertNo/{coin.sku}"
    coin_data = r.get(url, headers=headers).json()
    try:
        if coin_data["Images"]:
            images = coin_data["Images"]
            for image in images:
                response = r.get(image["Fullsize"])
                img = Image.open(BytesIO(response.content))
                img_io = BytesIO()
                img.save(img_io, format="JPEG")
                new_image = Images()
                new_image.image.save(
                    f"{uuid.uuid4().hex}.jpg",
                    ContentFile(img_io.getvalue()),
                    save=False,
                )
                new_image.save()
                coin.images.add(new_image)
            return JsonResponse(
                {"message": "Successfully added PCGS True View Images."}
            )
    except Exception as e:
        return JsonResponse({"message": str(e)})
    return JsonResponse({"message": "No images found."})


def get_product_desc_from_text(request, id):
    coin = CoinBaseModel.objects.get(id=id)
    description = get_product_description_from_text(coin.title)
    return JsonResponse({"description": description}, safe=False)


def get_product_desc_from_pictures(request, id):
    coin = CoinBaseModel.objects.get(id=id)

    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")

    img_urls = []
    for image in coin.images.all():
        img_urls.append(encode_image(image.image.path))
    description = get_product_description_from_photos(img_urls)
    return JsonResponse({"description": description})
    # for image in coin.images.all():
    #     img_urls.append(f"http://localhost:8000{image.image.url}")
    # description = get_product_description_from_photos(img_urls)
    # return JsonResponse({"description": description})


class GetCoinInfoBySku(ListAPIView):
    """
    API view to retrieve list of CoinBaseModel instances filtered by SKU.

    Inherits from Django Rest Framework's ListAPIView.

    Attributes:
    serializer_class: Specifies the serializer to use for the view.
    """

    serializer_class = CoinBaseModelSerializer

    def get_queryset(self):
        """
        Overrides the get_queryset method to filter CoinBaseModel instances by SKU.

        Returns:
        A queryset of CoinBaseModel instances that match the provided SKU.
        """

        sku = self.kwargs["sku"]
        return CoinBaseModel.objects.filter(sku=sku)
