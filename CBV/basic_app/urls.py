from django.conf.urls import url
from django.urls import path
from basic_app import views

app_name = 'basic_app'  # used in templates like {% url basic_app:list %}

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
    # the regex gets the key of the school
    url(r'^(?P<pk>[-\w]+)/$', views.SchoolDetailView.as_view(), name='detail')
]