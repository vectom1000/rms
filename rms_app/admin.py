"""Modul for Admin of Thesis-Exposee."""
from django.contrib import admin
from rms_app.models import Gericht


class GerichtAdmin(admin.ModelAdmin):
        list_display = ('gericht_name', 'beschreibung')

admin.site.register(Gericht, GerichtAdmin)
