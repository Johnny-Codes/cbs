from django.db import models


class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False)

    def soft_delete(self):
        try:
            self.is_deleted = True
            self.save()
            print("soft delete successful")
        except Exception as e:
            print("soft delete failed", e)

    def restore(self):
        self.is_deleted = False
        self.save()

    def hard_delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Deleted: {self.is_deleted}"

    class Meta:
        abstract = True
