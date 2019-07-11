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


class Pagination():
    def __init__(self,totalCount,nowPage,onePageCount,pageNumber):
        '''
        :param totalCount: 数据总条数
        :param nowPage:  当前是第几页
        :param onePageCount: 每页返回多少条
        :param pageNumber: 总共几页
        '''
        self.totalCount=totalCount
        self.nowPage=nowPage
        self.onePageCount=onePageCount
        self.pageNumber=pageNumber


    def firstPage(self):
        '''计算出前端传来的页面 起始索引'''
        return  (self.nowPage-1)*self.onePageCount


    def allPage(self):
        '''计算前端需展示的页数'''
        a,b=divmod(self.totalCount,self.onePageCount)
        if b==0:
            return a
        return a+1



