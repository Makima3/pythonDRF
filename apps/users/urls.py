from django.urls import path

from .views import CreateUserView, UserListView

urlpatterns = [
    path('', CreateUserView.as_view(), name="create_user"),
    path('/list', UserListView.as_view(), name="user_list"),

]