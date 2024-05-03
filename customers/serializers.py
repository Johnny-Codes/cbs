from customers.models import Customer
from rest_framework import serializers


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "business",
            "address_1",
            "address_2",
            "city",
            "state",
            "zip_code",
            "is_deleted",
        )
