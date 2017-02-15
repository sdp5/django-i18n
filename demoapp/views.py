from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.translation import ugettext_lazy as _

APP_DESC = _("Doing an awesome project. (str from views)")


class HomeView(TemplateView):
    """
    django-18n home view
    """
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        """
        Build the Context Data
        """
        context_data = super(TemplateView, self).get_context_data(**kwargs)
        context_data['description'] = APP_DESC
        return context_data
