from django.forms import ModelForm
from coins.models import CoinInventory

# from accounts.models import Business
# from cbs.settings import AUTH_USER_MODEL as User


class CoinInventoryForm(ModelForm):
    class Meta:
        model = CoinInventory
        fields = [
            "year",
            "mint",
            "denomination",
            "description",
            "strike",
            "grading",
            "grade",
        ]
