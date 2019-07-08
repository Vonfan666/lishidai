#!/usr/bin/python3
# @File:.py
# -*- coding:utf-8 -*-
# @Author:von_fan
# @Time:2019年07月04日01时28分44秒

from django.shortcuts import render_to_response,HttpResponse,redirect
from apps.lib import *
from  apps import models
import  json,datetime
from  django.core import serializers

from  django.http import QueryDict
from django.forms.models import model_to_dict





@Valid.cookiesVerify("home.html")
def  home(req):

     return render_to_response("home.html")
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

def  addLsdvarible(req):
    '''新增环境'''
    data={}

    # print("----------------",req)
    # print(req.POST)
    #
    # print(model_to_dict(req.POST))
    if Valid.cookiesInspect(req):  #重新写一个装饰器
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
        data["msg"] = "操作成功"
        return HttpResponse(json.dumps(data))
    else:
        return render_to_response("login.html")

def lsdvarible(req):
    '''查看环境列表'''
    data = {
        "list":[

        ]

    }
    if Valid.cookiesInspect(req):
        if req.method == "GET":

            return  render_to_response("lsdvarible.html")
        else:

            print(req.method)
            obj=models.lsdvarible.objects.all()
            i=0
            for  key  in obj:
                print(key.vbname,key.vbkey,key.createtime)
                print(data["list"].append({}))
                data["list"][i]["id"] = key.id
                data["list"][i]["vbname"]=key.vbname
                data["list"][i]["vbkey"] = key.vbkey
                data["list"][i]["vbaddr"] = key.vbaddr
                data["list"][i]["vbpop"] = key.vbpop
                data["list"][i]["createtime"] = str(key.createtime).split(".")[0]
                data["list"][i]["updatetime"] = str(key.updatetime).split(".")[0]
                i+=1
            print("obj",obj)
            data["status"] = 200
            data["msg"] = "操作成功"

            return HttpResponse(json.dumps(data))
    else:
        return render_to_response("login.html")

def addProject(req):
    data = {
        "list": [

        ]

    }
    if req.POST.get("provarible")=="0":
        data["status"] = 103
        data["msg"] = "请选择环境"
        return HttpResponse(json.dumps(data))

    elif  Valid.cookiesInspect:
        datacode=req.POST
        datacode=datacode.dict()
        datacode["procode"]=mymethod.proId()
        datacode["provaronemany_id"]=datacode["provarible"]
        datacode.pop("provarible")
        datacode["updatetime"]=mymethod.nowTime()

        models.lsdproject.objects.create(**datacode,)

        datacode=models.lsdproject.objects.all().values("procode","proname","proversion","provaronemany_id__vbname","provarmaymany__phone")
        for  a  in  datacode:



            data["list"].append(a)
        data["status"]=200
        data["msg"]="添加成功"
        return HttpResponse(json.dumps(data))
    else:
        return render_to_response("login.html")

#查看环境
def lookproject(req):
    data = {
        "list": [

        ]

    }
    if  Valid.cookiesInspect(req):
        datacode = models.lsdproject.objects.all().values("procode", "proname", "proversion","provaronemany_id__vbname",
                                                          "provarmaymany__phone","updatetime")
        for a in datacode:
            print(a["updatetime"])
            a["updatetime"]=str(a["updatetime"]).split("+")[0]
            data["list"].append(a)
        data["status"] = 200
        data["msg"] = "添加成功"

        return HttpResponse(json.dumps(data))
    else:
        return render_to_response("login.html")


#搜索项目名称
def findProject(req):
    data={
        "msg":None,
        "list":[],
        "status":None,
    }
    t=req.POST.get("proName")
    print(t)
    if t:
        print("ttttttttttttttt",bool(t))
        res = models.lsdproject.objects.filter(proname__contains=t).values("procode","proname","proversion","provaronemany_id__vbname","provarmaymany__phone","updatetime")
        print("_______________",res)
        print(bool(res))
        if res:
            for dic in res:
                dic["updatetime"] = dic["updatetime"].strftime("%Y-%m-%d %H:%M:%S")
                data["list"].append(dic)
        else:
            data["msg"]="未搜索到关键词,请重新输入！"
    else:
        res = models.lsdproject.objects.all().values("procode","proname","proversion","provaronemany_id__vbname","provarmaymany__phone","updatetime")
        for dic in  res:
            dic["updatetime"]=dic["updatetime"].strftime("%Y-%m-%d %H:%M:%S")
            data["list"].append(dic)

        # print(serializers.serialize('json', res))
        # # data["list"]=(json.loads(serializers.serialize('json',res)))
        print(data)

    data["status"]=200




    return  HttpResponse(json.dumps(data))