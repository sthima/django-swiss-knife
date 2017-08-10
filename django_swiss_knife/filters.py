from functools import reduce
import operator

from django.db.models import Q
import django_filters

from .fields import SearchField


class MultipleFieldsFilter(django_filters.CharFilter):
    field_class = SearchField

    def __init__(self, *args, **kwargs):
        if 'search_fields' not in kwargs:
            raise ValueError("MultipleFieldsFilter must recieve a 'search_fields' parameter")
        self.search_fields = kwargs.pop('search_fields')
        super(MultipleFieldsFilter, self).__init__(*args, **kwargs)

    def filter(self, queryset, value):
        """
            Método que realiza o filtro em diversos campos declarados no
            atributo search_fields.
        """
        query_list = [
            Q((_search_field + _lookup_type, value)) for _search_field, _lookup_type in self.search_fields.items()
        ]
        return queryset.filter(
            reduce(operator.or_, query_list)
        )
