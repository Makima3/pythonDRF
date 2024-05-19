from rest_framework import serializers

from django.contrib.auth import get_user_model
from .models import ProfileModel
from django.db.transaction import atomic

UsersModel = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('id', 'name', 'surname', 'age')


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UsersModel
        fields = ('id', 'email', 'password', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'profile')
        read_only_fields = ('id', 'is_active', 'is_staff', 'is_superuser', 'last_login')
        extra_kwargs = {
            'password': {
                'write_only': True,
            },
        }

    @ atomic
    def create(self, validated_data: dict):
        profile = validated_data.pop('profile')
        user = UsersModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(user=user, **profile)
        return user