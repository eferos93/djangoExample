from django.conf.urls import url
from djangoBasics.second_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^help/', views.help_http, name='help')
]