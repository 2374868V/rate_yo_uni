"""rate_yo_uni URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from project import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^project/', include('project.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^sign_up/', views.sign_up, name='sign_up'),
    url(r'^add_toilet/', views.sign_up, name='add_toilet'),
    url(r'^show_toilet/', views.sign_up, name='show_toilet')

]
