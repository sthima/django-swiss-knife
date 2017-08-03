from django import forms
from django.template import Context, loader


class TemplateWidgetMixin(object):

    def get_context_data(self, name, value, attrs={}):
        return {
            'name': name,
            'attrs': attrs,
        }

    def render(self, name, value, attrs={}):
        template = loader.get_template(self.template_name)
        attrs = self.build_attrs(attrs)
        context = self.get_context_data(name, value, attrs)
        return template.render(context)


class DropdownCheckboxSelectMultipleWidget(TemplateWidgetMixin, forms.CheckboxSelectMultiple):
    ''' Basic checkbox select multiple in a dropdown.
    '''
    template_name = 'django_swiss_knife/bootstrap/dropdown-checkbox-select-multiple.html'

    def __init__(self, *args, label='', **kwargs):
        super().__init__(*args, **kwargs)
        self.label = label

    def get_context_data(self, name, value, attrs={}):
        context = super().get_context_data(name, value, attrs)

        value = value or []

        choices = []
        for choice_key, choice_label in self.choices:
            choice_checked = choice_key in value
            choices.append((choice_key, choice_label, choice_checked))

        context.update({
            'choices': choices,
            'label': self.label,
        })
        return context