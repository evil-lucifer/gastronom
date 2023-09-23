from django.db import models
from base_model.models import BaseModel
from recipe.models import Recipe


class NutritionalFacts(BaseModel):
    recipe = models.ForeignKey(Recipe, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Рецепт')
    proteins = models.IntegerField(verbose_name='Белки')
    carbohydrates = models.IntegerField(verbose_name='Углеводы')
    fats = models.IntegerField(verbose_name='Жиры')

    class Meta:
        verbose_name = 'Пищевая ценнность'
        verbose_name_plural = 'Пищевая ценность'

    @property
    def calorie(self) -> int:
        return int(self.proteins * 4 + self.fats * 9 + self.carbohydrates * 4)
