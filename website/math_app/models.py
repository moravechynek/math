from pickle import FALSE
from django.db import models

class Priklad(models.Model):
    priklad = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Příklad"
        verbose_name_plural = "Příklady"

class Reseni(models.Model):
    reseni = models.CharField(max_length=200)
    FK_priklad = models.ForeignKey(
        'Priklad',
        on_delete=models.CASCADE,
        blank=False,
        null=False)

    class Meta:
        verbose_name = "Řešení"
        verbose_name_plural = "Řešení"