from django.forms.utils import flatatt
from django.utils.safestring import mark_safe
from django.template import loader


class AbstractButton(object):

    def __init__(self, url, label, attrs={}):
        self.url = url
        self.label = label
        self.attrs = attrs

    def __call__(self):
        return self.render()

    def render(self, *args, **kwargs):
        raise NotImplemented("You need to overwrite this method")


class Button(AbstractButton):
    def __init__(self, label, attrs={}):
        self.label = label
        self.attrs = attrs

    def render(self, *args, **kwargs):
        return mark_safe("<button %s>%s</button>" % (flatatt(self.attrs), self.label,))


class Anchor(AbstractButton):

    def __init__(self, url, label, attrs={}):
        self.url = url
        self.label = label
        self.attrs = attrs

    def render(self, *args, **kwargs):
        return mark_safe("<a href='%s' %s>%s</a>" % (self.url, flatatt(self.attrs), self.label))


class MultiActionsButton(AbstractButton):
    ''' A dropdown button that display a all buttons passed on actions
    '''
    template_name = "django_swiss_knife/bootstrap/multi-actions-dropdown-button.html"
    def __init__(self, label, actions=[]):
        self.label = label
        self.actions = actions

    def get_context_data(self, *args, **kwargs):
        context = {
            'label': self.label,
            'actions': self.actions
        }
        return context

    def render(self, *args, **kwargs):
        template = loader.get_template(self.template_name)
        context = self.get_context_data(*args, **kwargs)
        return template.render(context)


class SplitButtonsDropdown(AbstractButton):
    ''' A button splitted into action and dropdown
    '''
    template_name = "django_swiss_knife/bootstrap/split-button-dropdown.html"
    def __init__(self, main_action, actions=[]):
        self.main_action = main_action
        self.actions = actions

    def get_context_data(self, *args, **kwargs):
        context = {
            'main_action': self.main_action,
            'actions': self.actions
        }
        return context

    def render(self, *args, **kwargs):
        template = loader.get_template(self.template_name)
        context = self.get_context_data(*args, **kwargs)
        return template.render(context)
