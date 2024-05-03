from django.db import models
from accounts.models import User
from core.models import SoftDeleteModel


class Customer(
    SoftDeleteModel,
    User,
):
    phone_number = models.CharField(
        max_length=11,
        blank=True,
        null=True,
    )
    address_1 = models.CharField(
        max_length=64,
        blank=True,
        null=True,
    )
    address_2 = models.CharField(
        max_length=64,
        blank=True,
        null=True,
    )
    city = models.CharField(
        max_length=64,
        blank=True,
        null=True,
    )
    state = models.CharField(
        max_length=2,
        blank=True,
        null=True,
    )
    zip_code = models.CharField(
        max_length=10,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.username


class StripeTenantCustomer(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    stripe_id = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Stripe Tenant Customers"
        verbose_name = "Stripe Tenant Customer"

    # def get_stripe_id(self):
    #     """
    #     Get the stripe customer id from the stripe API
    #     by providing the user email
    #     """
    #     url = f"https://api.stripe.com/v1/customers?email={self.user.email}"
    #     response = r.get(url, headers={"Authorization": f"Bearer {settings.STRIPE_SECRET_KEY}"})
    #     data = response.json()
    #     return data["data"][0]["id"]
