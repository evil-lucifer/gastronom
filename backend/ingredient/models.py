from django.db import models
from base_model.models import BaseModel
from recipe.models import Recipe
from unit.models import Unit


class Ingredient(BaseModel):
    name = models.CharField(verbose_name='Название')
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Единица измерения')

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        unique_together = ('name', 'unit')

    def __str__(self) -> str:
        return f'{self.name} {str(self.unit)}'
