from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^(?P<owner_id>\d+)/poke$', views.poke, name = 'poke'),
    url(r'^(?P<id>\d+)/show$', views.show, name = 'show')
]
