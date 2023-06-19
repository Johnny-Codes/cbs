from django.shortcuts import render
from .serializers.sku_serializer import SKUSerializer
from .models.sku import SKU
from rest_framework import mixins, generics


class SKUSerializerView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = SKU.objects.all()
    serializer_class = SKUSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
