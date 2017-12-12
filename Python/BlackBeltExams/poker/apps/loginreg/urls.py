from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^about$', views.about),
    url(r'^contact$', views.contact),
    url(r'^signin$', views.signin),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
]
