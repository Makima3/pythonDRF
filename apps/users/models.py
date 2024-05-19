from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager


class UsersModel(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'auth_user'

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=120)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()


class ProfileModel(models.Model):
    class Meta:
        db_table = 'profile'
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.IntegerField()
    user = models.OneToOneField(UsersModel, on_delete=models.CASCADE)
