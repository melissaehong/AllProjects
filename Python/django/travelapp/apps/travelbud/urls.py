from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^destination/(?P<trip_id>\d+)$', views.show, name = 'show'),
    url(r'^add$', views.add, name='add'),
    url(r'^create$', views.create, name = 'create'),
    url(r'^show$', views.show, name = 'show'),
    url(r'^(?P<user_id>\d+)/join$', views.join, name = 'join'),
]
