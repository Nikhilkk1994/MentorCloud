from __future__ import unicode_literals

from rest_framework import (
    serializers as rest_serializers,
    exceptions as rest_exceptions
)
from django.utils.translation import ugettext_lazy as _

from invitation import models as invitation_models


class InvitationSerializer(rest_serializers.Serializer):
    """
    Serializer for Invitation
    """
    email = rest_serializers.EmailField(required=True, help_text=_('Email ID'))

    def validate(self, attrs):
        # check the invitation object exists
        invitation_object = invitation_models.Invitation.objects.filter(
            email=attrs.get('email'), status=invitation_models.Invitation.ACCEPTED
        )
        if invitation_object.exists():
            raise rest_exceptions.ValidationError('User with email {} already exists'.format(attrs.get('email')))
        return attrs


class InvitationResendSerializer(rest_serializers.Serializer):
    """
    Serializer for Resend Invitation OTP
    """
    email = rest_serializers.EmailField(required=True, help_text=_('Email ID'))

    def validate(self, attrs):
        invitation_object = invitation_models.Invitation.objects.filter(email=attrs.get('email'))
        if invitation_object.filter(status=invitation_models.Invitation.ACCEPTED).exists():
            raise rest_exceptions.ValidationError('User with email {} already exists'.format(attrs.get('email')))
        if not invitation_object.exists():
            raise rest_exceptions.ValidationError('User with email {} is not verified'.format(attrs.get('email')))
        invitation_object.first().save()
        return attrs
