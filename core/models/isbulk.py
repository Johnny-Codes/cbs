from django.db import models


class IsBulk(models.Model):
    is_bulk = models.BooleanField(default=False)

    class Meta:
        abstract = True
