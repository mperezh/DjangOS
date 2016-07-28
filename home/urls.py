from django.conf.urls import url
from home import views

urlpatterns = [
    url(r'^$', views.index, name="home"),
    url(r'^apps/open/(?P<app_id>\w+)$', views.open_app, name="home"),
    url(r'^apps/close/(?P<app_id>\w+)$', views.close_app, name="home"),
    url(r'^desktop$', views.show_desktop, name="home"),
]
