from django.shortcuts import render
from django.http import JsonResponse
from .serializers.sku_serializer import SKUSerializer
from .models.sku import SKU
from rest_framework import mixins, generics
import random


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


def random_sku(request):
    random_sku = "CBS" + str(random.randint(0, 999999999))
    data = {"random_sku": random_sku}
    return JsonResponse(data)
