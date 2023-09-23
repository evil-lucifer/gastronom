from django.db import models

from base_model.models import BaseModel


class Unit(BaseModel):
    name = models.CharField(verbose_name='Название', unique=True)

    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'

    def __str__(self) -> str:
        return str(self.name)
