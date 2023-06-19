from ..serializers.silverdollarserializer import (
    SilverDollarsSerializer,
    BulkSilverDollarsSerializer,
)
from ..models.silverdollars import (
    SilverDollars,
    BulkSilverDollars,
)
from rest_framework import mixins, generics


class SilverDollarsSerializerView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = SilverDollars.objects.all()
    serializer_class = SilverDollarsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SilverDollarsDetailSerializerView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    serializer_class = SilverDollarsSerializer

    def get_queryset(self):
        id = self.kwargs["id"]
        queryset = SilverDollars.objects.filter(id=id)
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BulkSilverDollarsSerializerView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = BulkSilverDollars.objects.all()
    serializer_class = BulkSilverDollarsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BulkSilverDollarsDetailSerializerView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    serializer_class = BulkSilverDollarsSerializer

    def get_queryset(self):
        id = self.kwargs["id"]
        queryset = BulkSilverDollars.objects.filter(id=id)
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
