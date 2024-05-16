from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import UserAutoParksSerializer
from .models import UserAutoParks


class UserAutoParksListCreateView(ListCreateAPIView):
    queryset = UserAutoParks.objects.all()
    serializer_class = UserAutoParksSerializer


class UserAutoParksRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = UserAutoParks.objects.all()
    serializer_class = UserAutoParksSerializer
