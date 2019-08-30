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
    def __init__(self,totalCount,nowPage,onePageCount,pageNumber=11):
        '''
        :param totalCount: 数据总条数
        :param nowPage:  当前是第几页
        :param onePageCount: 每页返回多少条
        :param pageNumber: 页面最多展示页数
        '''
        self.totalCount=totalCount
        self.nowPage=nowPage
        self.onePageCount=onePageCount
        self.pageNumber=pageNumber


    def start(self):
        '''计算出前端传来的页面 起始索引'''
        return  (self.nowPage-1)*self.onePageCount

    def  end(self):
        return self.nowPage* self.onePageCount


    def allPage(self):
        '''计算前端需展示的页数'''
        a,b=divmod(self.totalCount,self.onePageCount)
        if b==0:
            return a
        return a+1



    def onlySedPage(self):
        '''仅仅需要展示的页码'''
        if  self.allPage()<=self.pageNumber:
            return range(1,self.allPage()+1)

        else:
            if  self.nowPage<self.pageNumber/2:
                return range(1,self.pageNumber+1)
            if  self.nowPage>self.pageNumber/2+1  :
                return range(self.nowPage-self.pageNumber/2,self.nowPage+self.pageNumber/2)


            if self.nowPage+self.pageNumber/2>self.allPage():
                return range(self.allPage()-self.pageNumber+1,self.allPage())




