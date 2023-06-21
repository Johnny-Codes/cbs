from django.db import models


class Strike(models.Model):
    STRIKE = (
        ("MS", "Business/Mint State"),
        ("PR", "Proof"),
        ("RPR", "Reverse Proof"),
        ("PL", "Proof Like"),
        ("DMPL", "DMPL"),
        ("STN", "Satin"),
        ("BRN", "Burnished"),
    )
    strike = models.CharField(max_length=4, choices=STRIKE, default="MS")

    class Meta:
        abstract = True
