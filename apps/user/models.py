from django.db import models


class UserModel(models.Model):
    class Meta:
        db_table = 'user'
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)

