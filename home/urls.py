from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="home"),
    url(r'^apps/(?P<app_name>\w+)$', views.open_app, name="home"),
    url(r'^desktop$', views.desktop, name="home"),
]
