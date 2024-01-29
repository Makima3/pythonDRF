from django.urls import path
from .views import CarsListCreateView, CarsReadUpdateDeleteView


urlpatterns = [
    path('',CarsListCreateView.as_view(), name='cars_list_create'),
    path('/<int:pk>', CarsReadUpdateDeleteView.as_view(), name='cars_read_update_delete')
]