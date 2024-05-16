from django.urls import path

from .views import AutoParkListCreateView, AutoParkRetrieveUpdateDestroyView


urlpatterns = [
    path('', AutoParkListCreateView.as_view(), name='autopark_list_create'),
    path('/<int:pk>', AutoParkRetrieveUpdateDestroyView.as_view(), name='autopark_retrieve_update_destrot'),
]