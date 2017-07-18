from django.forms.widgets import flatatt
from django.utils.safestring import mark_safe


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
