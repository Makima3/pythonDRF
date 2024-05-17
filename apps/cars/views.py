from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import CarModel
from .serializers import CarModelSerializer
from apps.cars.managers import CarManager


class CarListCreateView(ListCreateAPIView):
    queryset = CarModel.objects.get_audi_only()
    serializer_class = CarModelSerializer


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer

