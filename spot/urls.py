from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^spot/(?P<id>\d+)$', views.spot, name='spot'),
]