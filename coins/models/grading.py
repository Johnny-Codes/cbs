from django.db import models
from coins.data.grades import (
    GRADING_SERVICES,
    GRADES,
)


class GradingServices(models.Model):
    name = models.CharField(
        max_length=15,
        choices=GRADING_SERVICES,
        default="PCGS",
        unique=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Grading Services"
        verbose_name = "Grading Service"


class CoinGrades(models.Model):
    grade = models.CharField(
        max_length=3,
        choices=GRADES,
        default="70",
        unique=True,
    )

    def __str__(self):
        return self.grade

    class Meta:
        verbose_name_plural = "Coin Grades"
        verbose_name = "Coin Grades"
