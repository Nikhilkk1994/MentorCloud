from django.contrib import admin

from testimonial import models as testimonial_models

# Register your models here.
admin.site.register(testimonial_models.Testimonial)
