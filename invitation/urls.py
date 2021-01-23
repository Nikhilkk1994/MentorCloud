from rest_framework import routers

from invitation import views as api_views

router = routers.SimpleRouter()

router.register(r'invitation', api_views.InvitationView, basename='invitation')

urlpatterns = []

urlpatterns += router.urls
