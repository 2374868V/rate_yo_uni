from django.conf.urls import url
from rate_yo_uni_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
