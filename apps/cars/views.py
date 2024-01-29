from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CarModel
from .serializers import CarSerializer
from rest_framework.generics import get_object_or_404, GenericAPIView


class CarsListCreateView(APIView):

    def get(self, *args, **kwargs):
        cars = CarModel.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)


class CarsReadUpdateDeleteView (GenericAPIView):
    queryset = CarModel.objects.all()

    def get(self, *args, **kwargs):
        car = self.get_object()
        serializer = CarSerializer(car)
        return Response(serializer.data)

    def put(self, *args, **kwargs):
        car = self.get_object()
        data = self.request.data
        serializer = CarSerializer(car, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        car = self.get_object()
        data = self.request.data
        serializer = CarSerializer(car, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        car = self.get_object()
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)








