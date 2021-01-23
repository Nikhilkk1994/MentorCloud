from rest_framework import serializers as rest_serializers

from package_session import models as package_session_models


class PackageSessionSerializer(rest_serializers.ModelSerializer):
    """
    Serializer for Package Session.
    """
    image = rest_serializers.SerializerMethodField()

    class Meta:
        model = package_session_models.PackageSessions
        fields = ('id', 'name', 'description', 'image',)

    def get_image(self, instance):
        if instance.image:
            return instance.image.url
        return None
