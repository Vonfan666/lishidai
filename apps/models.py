#!/usr/bin/python3
# -*- coding:utf-8 -*-
#author=von-fan
from django.db import models
from django.utils import timezone

# Create your models here.


class Login(models.Model):

    id=models.IntegerField(primary_key=True,unique=True)
    phone=models.CharField(max_length=11)
    pwd=models.CharField(max_length=18)
    createtime=models.DateTimeField(auto_now_add=True)   #创建时间 后续无法orm程序修改
    updatetime=models.DateTimeField(auto_now_add=True)
    class Meta():
        db_table='login'

    def __str__(self):
        return self.phone


class lsdvarible(models.Model):
    id=models.IntegerField(primary_key=True,unique=True)
    vbname=models.CharField(max_length=11)
    vbkey=models.CharField(max_length=11)
    vbaddr= models.CharField(max_length=255)
    createtime=models.DateTimeField(default=timezone.now)  #创建时间为当前时间
    updatetime = models.DateTimeField(default=None)  # 最后一次更新时间


    class Meta():
        db_table='varible'

    def __str__(self):
        return  self.vbname


class lsdproject(models.Model):
    id=models.IntegerField(primary_key=True,unique=True)  #名称
    proname=models.CharField(max_length=11,verbose_name="项目名称")  #版本
    proversion=models.CharField(max_length=11,verbose_name="测试版本") #测试版本
    provarible=models.ManyToManyField("lsdvarible")  #测试环境
    username=models.ForeignKey("Login",on_delete=models.CASCADE)  #执行人
    updatetime=models.DateTimeField(default=timezone.now)   #执行时间
    proexecutevalid=models.IntegerField(default=1)  #执行权限  1=True
    proviewvalid=models.IntegerField(default=1) #查看权限
    class Meta():
        db_table='lsdproject'

    def __str__(self):
        return  self.proname

