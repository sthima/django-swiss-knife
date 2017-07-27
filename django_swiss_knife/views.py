from django.contrib import messages
from django.views.generic.base import RedirectView
from django.views.generic.detail import SingleObjectMixin


class ActionView(SingleObjectMixin, RedirectView):
    """
    A view that executes an action and then redirects the page.
    """
    url = None

    success_message = None
    success_url = None

    error_message = None
    error_url = None

    def get_redirect_url(self, *args, **kwargs):
        success_url = self.get_success_url(*args, **kwargs)
        error_url = self.get_error_url(*args, **kwargs)
        if self.action_result and success_url:
            self.url = success_url
        elif (not self.action_result) and error_url:
            self.url = error_url
        else:
            self.url = self.get_url(*args, **kwargs)
        return super().get_redirect_url(*args, **kwargs)

    def get_url(self, *args, **kwargs):
        return self.url

    def get_success_message(self, *args, **kwargs):
        return self.success_message

    def get_success_url(self, *args, **kwargs):
        return self.success_url

    def get_error_message(self, *args, **kwargs):
        return self.error_message

    def get_error_url(self, *args, **kwargs):
        return self.error_url

    def action(self, *args, **kwargs):
        return True

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.action_result = self.action(*args, **kwargs)
        if self.action_result:
            success_message = self.get_success_message(*args, **kwargs)
            if success_message:
                messages.success(self.request, self.success_message)
        else:
            error_message = self.get_error_message(*args, **kwargs)
            if error_message:
                messages.error(self.request, self.error_message)
        return super().get(request, *args, **kwargs)

