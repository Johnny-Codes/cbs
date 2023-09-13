from invoice.models import SalesInvoice
from rest_framework import serializers


class SalesInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesInvoice
        fields = "__all__"
