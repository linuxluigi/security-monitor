try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

from . import views

urlpatterns = [
    url(r'^$', views.index, name='dashboard_index'),
    url(r'^(?P<website_id>[0-9]+)/$', views.url_status, name='dashboard_url_status'),
    url(r'^(?P<website_id>[0-9]+)/(?P<scan_id>[0-9]+)/$', views.url_scan_status, name='dashboard_url_foundings'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^login/$', views.login_view, name='login'),
]
