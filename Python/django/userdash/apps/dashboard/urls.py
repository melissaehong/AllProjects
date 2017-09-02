from django.conf.urls import url

urlpatterns = [
    url(r'^dashboard$', views.index)
    url(r'^dashboard/admin$', views.admin),
    url(r'^/users/new', views.add),
    url(r'^/users/show/(?P=<user_id>)\d+)$', views.show),
    url(r'^/users/edit$'), views.edit)
]
