from django.contrib import admin

# Register your models here.
from customers.models import Customers


@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
    )
