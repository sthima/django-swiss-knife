from django.views.generic.base import ContextMixin
from django.template import RequestContext, Template


class Breadcrumb(object):

    def __init__(self, request, *nodes):
        self.nodes = nodes
        self.request = request

    def __call__(self):
        template = Template("""
            {% load django_bootstrap_breadcrumbs %}
            {% block breadcrumbs %}
                {% clear_breadcrumbs %}
                {% for node in nodes %}
                    {% breadcrumb node.label node.url %}
                {% endfor %}
            {% endblock %}
            {% render_breadcrumbs %}
        """)
        context = RequestContext(self.request, {'nodes': self.nodes})
        return template.render(context)


class BreadcrumbNode(object):

    def __init__(self, label, url, *args, **kwargs):
        self.label = label
        self.url = url
        self.args = args
        self.kwargs = kwargs


class BreadcrumbsMixin(ContextMixin):
    breadcrumbs = []

    def get_breadcrumbs(self, **kwargs):
        return self.breadcrumbs

    def get_context_data(self, **kwargs):
        context = super(BreadcrumbsMixin, self).get_context_data(**kwargs)
        context['breadcrumbs'] = Breadcrumb(self.request, *self.get_breadcrumbs(**kwargs))

        return context
