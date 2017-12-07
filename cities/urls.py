from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.CityList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', views.CityDetail.as_view(), name='detail'),
    url(r'^new$', views.CityCreation.as_view(), name='new'),
    url(r'^edit/(?P<pk>\d+)$', views.CityUpdate.as_view(), name='edit'),
    url(r'^delete/(?P<pk>\d+)$', views.CityDelete.as_view(), name='delete'),

]