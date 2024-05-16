from rest_framework import serializers

from .models import UserAutoParks


class UserAutoParksSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAutoParks
        fields = ('id', 'name', 'lastname')