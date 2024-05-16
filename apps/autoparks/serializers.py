from rest_framework import serializers

from .models import AutoParkModel


class AutoParkModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoParkModel
        fields = ('id', 'name')