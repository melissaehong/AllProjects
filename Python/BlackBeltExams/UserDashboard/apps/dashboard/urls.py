from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<id>\d+)/add$', views.add),
    url(r'^create$', views.create),
    url(r'^(?P<id>\d+)/profile$', views.profile),
    url(r'^(?P<id>\d+)/show$', views.show, name='show'),
    url(r'^(?P<id>\d+)/edit$', views.edit),
    url(r'^(?P<id>\d+)/edit_user$', views.edit_user),
    url(r'^(?P<id>\d+)/update$', views.update),
    url(r'^(?P<id>\d+)/remove$', views.delete),
    url(r'^(?P<owner_id>\d+)/message$', views.message, name='message'),
    url(r'^(?P<owner_id>\d+)*/(?P<message_id>\d+)/comment$', views.comment, name='comment')
]
