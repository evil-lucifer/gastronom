from django.db import models
from base_model.models import BaseModel
from recipe.models import Recipe


class StageOfPreparation(BaseModel):
    step = models.IntegerField(verbose_name='Номер шага', default=0)
    recipe = models.ForeignKey(Recipe, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Рецепт')
    photo = models.CharField(verbose_name='Фото')
    description = models.CharField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Этап приготовления'
        verbose_name_plural = 'Этапы приготовления'
