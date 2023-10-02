from invoice.models import SalesInvoice
from rest_framework import serializers
from coins.serializers.coinbasemodelserializer import CoinBaseModelSerializer
from customers.serializers import CustomersSerializer


class SalesInvoiceSerializer(serializers.ModelSerializer):
    sales_item = CoinBaseModelSerializer(many=True)
    customer = CustomersSerializer()

    class Meta:
        model = SalesInvoice
        fields = "__all__"
