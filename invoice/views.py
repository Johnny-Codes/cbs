from django.http import JsonResponse
import json
from invoice.serializers import SalesInvoiceSerializer

from rest_framework.response import Response
from rest_framework import mixins, generics
from rest_framework import status


class SalesInvoiceSerializerView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    serializer_class = SalesInvoiceSerializer

    def post(self, request, *args, **kwargs):
        body = request.body
        items = json.loads(body.decode())
        for item in items:
            print(item)
        return JsonResponse({"status": "ok"})
