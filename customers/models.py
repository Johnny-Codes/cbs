from django.db import models
from accounts.models import User


class Customers(User):
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
