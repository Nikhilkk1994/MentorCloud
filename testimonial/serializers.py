from rest_framework import serializers as rest_serializers

from testimonial import models as testimonial_models


class TestimonialSerializer(rest_serializers.ModelSerializer):
    """
    Serializer for testimonial
    """
    image = rest_serializers.SerializerMethodField()

    class Meta:
        model = testimonial_models.Testimonial
        fields = ('id', 'first_name', 'last_name', 'description', 'company_name', 'image',)

    def get_image(self, instance):
        if instance.image:
            return instance.image.url
        return None
