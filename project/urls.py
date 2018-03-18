from django.conf.urls import url
from project import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_toilet/$', views.add_toilet, name='add_toilet'),
    url(r'^sign_up/', views.sign_up, name='sign_up'),
    url(r'^show_toilet/', views.show_toilet, name='show_toilet')
]
