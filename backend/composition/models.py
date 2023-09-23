from django.db import models
from base_model.models import BaseModel
from ingredient.models import Ingredient
from recipe.models import Recipe


class Сomposition(BaseModel):
    recipe = models.ForeignKey(Recipe, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Рецепт')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.SET_NULL, blank=True,
                                   null=True, verbose_name='Ингредиент')
    count = models.FloatField(verbose_name='Количество')

    class Meta:
        verbose_name = 'Состав'
        verbose_name_plural = 'Состав'
