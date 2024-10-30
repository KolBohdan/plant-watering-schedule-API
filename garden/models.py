from django.db import models


class Plant(models.Model):
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    watering_frequency_days = models.PositiveIntegerField()
    last_watered_date = models.DateField()

    class Meta:
        ordering = ["-last_watered_date"]

    def __str__(self) -> str:
        return self.name
