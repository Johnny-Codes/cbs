from customers.models import Customer
from rest_framework import serializers
from accounts.serializers import BusinessSerializer
from accounts.models import Business


class CustomersSerializer(serializers.ModelSerializer):
    business_id = serializers.PrimaryKeyRelatedField(
        source="business",
        queryset=Business.objects.all(),
        required=False,
        allow_null=True,
    )
    business_name = serializers.StringRelatedField(source="business")

    class Meta:
        model = Customer
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "business_id",
            "business_name",
            "address_1",
            "address_2",
            "city",
            "state",
            "zip_code",
            "is_deleted",
        )
