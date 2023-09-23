from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from national_cuisine.models import NationalCuisine


class NationalCuisineView(GenericViewSet, ListModelMixin):
    queryset = NationalCuisine.objects.all()
