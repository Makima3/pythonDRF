# Generated by Django 5.0.5 on 2024-05-17 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0003_rename_usersmodel_usermodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserModel',
            new_name='UsersModel',
        ),
    ]
