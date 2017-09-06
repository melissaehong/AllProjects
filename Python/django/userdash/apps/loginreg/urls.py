from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^signin$', views.signin),
    url(r'^register_user$', views.register_user),
    url(r'^signin_user$', views.signin_user),
    url(r'^dashboard$', views.dashboard),
    url(r'^logout$', views.logout),
]
