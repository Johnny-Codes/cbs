from django.db import models


class SelectMints(models.Model):
    philadelphia = models.BooleanField(default=False)
    san_francisco = models.BooleanField(default=False)
    denver = models.BooleanField(default=False)
    carson_city = models.BooleanField(default=False)
    west_coast = models.BooleanField(default=False)
    charlotte = models.BooleanField(default=False)
    new_orleans = models.BooleanField(default=False)
    dahlonega = models.BooleanField(default=False)

    class Meta:
        abstract = True


class SelectOneMint(models.Model):
    MINTS = (
        ("P", "Philadelphia Mint"),
        ("S", "San Francisco Mint"),
        ("D", "Denver Mint"),
        ("CC", "Carson City Mint"),
        ("W", "West Point Mint"),
        ("C", "Charlotte Mint"),
        ("O", "New Orleans Mint"),
        ("DL", "Dahlonega Mint"),
    )
    mint = models.CharField(max_length=2, choices=MINTS, default="P")

    class Meta:
        abstract = True
