#!/usr/bin/python3
# -*- coding:utf-8 -*-
#author=von-fan
from   django.shortcuts  import  redirect,render_to_response,render,HttpResponse
import  json
from  apps.lib import fromInvalid
from apps import models
from apps.lib.invalidSessionCode import InvalidSession


authUserLogin=InvalidSession("phone","pwd")

def  index(req):
    return render_to_response('login.html')

def  login(req):
    data={}
    print(req.method)
    if req.method=='GET':
        data['errorMassage'] = '请求类型错误'
        a = json.dumps(data)
        return render_to_response('login.html',locals())
    else:
        obj=fromInvalid.LoginInvalid(req.POST)
        isInvalid=obj.is_valid()
        if  isInvalid:
            obj=models.Login.objects.filter(phone=req.POST.get('phone')).values('pwd')
            if  obj:
                print(obj,obj[0])
                if req.POST.get('pwd')==obj[0]["pwd"]:

                    req.session["phone"] = req.POST.get('phone')
                    req.session["pwd"] = req.POST.get('pwd')
                    print("COOKIES----------------", req.COOKIES)
                    print("SESSION--------------", req.session)
                    print(req.session["pwd"])
                    print(req.session["phone"])

                    data={'msg':'登录成功','status':200,'errorMassage':'null'}

                else:
                    data['errorMassage']='您输入的密码有误！'
            else:
                data['errorMassage'] = '您输入的账号不存在！'
            a = json.dumps(data)
            a=HttpResponse(a)
            a.set_cookie("phone", req.POST.get('phone'))
            a.set_cookie("pwd", req.POST.get('pwd'))

            return a

        else:
            for  a  in  obj.errors:
                try:
                    data['errorMassage']=obj.errors[a][0]
                except:
                    pass
            a=json.dumps(data)
            return HttpResponse(a)

def  home(req):

    if authUserLogin.invalidLogin(req):
        return render_to_response("home.html")
    else:
        return render_to_response("login.html")