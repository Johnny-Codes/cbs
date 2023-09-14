from django.http import JsonResponse
import json
from invoice.serializers import SalesInvoiceSerializer
from invoice.models import SalesInvoice
from accounts.models import User
from customers.models import Customers
from coins.models.coinbasemodel import CoinBaseModel
from rest_framework.response import Response
from rest_framework import mixins, generics
from rest_framework import status


class SalesInvoiceSerializerView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = SalesInvoice.objects.all()
    serializer_class = SalesInvoiceSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        body = request.body
        items = json.loads(body.decode())
        print("items", items)
        sales_invoice = SalesInvoice()
        sales_invoice.save()
        customer = Customers.objects.get(id=1)
        sales_invoice.customer.add(customer)
        # print("customer", customer)
        print("sales invoice", sales_invoice.id)
        # sales_invoice.save()
        # print("sales invoice after first save", sales_invoice)
        for item in items:
            print("item", item)
            try:
                sale_item = CoinBaseModel.objects.get(sku=item["sku"])
                print("sale item", sale_item)
                sales_invoice.sales_item.add(sale_item)
                print("invoice in try statement", sales_invoice)
            except CoinBaseModel.DoesNotExist:
                print("doesn't exist")
                return JsonResponse({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)
        print("sales invoice", sales_invoice)
        sales_invoice.save()
        return JsonResponse({"status": "success", "sales invoice": sales_invoice.id}, status=status.HTTP_200_OK)