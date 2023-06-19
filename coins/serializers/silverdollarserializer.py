from rest_framework import serializers
from ..models.silverdollars import SilverDollars, BulkSilverDollars


class SilverDollarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SilverDollars
        fields = [
            "id",
            "sku",
            "pcgs_number",
            "year",
            "denomination",
            "description",
            "strike",
            "grading",
            "grade",
            "cost",
            "sale_price",
            "dollar_type",
            "business",
            "__str__",
        ]


class BulkSilverDollarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulkSilverDollars
        fields = [
            "id",
            "sku",
            "pcgs_number",
            "year_1",
            "year_2",
            "denomination",
            "description",
            "strike",
            "grading",
            "grade_1",
            "grade_2",
            "cost",
            "quantity",
            "sale_price",
            "average_cost",
            "dollar_type",
            "business",
            "__str__",
        ]
