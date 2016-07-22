"""Modul for Admin of Thesis-Exposee."""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.db.models import Q
from rms_app.models import Gericht


class GerichtAdmin(admin.ModelAdmin):
        list_display = ('gericht_name', 'beschreibung')


admin.site.register(Gericht, GerichtAdmin)
