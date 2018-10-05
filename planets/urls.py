from django.conf.urls import url
from . import views

app_name = 'planets'

urlpatterns = [
    url(r'^$', views.planets_list, name='planets_list'),
    url(r'^(?P<name>[-\w]+)/$', views.planet_data, name='planet_data'),
    url(r'^(?P<name>[-\w]+)/$', views.planet_data, name='moon_data'),
]