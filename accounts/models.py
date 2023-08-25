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
