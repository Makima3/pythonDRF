from django.db import models


class CarModel(models.Model):
    class Meta:
        db_table = 'car'
    brand = models.CharField(max_length=20)
    year = models.IntegerField()
    seats = models.IntegerField()
    type = models.CharField(max_length=20)
    volume = models.FloatField()
