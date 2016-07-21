# -*- coding: utf-8 -*-
"""Modul for Views of RMS."""

# Externe Module/Klassen

# Django Module/Klassen
from django.http import HttpResponseNotFound
from django.shortcuts import render, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.auth import login
from django.core.urlresolvers import reverse
from rms_app.models import Gericht


def uebersicht(request):
    """
    Zeigt eine Übersicht aller eingetragenen Rezepte/Gerichte.
    :param request:
    :return:
    """
    gericht = Gericht.objects.create(gericht_name="Spaghetti")
    gericht.save()
    gerichte = Gericht.objects.get(pk=1)
    return render(request, 'main.html', {'gerichte': gerichte})


def zeige_gericht(request, gericht_id):
    """
    Zeigt alle Informationen für ein spezielles Gericht an.
    :param request:
    :param gericht_id:
    :return:
    """
    gericht = Gericht.objects.get(pk=gericht_id)
    return render(request, 'gericht.html', {'gericht': gericht})
