from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.users.serializers import UserSerializer

from django.contrib.auth import get_user_model

UserModel = get_user_model()


class CreateUserView(CreateAPIView):
    serializer_class = UserSerializer


class UserListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    model = UserModel
    permission_classes = (IsAuthenticated,)
