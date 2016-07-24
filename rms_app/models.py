"""Modul for Models of Thesis-Exposee."""
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Gericht(models.Model):
    gericht_name = models.CharField(max_length=100, blank=False)
    beschreibung = models.CharField(max_length=20000, blank=True)
    kategorie = models.ForeignKey('Kategorie', on_delete=models.PROTECT,
                                  null=True, related_name='+', blank=True)

    def __str__(self):
        return self.gericht_name

    class Meta:
        verbose_name = 'Gericht'
        verbose_name_plural = 'Gerichte'


class Kategorie(models.Model):
    kategorie_name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.kategorie_name

    class Meta:
        verbose_name = 'Kategorie'
        verbose_name_plural = 'Kategorien'


