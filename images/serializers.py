from rest_framework import serializers
from django.conf import settings
from .models import Images
from coins.models.coinbasemodel import CoinBaseModel


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ["id", "image"]
