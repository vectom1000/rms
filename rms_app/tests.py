"""Modul for Tests of Thesis-Exposee."""

# Create your tests here.

from django.core.urlresolvers import reverse
from django.test import TestCase


class BasicHtmlTests(TestCase):
    """Needed HTML properties."""

    def test_doctype(self):
        """Title page must have a DOCTYPE declaration."""
        response = self.client.get(reverse('index'))
        self.assertRegex(response.content, '^<!DOCTYPE html>')

    def test_utf8(self):
        """Title page must contain a charset declaration for UTF8."""
        response = self.client.get(reverse('index'))
        self.assertContains(response, '<meta charset="utf-8">')

    def test_viewpoint(self):
        """Title page must contain a viewport declaration."""
        response = self.client.get(reverse('index'))
        self.assertContains(response, '<meta name="viewport" content="')
