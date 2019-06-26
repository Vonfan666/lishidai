from  django.forms import  fields
from  django import forms


class  LoginInvalid(forms.Form):
    phone=fields.CharField(required=True,max_length=11,min_length=11,
                              error_messages={
                                  'invalid':'格式输入错误',
                                  'required':'账号不能为空',
                                  'max_length':'请输入11位手机号码',
                                  'min_length': '请输入11位手机号码',
                              })
    pwd=fields.CharField(
        required=True,max_length=18,min_length=6,strip=True,
        error_messages={
                                  'invalid':'格式输入错误',
                                  'required':'密码不能为空',
                                  'max_length':'请输入小于十八位的密码',
                                  'min_length': '请输入大于六位的密码',

        }
    )


