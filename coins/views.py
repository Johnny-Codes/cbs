from django.shortcuts import render
from coins.forms import CoinBaseForm
from coins.models import SilverDollars


# Create your views here.
def inventory_form_view(request):
    inventory_form = CoinInventoryForm()
    coin_base_form = CoinBaseForm()
    if request.method == "POST":
        inventory_form = CoinInventoryForm(request.POST)
        coin_base_form = CoinBaseForm(request.POST)
        if inventory_form.is_valid() and coin_base_form.is_valid():
            inventory_form.save()
            coin_base_form.save()
            return render(
                request,
                "coins/inventory_form.html",
                {
                    # "inventory_form": inventory_form,
                    "coin_base_form": coin_base_form,
                },
            )
    context = {
        # "inventory_form": inventory_form,
        "coin_base_form": coin_base_form,
    }
    return render(request, "coins/inventory_form.html", context)


def load_denominations(request):
    denomination = request.GET.get("denomination")
    if denomination == "$1":
        context = {"silver_dollars": SilverDollars.objects.all()}
        return render(request, "coins/silver_dollar_options.html", context)
    else:
        pass
