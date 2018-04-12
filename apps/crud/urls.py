from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # New user form submission
    url(r'^add_user$', views.addUser),
    url(r'^users/create$', views.create, name='my_new'),

    url(r'^users/(?P<id>\d+)$', views.show, name='display'),

    url(r'^edit/(?P<id>\d+)$', views.update),
    url(r'^users/edit/(?P<id>\d+)$', views.edit, name='edit'),

    url(r'^users/(?P<id>\d+)/destroy$', views.delete, name='destroy')
]
