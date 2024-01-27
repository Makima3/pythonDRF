from django.db import models


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'
    brand = models.CharField(max_length=20)
    year = models.IntegerField()
    car_type = models.CharField(max_length=20)
    number_of_seats = models.IntegerField()
    volume_engine = models.FloatField()
