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


def hello(request):
    gericht = Gericht.objects.create(gericht_name="Spaghetti")
    gericht.save()
    print gericht.gericht_name
    return render(request, 'layout.html')