from django.db import models


# Create your models here.
class Images(models.Model):
    image = models.ImageField(upload_to="images/")

    class Meta:
        verbose_name_plural = "Images"
        verbose_name = "Image"
