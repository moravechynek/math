from django.db import models

class Priklad(models.Model):
    priklad = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Příklad"
        verbose_name_plural = "Příklady"