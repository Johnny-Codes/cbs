from rest_framework import serializers
from ..models.halfdollars import HalfDollars, BulkHalfDollars


class HalfDollarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HalfDollars
        fields = "__all__"


class BulkHalfDollarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulkHalfDollars
        fields = "__all__"
