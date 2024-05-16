from django.db import models


class UserAutoParks(models.Model):
    class Meta:
        db_table = 'userAutoParks'
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
