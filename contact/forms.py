from django.forms import ModelForm
from .models import SubmitEmail


class EmailForm(ModelForm):
    class Meta:
        model = SubmitEmail
        fields = ("email",)
