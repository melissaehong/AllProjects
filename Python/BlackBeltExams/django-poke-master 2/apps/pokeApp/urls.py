from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^main$', views.main, name='main'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^pokes$', views.pokes, name='pokes'),
    url(r'^action$', views.action, name='action'),
]
