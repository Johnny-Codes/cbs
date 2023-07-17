from .models import Images
from .serializers import ImageSerializer
from rest_framework import mixins, generics


# Create your views here.
class ImageSerializerView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
