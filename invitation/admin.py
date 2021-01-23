from django.contrib import admin

from invitation import models as invitation_models

# Register your models here.
admin.site.register(invitation_models.Invitation)
