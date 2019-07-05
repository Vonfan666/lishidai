#!/usr/bin/python3
# @File:.py
# -*- coding:utf-8 -*-
# @Author:von_fan
# @Time:2019年07月04日00时51分30秒
import time,random,os

class Method():
    def __init__(self):
        pass


    def proId(self):
        timeStr=time.strftime('%Y%m%d%H%M%S')
        a=str(random.randrange(100,999))
        return "{}{}".format(timeStr,a)


    def nowTime(self):
        timeStr = time.strftime('%Y-%m-%d %H:%M:%S')
        return timeStr

if  __name__=="__main__":
    MyMethod=Method()
    a=MyMethod.nowTime()
    print(a,type(a))




