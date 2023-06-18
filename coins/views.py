from django.shortcuts import render
from coins.forms import CoinInventoryForm
from coins.models import SilverDollars


# Create your views here.
def inventory_form_view(request):
    inventory_form = CoinInventoryForm()
    if request.method == "POST":
        inventory_form = CoinInventoryForm(request.POST)
        if inventory_form.is_valid():
            inventory_form.save()
            return render(
                request,
                "coins/inventory_form.html",
                {
                    "inventory_form": inventory_form,
                },
            )
    context = {
        "inventory_form": inventory_form,
    }
    return render(request, "coins/inventory_form.html", context)


def load_denominations(request):
    denomination = request.GET.get("denomination")
    if denomination == "$1":
        context = {"silver_dollars": SilverDollars.objects.all()}
        return render(request, "coins/silver_dollar_options.html", context)
    else:
        pass
