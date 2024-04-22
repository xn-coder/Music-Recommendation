"""
URL configuration for music project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import home, explore, login, register, faqs, recommend_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('explore/', explore, name='explore'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('faqs/', faqs, name='faqs'),
    path('recommend/', recommend_view, name='recommend'),
]
