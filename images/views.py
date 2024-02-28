from rest_framework import mixins, generics
from rest_framework.response import Response
from .serializers import ImageSerializer
from .models import Images
from coins.models.coinbasemodel import CoinBaseModel


class ImageSerializerView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        coin_id = request.data.get("coin_id")
        coin = CoinBaseModel.objects.get(id=coin_id)
        for key, image in request.data.items():
            if "images" in key:
                image_instance = Images.objects.create(image=image)
                coin.images.add(image_instance)
        coin.save()
        return Response({"status": "success"}, status=200)


class CoinImageView(generics.RetrieveDestroyAPIView):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer
    lookup_field = "id"
