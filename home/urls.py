from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="home"),
    url(r'^apps/chrome$', views.chrome_app, name="home"),
    url(r'^desktop$', views.desktop, name="home"),
]
