# -*- coding: utf-8 -*-
"""Modul for Forms of RMS."""
from django import forms
from django.forms import ModelForm
from bootstrap_markdown.widgets import MarkdownEditor
from rms_app.models import Kategorie, Gericht


class GerichtsFormular(ModelForm):
    gericht_name = forms.CharField(max_length=300, required=True, widget=forms.TextInput(
        attrs={"type": "text", "class": "form-control", 'autofocus': 'autofocus'}))
    beschreibung = forms.CharField(max_length=3000, required=True, widget=MarkdownEditor(
                                            attrs={'id': 'Beschreibung',
                                                   'hiddenButtons': "Preview",
                                                   'fullscreen': True}))

    class Meta:
        model = Gericht
        fields = ('beschreibung', 'gericht_name')


