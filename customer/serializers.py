from django.utils.translation import ugettext_lazy as _

from rest_framework.authtoken.models import Token
from rest_framework import (
    serializers as rest_serializers,
    exceptions as rest_exceptions
)

from customer import models as customer_models
from invitation import models as invitation_models


class BaseUserSerializer(rest_serializers.ModelSerializer):
    """
    Serializer for user(customer, ect)
    """
    access_token = rest_serializers.SerializerMethodField()

    class Meta:
        model = customer_models.User
        fields = ('email', 'first_name', 'last_name', 'access_token',)

    def get_access_token(self, instance):
        return Token.objects.get(user=instance).key


class UserLoginSerializer(rest_serializers.Serializer):
    """
    Serializer for User Login In
    """
    email = rest_serializers.EmailField(label=_('Email ID'))
    password = rest_serializers.CharField(
        label=_('Password'), write_only=True, style={'input_type': 'password'}
    )

    def validate(self, attrs):
        user = customer_models.User.objects.filter(email=attrs.get('email')).first()
        if not user or not user.check_password(attrs.get('password')):
            raise rest_exceptions.ValidationError(_('Email/Password is incorrect.'))
        attrs['user'] = user
        return attrs


class UserSignSerializer(rest_serializers.Serializer):
    """
    Serializer for User Sign Up
    """
    email = rest_serializers.EmailField(required=True, help_text=_('Email'))
    first_name = rest_serializers.CharField(max_length=30, required=True, help_text=_('First Name'))
    last_name = rest_serializers.CharField(max_length=30, required=True, help_text=_('Last Name'))
    password = rest_serializers.CharField(max_length=40, required=True, help_text=_('password'), write_only=True)
    opt = rest_serializers.IntegerField(required=True, help_text=_('OTP'), write_only=True)
    access_token = rest_serializers.SerializerMethodField()

    def get_access_token(self, instance):
        return Token.objects.get(user=customer_models.User.objects.get(email=instance.get('email'))).key

    def validate(self, attrs):
        # check email is already exists
        invitation_object = invitation_models.Invitation.objects.filter(email=attrs.get('email'))
        if not invitation_object.exists():
            raise rest_exceptions.ValidationError(_('Email is not verify. Please verify the email by sign up again.'))
        if (
                invitation_object.filter(status=invitation_models.Invitation.ACCEPTED).exists() or
                customer_models.User.objects.filter(email=attrs.get('email')).exists()
        ):
            raise rest_exceptions.ValidationError('User is already exists with email {}'.format(attrs.get('email')))
        # validate the OPT
        if not (attrs.get('opt') == invitation_object.first().activation_key):
            raise rest_exceptions.ValidationError(_('Enter the invalid OTP {}'.format(attrs.get('opt'))))
        # create the object
        invitation = invitation_object.first()
        instance = customer_models.User.objects.create(
            email=attrs.get('email'), first_name=attrs.get('first_name'), last_name=attrs.get('last_name'),
            password=attrs.get('password')
        )
        instance.set_password(attrs.get('password'))
        invitation.status = invitation_models.Invitation.ACCEPTED
        invitation.save()
        instance.save()
        return attrs
