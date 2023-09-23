from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import ListModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import GenericViewSet


class RecipeView(GenericViewSet, ListModelMixin):
    pagination_class = LimitOffsetPagination
    filter_backends = [SearchFilter, OrderingFilter, ]
    search_fields = ['name']
    ordering_fields = ['name']
