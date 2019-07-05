#!/usr/bin/python3
# -*- coding:utf-8 -*-
#author=von-fan
from django.db import models
from django.utils import timezone

# Create your models here.


class Login(models.Model):
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
    vbname=models.CharField(max_length=255,verbose_name="环境名称")
    vbkey=models.CharField(max_length=255,verbose_name="环境变量")
    vbaddr= models.CharField(max_length=255,verbose_name="环境地址")
    vbpop = models.CharField(max_length=255, verbose_name="创建人")
    createtime=models.DateTimeField(default=timezone.now,verbose_name="创建时间")  #创建时间为当前时间
    updatetime = models.DateTimeField(default=None,verbose_name="最后一次更新时间")  # 最后一次更新时间


    class Meta():
        db_table='lsdvarible'
        verbose_name_plural="环境"


    def __str__(self):
        return  self.vbname


class lsdproject(models.Model):

    proname=models.CharField(max_length=255,verbose_name="项目名称")  #版本
    proversion=models.CharField(max_length=255,verbose_name="测试版本") #测试版本
    runname=models.CharField(max_length=255,blank=True,verbose_name="创建人",default=None)
    updatetime=models.DateTimeField(default=timezone.now,verbose_name="最后一次执行时间")   #执行时间
    proexecutevalid=models.IntegerField(default=1,verbose_name="执行权限")  #执行权限  1=True
    proviewvalid=models.IntegerField(default=1,verbose_name="查看权限") #查看权限

    proVarOneMany = models.ManyToManyField("lsdvarible")  # 测试环境
    proVarMayMany = models.ForeignKey("Login", on_delete=models.CASCADE)  # 执行人
    class Meta():
        db_table='lsdproject'
        verbose_name_plural="项目"

    def __str__(self):
        return  self.proname

