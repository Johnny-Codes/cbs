from django.db import models

STRIKE = (
    ("MS", "Business/Mint State"),
    ("PR", "Proof"),
    ("RPR", "Reverse Proof"),
    ("PL", "Proof Like"),
    ("DMPL", "DMPL"),
    ("STN", "Satin"),
    ("BRN", "Burnished"),
)


class Strike(models.Model):
    strike = models.CharField(
        max_length=4,
        choices=STRIKE,
        default="MS",
        unique=True,
    )

    def __str__(self):
        return self.strike

    class Meta:
        verbose_name_plural = "Strikes"
        verbose_name = "Strike"
