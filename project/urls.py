from django.conf.urls import url
from project import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
