from django.conf.urls import url
from project import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_toilet/$', views.add_toilet, name='add_toilet'),
    url(r'^sign_up/$', views.sign_up, name='sign_up'),
    url(r'^signIn/$', views.user_login, name='sign_in'),
    url(r'^signOut/$', views.user_logout, name='sign_out'),
    url(r'^bathrooms/(?P<b_slug>[\w\-]+)/rate/$', views.rate, name='rate'),
    url(r'^bathrooms/(?P<b_slug>[\w\-]+)/comment/$', views.comment, name='comment'),
    url(r'^bathrooms/(?P<b_slug>[\w\-]+)/$', views.show_toilet, name='show_toilet'),
]
