from django.db import models
from django.contrib.auth.models import AbstractUser
import requests as r

class Business(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Businesses"
        verbose_name = "Business Name"


class User(AbstractUser):
    username = models.CharField(
        max_length=32,
        unique=True,
        blank=True,
        null=True,
    )
    email = models.EmailField(unique=True)
    business = models.ForeignKey(
        Business,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "Users"
        verbose_name = "User"


class StripeCustomer(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	stripe_id = models.CharField(max_length=255)

	def __str__(self):
		return self.user.username

	class Meta:
		verbose_name_plural = "Stripe Customers"
		verbose_name = "Stripe Customer"

	def get_stripe_id(self):
		"""
		Get the stripe customer id from the stripe API
		by providing the user email
		"""
		pass
