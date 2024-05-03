from django.contrib import admin

# Register your models here.
from customers.models import Customer, StripeTenantCustomer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
    )


@admin.register(StripeTenantCustomer)
class StripeTenantCustomerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "stripe_id",
    )
