from django.conf.urls import url
from home import views

urlpatterns = [
    url(r'^$', views.index, name="home"),
    url(r'^desktop$', views.show_desktop, name="home"),
    url(r'^apps/open/(?P<app_id>\w+)$', views.open_app, name="home"),
    url(r'^apps/close/(?P<app_id>\w+)$', views.close_app, name="home"),
    url(r'^apps/get/memory/(?P<app_id>\w+)$', views.get_memory_app, name="home"),
    url(r'^apps/all$', views.get_all_open_apps, name="home"),
    url(r'^reports/processes/add/(?P<app_id>\w+)$', views.add_process, name="home"),
    url(r'^reports/processes/close/(?P<app_id>\w+)$', views.remove_process, name="home"),
    url(r'^reports/processes/status/(?P<app_id>\w+)$', views.change_process_state, name="home"),
    url(r'^reports/resources$', views.resources, name="home"),
    url(r'^reports/resources/memory', views.get_memory_available, name="home"),
    url(r'^reports/memory-table/show', views.show_memory_table, name="home"),
    url(r'^reports/memory-table/add/(?P<app_id>\w+)', views.add_to_memory_table, name="home"),
    url(r'^reports/memory-table/remove/(?P<app_id>\w+)', views.remove_from_memory_table, name="home"),
    url(r'^reports/memory-table/compact', views.compact_memory_table, name="home"),
]
