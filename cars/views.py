from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CarModel
from .serializers import CarListCreateSerializer, CarCreateReadUpdateDeleteSerializer


class CarListCreateView(APIView):
    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarListCreateSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()

        return Response(serializer.data)

    def get(self, *args, **kwargs):
        cars = CarModel.objects.all()
        serializer = CarListCreateSerializer(cars, many=True)
        return Response(serializer.data)


class CarCreateReadUpdateDeleteView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            raise Http404
        serializer = CarCreateReadUpdateDeleteSerializer(car)
        return Response(serializer.data)

    def put(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            raise Http404
        data = self.request.data
        serializer = CarCreateReadUpdateDeleteSerializer(car, data=data)

        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data)

    def delete(self, *args, **kwargs):
        return Response("ll")

    def patch(self, *args, **kwargs):
        return Response("o")