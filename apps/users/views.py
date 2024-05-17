from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import UsersSerializer
from .models import UserAutoParks


class UsersListCreateView(ListCreateAPIView):
    queryset = UserAutoParks.objects.all()
    serializer_class = UsersSerializer


class UsersRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = UserAutoParks.objects.all()
    serializer_class = UsersSerializer
