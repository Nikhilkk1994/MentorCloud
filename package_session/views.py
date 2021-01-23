from rest_framework import mixins as rest_mixins
from rest_framework.viewsets import GenericViewSet

from rest_framework import pagination as rest_pagination

from package_session import serializers as package_session_serializer
from package_session import models as package_session_models


class PackageSessionPagination(rest_pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    invalid_page_message = 'Page out of range'


class PackageSessionView(rest_mixins.ListModelMixin, GenericViewSet):
    """
    View Set for get the list of Testimonial
    """
    serializer_class = package_session_serializer.PackageSessionSerializer
    queryset = package_session_models.PackageSessions.objects.all()
    pagination_class = PackageSessionPagination
