from django.db import models
from bootstrap3_datetime.widgets import DateTimePicker
from . import fields


class ViewModelMeta:
    default_permissions = ('add', 'change', 'delete', 'view')


class NotRemovedObject(models.Manager):
    """ Model manager to list only objects not removed (is_removed = False).
        Used along with RemovedModel Class.
    """
    def get_queryset(self):
        return super(NotRemovedObject, self).get_queryset().filter(is_removed=False)


class RemovedModelMixin(models.Model):
    """ Boolean field indicating whether an instance of this class is removed or not
    """
    is_removed = models.BooleanField(null=False, blank=True, default=False, verbose_name="Inativo")
    objects = NotRemovedObject()
    full_objects = models.Manager()

    def delete(self, *args, **kwargs):
        if not self.is_removed:
            self.is_removed = True
            self.save()
        return

    class Meta:
        abstract = True


class MoneyField(models.DecimalField):
    def formfield(self, **kwargs):
        defaults = {}
        defaults['max_digits'] = 12
        defaults['decimal_places'] = 2
        defaults['localize'] = True
        defaults['form_class'] = fields.MoneyField
        defaults.update(kwargs)
        return super().formfield(**defaults)


class DateTimeField(models.DateTimeField):
    def formfield(self, **kwargs):
        defaults = {}
        defaults['widget'] = DateTimePicker(
            options={
                "format": "DD/MM/YYYY HH:mm",
                "icons": {
                    "date": 'fa fa-calendar',
                    "time": 'fa fa-clock-o',
                    "up": 'fa fa-chevron-up',
                    "down": 'fa fa-chevron-down',
                }
            },
            icon_attrs={
                'class': 'fa fa-calendar'
            },
        )
        defaults.update(kwargs)
        return super().formfield(**defaults)


class DateField(models.DateField):
    def formfield(self, **kwargs):
        defaults = {}
        defaults['widget'] = DateTimePicker(
            options={
                "format": "DD/MM/YYYY",
                "pickTime": False,
                "icons": {
                    "date": 'fa fa-calendar',
                    "time": 'fa fa-clock-o',
                    "up": 'fa fa-chevron-up',
                    "down": 'fa fa-chevron-down',
                }
            },
            icon_attrs={
                'class': 'fa fa-calendar'
            },
        )
        defaults.update(kwargs)
        return super().formfield(**defaults)
