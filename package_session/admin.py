from django.contrib import admin

from package_session import models as package_session_models

# Register your models here.
admin.site.register(package_session_models.PackageSessions)
