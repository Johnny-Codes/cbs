from customers.models import Customer
from rest_framework import serializers
from accounts.serializers import BusinessSerializer


class CustomersSerializer(serializers.ModelSerializer):
    business = BusinessSerializer(read_only=True)

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
