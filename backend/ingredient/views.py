from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from ingredient.models import Ingredient


class IngredientView(GenericViewSet, ListModelMixin):
    queryset = Ingredient.objects.all()
