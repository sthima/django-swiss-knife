from django import forms

from . import widgets


class SearchField(forms.CharField):
    widget = widgets.SearchInput


class MoneyField(forms.DecimalField):
    widget = widgets.MoneyInput

    def widget_attrs(self, widget):
        attrs = super().widget_attrs(widget)
        attrs['data-money-field'] = True
        # TODO (mmarchini) customizable currency
        attrs['data-currency'] = "R$"
        return attrs
