from ..serializers.halfdollarserializer import (
    HalfDollarsSerializer,
    BulkHalfDollarsSerializer,
)
from ..models.halfdollars import (
    HalfDollars,
    BulkHalfDollars,
)
from rest_framework import mixins, generics


class HalfDollarsSerializerView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = HalfDollars.objects.all()
    serializer_class = HalfDollarsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class HalfDollarsDetailSerializerView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    serializer_class = HalfDollarsSerializer

    def get_queryset(self):
        id = self.kwargs["id"]
        queryset = HalfDollars.objects.filter(id=id)
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BulkHalfDollarsSerializerView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = BulkHalfDollars.objects.all()
    serializer_class = BulkHalfDollarsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BulkHalfDollarsDetailSerializerView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    serializer_class = BulkHalfDollarsSerializer

    def get_queryset(self):
        id = self.kwargs["id"]
        queryset = BulkHalfDollars.objects.filter(id=id)
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
