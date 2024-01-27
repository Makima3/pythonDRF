from rest_framework import serializers
from .models import CarModel


class CarListCreateSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    brand = serializers.CharField(max_length=20)
    year = serializers.IntegerField()

    def create(self, validated_data):
        car = CarModel.objects.create(**validated_data)
        return car


class CarCreateReadUpdateDeleteSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    brand = serializers.CharField(max_length=20)
    car_type = serializers.CharField(max_length=20)
    year = serializers.IntegerField()
    number_of_seats = serializers.IntegerField()
    volume_engine = serializers.FloatField()

    def update(self, instance, validated_data:dict):
        for k, v in validated_data.items():
            setattr(instance, k, v)
        instance.save()
        return instance

