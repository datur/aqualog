from django.db import models

# Create your models here.
class Tank(models.Model):
    class WaterTypeChoices(models.TextChoices):
        fresh = "1", "FRESH"
        salt = "2", "SALT"
        brackish = "3", "BRACKISH"
    class UnitTypeChoices(models.TextChoices):
        metric = "1", "LITRES"
        imperial = "2", "GALLONS"

    name = models.CharField(max_length=60)
    capacity = models.IntegerField()
    unit_type = models.CharField(max_length=15, choices=UnitTypeChoices.choices, default=UnitTypeChoices.metric)
    water_type = models.CharField(max_length=15,choices=WaterTypeChoices.choices, default=WaterTypeChoices.fresh)

    def __str__(self):
        return self.name