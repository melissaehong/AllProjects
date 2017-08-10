from django.conf.urls import url
from views import users, users_w_id, new, edit, destroy

urlpatterns = [
    url(r'^products/$', users),
    url(r'^products/new$', new),
    url(r'^products/(?P<id>\d+)/$', users_w_id),
    url(r'^products/(?P<id>\d+)/edit/$', edit),
    url(r'^products/(?P<id>\d+)/destroy/$', destroy)
]
