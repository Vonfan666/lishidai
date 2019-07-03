#!/usr/bin/python3
# @File:.py
# -*- coding:utf-8 -*-
# @Author:von_fan
# @Time:2019年07月04日01时28分44秒

from django.shortcuts import render_to_response,HttpResponse
from  apps.lib.invalidSessionCode import InvalidSession
import  json

authUserLogin=InvalidSession("phone","pwd")

def  home(req):

    if authUserLogin.invalidLogin(req):
        return render_to_response("home.html")
    else:
        return render_to_response("login.html")


def backLogin(req):


    data={
        "msg":None,
        "status":None,
    }
    # phone=req.COOKIES.get("phone")
    del req.session["phone"]
    # print("1111111",authUserLogin.delSession())
    # del req.session[authUserLogin.delSession()]
    data["msg"]="操作成功"
    data["status"]=200
    return HttpResponse(json.dumps(data))




def  addProject(req):
    print(req.POST.get("data"))
    print()