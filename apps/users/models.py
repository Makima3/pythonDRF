from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class UsersModel(models.Model, AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'auth_user'

    email = models.EmailField(unique=True)

