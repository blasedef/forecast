from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^third_party/list/$', views.thirdPartyList, name='thirdPartyList'),
    url(r'^third_party/new/$', views.thirdPartyNew, name='thirdPartyEdit'),
    url(r'^third_party/(?P<thirdParty_id>[0-9]+)$', views.thirdPartyEdit, name='thirdPartyEdit')
]