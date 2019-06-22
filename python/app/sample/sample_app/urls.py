from django.conf.urls import url
from sample_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^members/$', views.members, name='members'),
]