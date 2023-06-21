from django.shortcuts import render
from .forms import EmailForm


# Create your views here.
def contact_page(request):
    form = EmailForm()
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "contact/contact.html")
    context = {
        "form": form,
    }
    return render(request, "contact/contact.html", context)
