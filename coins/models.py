from django.db import models
from accounts.models import Business
from core.models import CreatedUpdated


# Create your models here.
class CoinBaseModel(models.Model):
    year = models.IntegerField()
    MINTS = (
        ("P", "P"),
        ("S", "S"),
        ("D", "D"),
        ("CC", "CC"),
        ("W", "W"),
        ("C", "C"),
        ("O", "O"),
        ("M", "M"),
    )
    mint = models.CharField(max_length=2, choices=MINTS, default="P")
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
    description = models.TextField(null=True, blank=True)
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
    GRADING_SERVICES = (
        ("PCGS", "PCGS"),
        ("NGC", "NGC"),
        ("PCGSCAC", "PCGS CAC"),
        ("NGCCAC", "NGC CAC"),
        ("ANACS", "ANACS"),
        ("ICG", "ICG"),
        ("PCGSoNGC", "PCGS or NGC"),
        ("PCGSoNGCaCAC", "PCGS or NGC and CAC"),
        ("Ungraded", "Ungraded"),
    )
    grading = models.CharField(
        max_length=15,
        choices=GRADING_SERVICES,
        default="PCGS",
    )
    GRADES = (
        ("70", "70"),
        ("69+", "69+"),
        ("69", "69"),
        ("68+", "68+"),
        ("68", "68"),
        ("67+", "67+"),
        ("67", "67"),
        ("66+", "66+"),
        ("66", "66"),
        ("65+", "65+"),
        ("65", "65"),
        ("64+", "64+"),
        ("64", "64"),
        ("63+", "63+"),
        ("63", "63"),
        ("62+", "62+"),
        ("62", "62"),
        ("61+", "61+"),
        ("61", "61"),
        ("60+", "60+"),
        ("60", "60"),
        ("58", "58"),
        ("55", "55"),
        ("50", "50"),
        ("45", "45"),
        ("40", "40"),
        ("35", "35"),
        ("30", "30"),
        ("25", "25"),
        ("20", "20"),
        ("15", "15"),
        ("12", "12"),
        ("10", "10"),
        ("08", "08"),
        ("06", "06"),
        ("04", "04"),
        ("03", "03"),
        ("02", "02"),
        ("01", "01"),
        ("BU", "BU"),
        ("CU", "CU"),
        ("UNC", "UNC"),
        ("AU+", "AU+"),
        ("AU", "AU"),
        ("XF+", "XF+"),
        ("XF", "XF"),
        ("VF+", "VF+"),
        ("VF", "VF"),
        ("F+", "F+"),
        ("F", "F"),
        ("VG+", "VG+"),
        ("VG", "VG"),
        ("G+", "G+"),
        ("G", "G"),
    )
    grade = models.CharField(max_length=3, choices=GRADES, default="70")

    def __str__(self):
        return f"{self.year}-{self.mint} {self.denomination}\
              {self.grading} {self.grade}"

    class Meta:
        abstract = True


class SilverDollars(models.Model):
    SILVER_DOLLARS = (
        ("Flowing Hair Dollar", "Flowing Hair Dollar"),
        ("Draped Bust Dollar", "Draped Bust Dollar"),
        ("Liberty Seated Dollar", "Liberty Seated Dollar"),
        ("Trade Dollar", "Trade Dollar"),
        ("Morgan Dollar", "Morgan Dollar"),
        ("Peace Dollar", "Peace Dollar"),
        ("Ike Dollar", "Ike Dollar"),
        ("Susan B. Anthony Dollar", "Susan B. Anthony Dollar"),
        ("Sacagawea Dollar", "Sacagawea Dollar"),
        ("Presidential Dollar", "Presidential Dollar"),
        ("American Innovation Dollar", "American Innovation Dollar"),
    )
    dollar_type = models.CharField(max_length=30, choices=SILVER_DOLLARS)


class CoinInventory(CoinBaseModel, CreatedUpdated):
    business = models.ForeignKey(
        Business,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="business",
    )
