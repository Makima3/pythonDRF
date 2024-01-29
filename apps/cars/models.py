from django.db import models
from core.models import CarBaseModel


class CarModel(CarBaseModel):
    class Meta:
        db_table = 'cars'
    brand = models.CharField(max_length=15)
    year = models.IntegerField()
    volume_engine = models.FloatField()
    color = models.CharField(max_length=20)
