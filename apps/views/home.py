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
    print(1111111111111111111111)
    print(req.POST,"!!!!!!!!!!!!!!!!!!!!")
    '''新增环境'''
    data={}

    # print("----------------",req)
    # print(req.POST)
    #
    # print(model_to_dict(req.POST))
    if Valid.cookiesInspect(req):  #重新写一个装饰器

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
        print(req.POST)
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
                data["list"][i]["createtime"] = str(key.createtime).split("+")[0]
                data["list"][i]["updatetime"] = str(key.updatetime).split("+")[0]
                i+=1
            print("obj",obj)
            data["status"] = 200
            data["msg"] = "操作成功"

            return HttpResponse(json.dumps(data))
    else:
        return render_to_response("login.html")
#新增项目
def addProject(req):
    print("!!!!!!!!!!!!!!!!!")
    print(req.POST,"!!!!!!!!!!!!")
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

        datacode=models.lsdproject.objects.all().values("procode", "proname", "proversion","provaronemany_id__vbname",
                                                          "provarmaymany__phone","updatetime","provaronemany_id").order_by("updatetime").reverse()
        for  a  in  datacode:
            a["updatetime"]=str(a["updatetime"]).split("+")[0]
            data["list"].append(a)
        data["status"]=200
        data["msg"]="添加成功"
        return HttpResponse(json.dumps(data))
    else:
        return render_to_response("login.html")
#编辑项目
def editProject(req):
    print("_________________",req.POST)
    data={
        "msg":None,
        "list":[],
        "status":None
    }

    if Valid.cookiesInspect(req):
        proCode=req.POST.get("proCode")
        proName=req.POST.get("proname")
        proversion=req.POST.get("proversion")
        provarible=req.POST.get("provarible")

        print(proCode,proversion,proName)
        if proName is None or proversion is None or provarible is None or provarible is "0" :
            data["msg"]="输入不能为空"
        else:
            models.lsdproject.objects.filter(procode=proCode).update(proname=proName,proversion=proversion,provaronemany_id=provarible)
            data["msg"]="修改成功"
            data["status"] = 200
    else:return render_to_response("login.html")
    return HttpResponse(json.dumps(data))
#删除项目
def clearProject(req):
    data = {
        "list":[

        ]

    }
    proCode=req.POST.get("proCode")
    if Valid.cookiesInspect(req):
        models.lsdproject.objects.filter(procode=proCode).delete()

        data["msg"]="删除成功"
        data["status"]=200
    else:
        data["msg"]="删除失败"
    return  HttpResponse(json.dumps(data))
#查看项目
def lookproject(req):
    data = {
        "list": [

        ]

    }
    if  Valid.cookiesInspect(req):
        datacode = models.lsdproject.objects.all().values("procode", "proname", "proversion","provaronemany_id__vbname",
                                                          "provarmaymany__phone","updatetime","provaronemany_id").order_by("updatetime").reverse()
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
        res = models.lsdproject.objects.filter(proname__contains=t).values("procode","proname","proversion","provaronemany_id__vbname","provarmaymany__phone","updatetime").order_by("updatetime").reverse()
        print("_______________",res)
        print(bool(res))
        if res:
            for dic in res:
                dic["updatetime"] = dic["updatetime"].strftime("%Y-%m-%d %H:%M:%S")
                data["list"].append(dic)
        else:
            data["msg"]="未搜索到关键词,请重新输入！"
    else:
        res = models.lsdproject.objects.all().values("procode","proname","proversion","provaronemany_id__vbname","provarmaymany__phone","updatetime").order_by("updatetime").reverse()
        for dic in  res:
            dic["updatetime"]=dic["updatetime"].strftime("%Y-%m-%d %H:%M:%S")
            data["list"].append(dic)

        # print(serializers.serialize('json', res))
        # # data["list"]=(json.loads(serializers.serialize('json',res)))
        print(data)

    data["status"]=200




    return  HttpResponse(json.dumps(data))


def  findVarible(req):
    print("path----",req.path)
    if  Valid.cookiesInspect(req):
        pass
    else:
        pass
    return HttpResponse(111)