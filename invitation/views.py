from __future__ import unicode_literals

from rest_framework import (
    mixins as rest_mixins,
)
from rest_framework.decorators import action
from rest_framework import status as http_status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from invitation import models as invitation_models
from invitation import serializers as invitation_serializer
from invitation import mixins as invitation_mixins


class InvitationView(rest_mixins.CreateModelMixin, invitation_mixins.ActionSpecificSerializerMixin, GenericViewSet):
    """
    View Set for Invitation
    """
    serializer_classes = {
        'create': invitation_serializer.InvitationSerializer,
        'resend_opt': invitation_serializer.InvitationResendSerializer
    }
    serializer_class = invitation_serializer.InvitationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.data
        invitation, created = invitation_models.Invitation.objects.get_or_create(**validated_data)
        if not created:
            invitation.save()
        return Response(serializer.data, status=http_status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def resend_opt(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'message': 'OTP is send to your email'}, status=http_status.HTTP_200_OK)
