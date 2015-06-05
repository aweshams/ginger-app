"""ginger_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns,include, url
from django.contrib import admin
from food import views

urlpatterns = [
	url(r'^foodtrucks/$', views.get_foodtrucks, name='get_truck_list'),
	url(r'^events/$', views.get_events , name='get_events_list'),
	url(r'^(?P<event_location>\d+)/$',views.get_event_vendors, name='get_event_vendors'),
	url(r'^(?P<vendor_id>\d+)/vendor/$',views.get_vendor_name, name='get_vendor_name'),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^home/$', views.index),
]
