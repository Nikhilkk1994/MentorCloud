from rest_framework import mixins as rest_mixins
from rest_framework.viewsets import GenericViewSet

from rest_framework import pagination as rest_pagination

from testimonial import serializers as testimonial_serializer
from testimonial import models as testimonial_models


class TestimonialPagination(rest_pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    invalid_page_message = 'Page out of range'


class TestimonialView(rest_mixins.ListModelMixin, rest_mixins.RetrieveModelMixin, GenericViewSet):
    """
    View Set for get the list of Testimonial
    """
    serializer_class = testimonial_serializer.TestimonialSerializer
    queryset = testimonial_models.Testimonial.objects.order_by('id')
    pagination_class = TestimonialPagination
