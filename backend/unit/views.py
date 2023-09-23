from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from unit.models import Unit


class UnitView(GenericViewSet, ListModelMixin):
    queryset = Unit.objects.all()

