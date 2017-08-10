from django import forms

from . import widgets


class SearchField(forms.CharField):
    widget = widgets.SearchInput
