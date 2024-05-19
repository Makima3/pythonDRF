from rest_framework.generics import CreateAPIView

from apps.users.serializers import UserSerializer


class CreateUserView(CreateAPIView):
    serializer_class = UserSerializer
