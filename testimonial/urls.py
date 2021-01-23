from __future__ import unicode_literals

from rest_framework import routers

from testimonial import views as api_views

router = routers.SimpleRouter()

router.register(r'testimonial', api_views.TestimonialView, basename='testimonial')

urlpatterns = []

urlpatterns += router.urls
