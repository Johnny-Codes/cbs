from django.db import models
from django.contrib.auth.models import AbstractUser


class Business(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Businesses"
        verbose_name = "Business Name"


class User(AbstractUser):
    business = models.ForeignKey(
        Business,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "Users"
        verbose_name = "User"
