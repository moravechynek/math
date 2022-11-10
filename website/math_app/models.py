from django.db import models
import os

def get_image_ucebnice(instance, filename):
    return os.path.join('math_app/static/img/', filename)

class Ucebnice(models.Model):
    nazev = models.CharField(max_length=200)
    obrazek = models.ImageField(upload_to=get_image_ucebnice,default=None)
    def __str__(self):
        return self.nazev
    class Meta:
        verbose_name = "Učebnice"
        verbose_name_plural = "Učebnice"

class Kapitola(models.Model):
    nazev = models.CharField(max_length=200)
    FK_ucebnice = models.ForeignKey(
        'Ucebnice',
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        default=None)
    def __str__(self):
        return self.nazev
    class Meta:
        verbose_name = "Kapitola"
        verbose_name_plural = "Kapitoly"

class Cviceni(models.Model):
    text = models.CharField(max_length=200)
    FK_kapitola = models.ForeignKey(
        'Kapitola',
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        default=None)
    def __str__(self):
        return self.text
    class Meta:
        verbose_name = "Cvičení"
        verbose_name_plural = "Cvičení"

class Priklad(models.Model):
    priklad = models.CharField(max_length=200)
    FK_cviceni = models.ForeignKey(
        'Cviceni',
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        default=None)
    def __str__(self):
        return self.priklad
    class Meta:
        verbose_name = "Příklad"
        verbose_name_plural = "Příklady"

class Reseni(models.Model):
    reseni = models.CharField(max_length=200)
    FK_priklad = models.ForeignKey(
        'Priklad',
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        default=None)
    je_spravne = models.BooleanField(default=None)
    #timestamp
    def __str__(self):
            return self.reseni
    class Meta:
        verbose_name = "Řešení"
        verbose_name_plural = "Řešení"