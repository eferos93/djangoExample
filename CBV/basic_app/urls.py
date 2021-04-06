from django.conf.urls import url
from django.urls import path
from basic_app import views

app_name = 'basic_app'  # used in templates like {% url basic_app:list %}

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
    # the regex gets the key of the school
    url(r'^(?P<pk>\d+)/$', views.SchoolDetailView.as_view(), name='detail'),
    path('create/', views.SchoolCreateView.as_view(), name='create'),
    url(r'^delete/(?P<pk>\d+)/$', views.SchoolDeleteView.as_view(), name='delete'),
    url(r'^update/(?P<pk>\d+)/$', views.SchoolUpdateView.as_view(), name='update'),
]