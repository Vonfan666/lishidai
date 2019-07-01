#!/usr/bin/python3
# -*- coding:utf-8 -*-
#author=von-fan
from django.contrib import admin

# Register your models here.

from django.contrib import  admin
from  apps import  models


admin.site.register(models.Login)
