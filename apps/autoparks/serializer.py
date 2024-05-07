from rest_framework import serializers

from .models import AutoParkModel


class AutoParkSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoParkModel
        fields = ('id','autopark_name')
