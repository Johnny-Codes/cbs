from invoice.models import SalesInvoice
from rest_framework import serializers
from coins.serializers.coinbasemodelserializer import CoinBaseModelSerializer


class SalesInvoiceSerializer(serializers.ModelSerializer):
    sales_item = CoinBaseModelSerializer(many=True)

    class Meta:
        model = SalesInvoice
        fields = "__all__"
