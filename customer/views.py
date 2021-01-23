from rest_framework import mixins as rest_mixins
from rest_framework import status as http_status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from customer import serializers as customer_serializers


class UserLogin(rest_mixins.CreateModelMixin, GenericViewSet):
    """
    ViewSet for login
    """
    serializer_class = customer_serializers.UserLoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get('user')
        return Response(
            customer_serializers.BaseUserSerializer(instance=user).data,
            status=http_status.HTTP_201_CREATED
        )


class UserSignUp(GenericViewSet):
    """
    View Set for user sign Up
    """
    serializer_class = customer_serializers.UserSignSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=http_status.HTTP_201_CREATED)
