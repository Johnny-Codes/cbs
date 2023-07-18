from django.db import models


class SelectMints(models.Model):
    philadelphia = models.BooleanField(default=False)
    san_francisco = models.BooleanField(default=False)
    denver = models.BooleanField(default=False)
    carson_city = models.BooleanField(default=False)
    west_point = models.BooleanField(default=False)
    charlotte = models.BooleanField(default=False)
    new_orleans = models.BooleanField(default=False)
    dahlonega = models.BooleanField(default=False)

    def __str__(self):
        selected_mints = []
        if self.philadelphia:
            selected_mints.append("P")
        if self.san_francisco:
            selected_mints.append("S")
        if self.denver:
            selected_mints.append("D")
        if self.carson_city:
            selected_mints.append("CC")
        if self.west_point:
            selected_mints.append("W")
        if self.charlotte:
            selected_mints.append("C")
        if self.new_orleans:
            selected_mints.append("O")
        if self.dahlonega:
            selected_mints.append("D")
        return ", ".join(selected_mints)

    class Meta:
        verbose_name_plural = "Select Multiple Mints"
        verbose_name = "Select Multiple Mints"


class SelectOneMint(models.Model):
    MINTS = (
        ("Philadelphia Mint", "Philadelphia Mint"),
        ("San Francisco Mint", "San Francisco Mint"),
        ("Denver Mint", "Denver Mint"),
        ("Carson City Mint", "Carson City Mint"),
        ("West Point Mint", "West Point Mint"),
        ("Charlotte Mint", "Charlotte Mint"),
        ("New Orleans Mint", "New Orleans Mint"),
        ("Dahlonega Mint", "Dahlonega Mint"),
    )
    coin_mint = models.CharField(
        max_length=32,
        choices=MINTS,
        default="P",
        unique=True,
    )

    def __str__(self):
        return self.coin_mint

    class Meta:
        verbose_name_plural = "Select One Mint"
        verbose_name = "Select One Mint"
