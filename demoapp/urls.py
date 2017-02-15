# django
from django.conf.urls import url
from demoapp.views import HomeView
from django.views.i18n import JavaScriptCatalog


urlpatterns = [
    url(r'^$', HomeView.as_view(), name="index"),
    url(r'^jsi18n/$', JavaScriptCatalog.as_view(), name='javascript-catalog'),
]
