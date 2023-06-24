from django.shortcuts import render
from django.contrib import messages
from .forms import EmailForm
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def contact_page(request):
    form = EmailForm()
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thank you for signing up! Please watch \
                             your inbox for more information.",
            )
            return render(
                request,
                "contact/contact.html",
                {"form": EmailForm()},
            )
        else:
            messages.error(request, "Something went wrong, please try again.")
    context = {
        "form": form,
    }
    return render(request, "contact/contact.html", context)
