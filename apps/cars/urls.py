from django.urls import path
from .views import CarsListCreateAPIView, CarsReadUpdateDeleteAPIView


urlpatterns = [
    path('',CarsListCreateAPIView.as_view(), name='cars_list_create'),
    path('/<int:pk>', CarsReadUpdateDeleteAPIView.as_view(), name='cars_read_update_delete')
]