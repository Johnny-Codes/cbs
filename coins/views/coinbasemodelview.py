from coins.serializers.coinbasemodelserializer import CoinBaseModelSerializer
from coins.models.coinbasemodel import CoinBaseModel

from rest_framework import mixins, generics


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
