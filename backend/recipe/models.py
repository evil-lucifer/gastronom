from base_model.models import BaseModel
from django.db import models

from category.models import Category
from national_cuisine.models import NationalCuisine


class Recipe(BaseModel):
    name = models.CharField(verbose_name='Название')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, blank=True, null=True)
    national_cuisine = models.ForeignKey(NationalCuisine, verbose_name='Национальная кухня',
                                         on_delete=models.SET_NULL, blank=True, null=True)
    description = models.CharField(verbose_name='Описание', default='')
    cooking_time = models.IntegerField(verbose_name='Время приготовления', default=0)

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self) -> str:
        return str(self.name)
