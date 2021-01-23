from __future__ import unicode_literals

from rest_framework import routers

from package_session import views as api_views

router = routers.SimpleRouter()

router.register(r'packages', api_views.PackageSessionView, basename='package_session')

urlpatterns = []

urlpatterns += router.urls
