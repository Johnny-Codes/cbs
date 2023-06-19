from rest_framework import serializers
from ..models.silverdollars import SilverDollars, BulkSilverDollars


class SilverDollarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SilverDollars
        fields = "__all__"


class BulkSilverDollarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulkSilverDollars
        fields = "__all__"
