from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .filters import filter_cars
from .models import CarModel
from .serializers import CarSerializer


class CarsListCreateAPIView(ListCreateAPIView):

    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self, *args, **kwargs):
        return filter_cars(self.request.query_params)


class CarsReadUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

