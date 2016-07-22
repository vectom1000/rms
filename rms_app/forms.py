# -*- coding: utf-8 -*-
"""Modul for Forms of RMS."""
from django import forms
from django.forms import ModelForm
from bootstrap_markdown.widgets import MarkdownEditor
from rms_app.models import Kategorie, Gericht


class GerichtsFormular(ModelForm):
    gericht_name = forms.CharField(max_length=1500, required=True, widget=MarkdownEditor(
                                            attrs={'id': 'Name',
                                                   'boostrap_cdn': False,
                                                   'hiddenButtons': "Preview"}))


