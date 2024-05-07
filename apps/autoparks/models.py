from django.db import models


class AutoParkModel(models.Model):
    class Meta:
        db_table = 'auto_parks'
    autopark_name = models.CharField(max_length=20)
