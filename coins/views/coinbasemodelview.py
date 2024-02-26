import os
import json
import requests as r
from coins.serializers.coinbasemodelserializer import (
    CoinBaseModelSerializer,
    CoinSkusOnlySerializer,
)
from coins.models.coinbasemodel import CoinBaseModel

from rest_framework.response import Response
from rest_framework import mixins, generics
from rest_framework import status
from django.http import JsonResponse


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
        print("request data", request.data)
        print("type of data", type(request.data))

        serializer = self.get_serializer(
            coin_instance,
            data=request.data,
            partial=True,
        )

        # Call .is_valid() before accessing serializer.data
        if serializer.is_valid():
            print("is valid", serializer)
            serializer.save()
            return Response(serializer.data)
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


def pcgs_coin_data(request, *args, **kwargs):
    pcgs_api_key = os.environ.get("PCGS_API_KEY")
    if isinstance(request, dict):
        pcgs_no = request.get("pcgs_no")
    else:
        pcgs_no = json.loads(request.body).get("pcgs_no")
    print("pcgs no", pcgs_no)
    if pcgs_no is None:
        return None
    print("pcgs no", pcgs_no)
    headers = {"authorization": f"bearer {pcgs_api_key}"}
    base_url = (
        f"https://api.pcgs.com/publicapi/coindetail/GetCoinFactsByCertNo/{pcgs_no}"
    )
    coin_data = r.get(base_url, headers=headers).json()
    print(coin_data)
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

    Do I want to format this here or on the frontend? Probably here
    """
    return JsonResponse(coin_data)
