from django.urls import path

from .views import CarRetrieveUpdateDestroyView, CarListCreateView

urlpatterns = [
    path('', CarListCreateView.as_view(), name='car_list_create'),
    path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view(), name='car_retrieve_update_destroy'),
]