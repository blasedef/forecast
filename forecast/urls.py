from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^thirdparty/$', views.thirdparty, name='thirdparty'),
    url(r'^thirdparty/(?P<thirdparty_id>[0-9]+)$', views.thirdparty_edit, name='thirdparty_edit')
]