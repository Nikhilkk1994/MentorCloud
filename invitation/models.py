from __future__ import unicode_literals

from random import randint

from django.db import models
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _


class Invitation(models.Model):
    """
    Model for Customer Invitation
    """

    PENDING, ACCEPTED = 1, 2

    _INVITE_STATUS_CHOICES = (
        (PENDING, _('PENDING')),
        (ACCEPTED, _('ACCEPTED'))
    )
    email = models.EmailField(_('Email'), unique=True)
    status = models.IntegerField(
        choices=_INVITE_STATUS_CHOICES, default=PENDING, verbose_name=_('Status'), db_index=True
    )
    activation_key = models.IntegerField(blank=True, verbose_name=_('Activation'), db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'), db_index=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'), null=True)

    class Meta:
        verbose_name = _('Invitation')
        verbose_name_plural = _('Invitations')

    def __str__(self):
        return self.email

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.activation_key = randint(1000, 9999)
        super(Invitation, self).save(force_insert, force_update, using, update_fields)
        # check the status of the Invitation
        if self.status == Invitation.PENDING:
            self.send_invitation_email()

    def send_invitation_email(self):
        # send_mail(
        #     subject='[MentorBaba] Activation Code - New Registration - MentorBaba',
        #     message='',
        #     from_email='nikhil.kaplas@gmail.com', recipient_list=[self.email],
        #     html_message=render_to_string('verification_email.html', {'OPT': self.activation_key})
        # )
        pass
