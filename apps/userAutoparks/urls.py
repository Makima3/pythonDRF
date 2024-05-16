from django.urls import path

from .views import UserAutoParksRetrieveUpdateDestroyView, UserAutoParksListCreateView

urlpatterns = [
    path('', UserAutoParksListCreateView.as_view(), name='userAutoParks_list_create'),
    path('/<int:pk>', UserAutoParksRetrieveUpdateDestroyView.as_view(), name='userAutoParks_retrieve_update_destroy'),
]