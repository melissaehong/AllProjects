from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
]
