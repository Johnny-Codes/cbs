from django.http import JsonResponse
import json
from invoice.serializers import SalesInvoiceSerializer
from invoice.models import SalesInvoice
from accounts.models import User
from customers.models import Customer
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
        items = request.data
        print("sales invoice items", items)
        sales_invoice = SalesInvoice()
        customer_id = items["customer"]
        sales_invoice.sales_json = items
        sales_invoice.customer_id = Customer.objects.get(id=customer_id).id
        sales_invoice.save()

        if items["notes"] != "" and items["notes"] is not None:
            sales_invoice.notes = items["notes"]

        sale_items = []
        for item in items["skus"]:
            try:
                sale_item = CoinBaseModel.objects.get(sku=item["sku"])
                sale_item.update_quantity(method="subtract", qty=int(item["quantity"]))
                sale_items.append(sale_item)
            except CoinBaseModel.DoesNotExist:
                return JsonResponse(
                    {"status": "error"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        sales_invoice.sales_item.add(*sale_items)
        sales_invoice.save()

        return JsonResponse(
            {"status": "success", "sales invoice": sales_invoice.id},
            status=status.HTTP_200_OK,
        )


class SalesInvoiceForCustomerView(
    mixins.ListModelMixin,
    generics.GenericAPIView,
):
    queryset = SalesInvoice.objects.all()
    serializer_class = SalesInvoiceSerializer
    lookup_url_kwarg = "customer_id"

    def get(self, request, *args, **kwargs):
        customer = self.kwargs.get(self.lookup_url_kwarg)
        queryset = self.get_queryset().filter(customer_id=customer)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
