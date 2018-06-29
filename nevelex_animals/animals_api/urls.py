from django.conf.urls import url
from animals_api import views

urlpatterns = [
    url(r'^Animal/$', views.animal_list),
    url(r'^Animal/(?P<pk>[0-9]+)/$', views.animal_detail),
]