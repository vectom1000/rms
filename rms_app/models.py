"""Modul for Models of Thesis-Exposee."""
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Gericht(models.Model):
    gericht_name = models.CharField(max_length=100)
    beschreibung = models.CharField(max_length=20000)

    def __str__(self):
        return self.gericht_name
