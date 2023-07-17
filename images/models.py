import uuid
from django.db import models
import random
import string


def image_file_path(instance, filename):
    extension = filename.split(".")[-1]
    uuid_string = uuid.uuid4().hex
    random_string = "".join(
        random.choices(
            string.ascii_lowercase + string.digits,
            k=12,
        )
    )
    new_filename = f"{uuid_string}{random_string}.{extension}"
    return f"images/{new_filename}"


class Images(models.Model):
    image = models.ImageField(
        upload_to=image_file_path,
        unique=True,
    )

    class Meta:
        verbose_name_plural = "Images"
        verbose_name = "Image"
