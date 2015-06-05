from django.conf.urls import patterns, url, include
from django.contrib import admin
from food import views

admin.autodiscover()

urlpatterns = patterns('',
  url(r'^foodtrucks/$', views.get_foodtrucks, name='get_truck_list'),
  )

