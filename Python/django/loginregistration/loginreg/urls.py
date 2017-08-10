from django.conf.urls import url
from . import views
from views import index, login, register, success, logout

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='login'),
    url(r'^login$', views.login, name='register'),
    url(r'^success$', views.success, name='success'),
    url(r'^logout$', views.logout, name='logout')
]
