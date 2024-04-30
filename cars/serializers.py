from rest_framework import serializers
from .models import CarModel


class CarModelSerializerPartial(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    brand = serializers.CharField(max_length=20)
    year = serializers.IntegerField()


class CarModelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    brand = serializers.CharField(max_length=20)
    year = serializers.IntegerField()
    seats = serializers.IntegerField()
    type = serializers.CharField(max_length=20)
    volume = serializers.FloatField()

    def create(self, validated_data):
        car = CarModel.objects.create(**validated_data)
        return car

    def update(self, instance, validated_data: dict):
        for k, v in validated_data.items():
            setattr(instance, k, v)
        instance.save()
        return instance




