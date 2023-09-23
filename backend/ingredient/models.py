from django.db import models
from base_model.models import BaseModel
from recipe.models import Recipe
from unit.models import Unit


class Ingredient(BaseModel):
    recipe = models.ForeignKey(Recipe, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Рецепт')
    name = models.CharField()
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Единица измерения')

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self) -> str:
        return f'{self.name} {str(self.unit)}'
