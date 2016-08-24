from django.conf.urls import url
from home import views

urlpatterns = [
    url(r'^$', views.index, name="home"),
    url(r'^desktop$', views.show_desktop, name="home"),
    url(r'^apps/open/(?P<app_id>\w+)$', views.open_app, name="home"),
    url(r'^apps/close/(?P<app_id>\w+)$', views.close_app, name="home"),
    url(r'^reports/processes/add/(?P<app_id>\w+)$', views.add_process, name="home"),
    url(r'^reports/processes/close/(?P<app_id>\w+)$', views.remove_process, name="home"),

]
