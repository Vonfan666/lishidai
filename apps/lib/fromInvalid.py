#!/usr/bin/python3
# -*- coding:utf-8 -*-
#author=von-fan
from  django.forms import  fields
from  django import forms
from  django.core.validators import  RegexValidator


class  LoginInvalid(forms.Form):
    phone=fields.CharField(required=True,max_length=18,min_length=4,
                              error_messages={
                                  'invalid':'格式输入错误',
                                  'required':'账号不能为空',
                                  'max_length':'账号最多数据十八位',
                                  'min_length': '账号最少输入四位',
                              })
    pwd=fields.CharField(
        required=True,max_length=18,min_length=6,strip=True,
        error_messages={
                                  # 'invalid':'格式输入错误',
                                  'required':'密码不能为空',
                                  'max_length':'请输入小于十八位的密码',
                                  'min_length': '请输入大于六位的密码',

        },
        # validators=[RegexValidator(r'^[0-9]+$','请输入数字')],
    )


