from django.db import models


class Denominations(models.Model):
    DENOM = (
        ("$50", "$50"),
        ("$25", "$25"),
        ("$20", "$20"),
        ("$10", "$10"),
        ("$5", "$5"),
        ("$4", "$4"),
        ("$3", "$3"),
        ("$2.5", "$2.5"),
        ("$1", "$1"),
        ("50C", "50C"),
        ("25C", "25C"),
        ("20C", "20C"),
        ("10C", "10C"),
        ("5C", "5C"),
        ("3CN", "3CN"),
        ("3CS", "3CS"),
        ("2C", "2C"),
        ("1C", "1C"),
        ("H1C", "H1C"),
    )
    denomination = models.CharField(max_length=4, choices=DENOM, default="$1")

    class Meta:
        abstract = True
