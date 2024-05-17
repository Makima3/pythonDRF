from django.db import models

from apps.cars.managers import CarManager


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'
    brand = models.CharField(max_length=20)
    year = models.IntegerField()
    price = models.IntegerField()

    objects = CarManager()

