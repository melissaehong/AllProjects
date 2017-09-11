from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^(?P<poker_id>\d+)*/(?P<pokee_id>\d+)/poke$', views.poke, name = 'poke'),
]
