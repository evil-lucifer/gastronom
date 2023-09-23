from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from category.models import Category


class CategoryView(GenericViewSet, ListModelMixin):
    queryset = Category.objects.all()
