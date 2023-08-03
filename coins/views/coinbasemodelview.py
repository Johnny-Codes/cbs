from coins.serializers.coinbasemodelserializer import CoinBaseModelSerializer
from coins.models.coinbasemodel import CoinBaseModel

from rest_framework.response import Response
from rest_framework import mixins, generics
from rest_framework import status


class CoinBaseModelSerializerView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = CoinBaseModel.objects.all()
    serializer_class = CoinBaseModelSerializer

    def get(self, request, *args, **kwargs):
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
        serializer = self.get_serializer(coin_instance, data=request.data)
        if serializer.is_valid():
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
