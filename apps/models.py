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
        verbose_name_plural="用户信息"

    def __str__(self):
        return self.phone


class lsdvarible(models.Model):
    id=models.IntegerField(primary_key=True,unique=True)
    vbname=models.CharField(max_length=11,verbose_name="环境名称")
    vbkey=models.CharField(max_length=11,verbose_name="环境变量")
    vbaddr= models.CharField(max_length=255,verbose_name="环境地址")
    vbkey = models.CharField(max_length=11, verbose_name="创建人")
    createtime=models.DateTimeField(default=timezone.now,verbose_name="创建时间")  #创建时间为当前时间
    updatetime = models.DateTimeField(default=None,verbose_name="最后一次更新时间")  # 最后一次更新时间


    class Meta():
        db_table='varible'
        verbose_name_plural="环境"


    def __str__(self):
        return  self.vbname


class lsdproject(models.Model):
    id=models.IntegerField(primary_key=True,unique=True)  #名称
    proname=models.CharField(max_length=11,verbose_name="项目名称")  #版本
    proversion=models.CharField(max_length=11,verbose_name="测试版本") #测试版本
    provarible=models.ManyToManyField("lsdvarible",verbose_name="测试环境")  #测试环境
    username=models.ForeignKey("Login",on_delete=models.CASCADE,verbose_name="执行人")  #执行人
    updatetime=models.DateTimeField(default=timezone.now,verbose_name="最后一次执行时间")   #执行时间
    proexecutevalid=models.IntegerField(default=1,verbose_name="执行权限")  #执行权限  1=True
    proviewvalid=models.IntegerField(default=1,verbose_name="查看权限") #查看权限
    class Meta():
        db_table='lsdproject'
        verbose_name_plural="项目"

    def __str__(self):
        return  self.proname

