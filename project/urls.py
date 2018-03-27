from django.conf.urls import url
from project import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_toilet/$', views.add_toilet, name='add_toilet'),
    url(r'^sign_up/', views.sign_up, name='sign_up'),
    url(r'^show_toilet/(?P<b_slug>[\w\-]+)/$', views.show_toilet, name='show_toilet'),
    url(r'^signIn/$', views.user_login, name='sign_in'),
    url(r'^signOut/', views.user_logout, name='sign_out')
]
