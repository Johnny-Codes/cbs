from rest_framework import serializers
from accounts.models import User, Business


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "business",
        ]


class BusinessSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Business
        fields = ["id", "name", "user"]
