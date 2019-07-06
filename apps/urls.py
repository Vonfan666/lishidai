#!/usr/bin/python3
# -*- coding:utf-8 -*-
#author=von-fan
"""lishidai URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path,include
from  django.conf.urls import url
from  apps.views import login,home
urlpatterns = [
    url(r'index/',login.index,name='index'),
    url(r'login/',login.login,name='login'),
    url(r'home/',home.home,name='home'),
    url(r'backLogin/',home.backLogin,name='backLogin'),
    url(r'addLsdvarible/', home.addLsdvarible, name='addLsdvarible'),
    url(r'lsdvarible/', home.lsdvarible, name='lsdvarible'),


]
