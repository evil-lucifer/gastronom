from django.db import models
from base_model.models import BaseModel


class NationalCuisine(BaseModel):
    name = models.CharField(verbose_name='Название')

    class Meta:
        verbose_name = 'Национальная кухня'
        verbose_name_plural = 'Национальные кухни'

    def __str__(self) -> str:
        return str(self.name)
