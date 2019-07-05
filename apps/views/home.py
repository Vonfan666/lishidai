#!/usr/bin/python3
# @File:.py
# -*- coding:utf-8 -*-
# @Author:von_fan
# @Time:2019年07月04日01时28分44秒

from django.shortcuts import render_to_response,HttpResponse,redirect
from  apps.lib.invalidSessionCode import InvalidSession
from apps.lib import longmethod
from  apps import models
import  json,datetime
from django.forms.models import model_to_dict

selectValid=InvalidSession("phone","pwd")
updateValid=InvalidSession("phone","pwd")
longMtd=longmethod.Method()


@selectValid.cookiesVerify("home.html")
def  home(req):

    return  req



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
    data={}

    # print("----------------",req)
    # print(req.POST)
    #
    # print(model_to_dict(req.POST))
    if updateValid.cookiesInspect(req):
        print(req.POST)
        proName=req.POST.get("proName")
        prokey=req.POST.get("prokey")
        proattr=req.POST.get("proattr")
        vbpop=req.session["phone"]
        createtime=datetime.datetime.now()
        print(createtime,type(createtime))

        print("++++++",proName,prokey,proattr,vbpop,createtime,)
        models.lsdvarible.objects.create(
                                            vbname=proName,
                                            vbkey=prokey,
                                            vbaddr=proattr,
                                            vbpop=vbpop,
                                            createtime=createtime,
                                            updatetime=createtime,

                                             )
        data["status"] = 200
        data["msg"] = "请求成功"
        return HttpResponse(json.dumps(data))
    else:
        return render_to_response("login.html")


def lsdvarible(req):
    data = {
        "list":[

        ]

    }
    if updateValid.cookiesInspect(req):
        if req.method == "GET":
            print("ggggg", req.method)
            return  render_to_response("lsdvarible.html")
        else:

            print(req.method)
            obj=models.lsdvarible.objects.all()
            i=0
            for  key  in obj:
                print(key.vbname,key.vbkey,key.createtime)
                print(data["list"].append({}))
                data["list"][i]["vbname"]=key.vbname
                data["list"][i]["vbkey"] = key.vbkey
                data["list"][i]["vbaddr"] = key.vbaddr
                data["list"][i]["vbpop"] = key.vbpop
                data["list"][i]["createtime"] = str(key.createtime).split("+")[0]
                data["list"][i]["updatetime"] = str(key.updatetime).split("+")[0]
                i+=1
            print("obj",obj)
            data["status"] = 200
            data["msg"] = "请求成功"

            print(data)
            return HttpResponse(json.dumps(data))
    else:
        return render_to_response("login.html")


