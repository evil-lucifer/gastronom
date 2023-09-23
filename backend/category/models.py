from base_model.models import BaseModel
from django.db import models


class Category(BaseModel):
    name = models.CharField(verbose_name='Название')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return str(self.name)
