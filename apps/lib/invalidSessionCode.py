#!/usr/bin/python3
# -*- conding:utf-8 -*-
#auther=von-fan
# class InvalidSession():
#     def  __init__(self,phone,pwd):
#         self.phone=phone
#         self.pwd=pwd
#
#
#     def  invalidLogin(self,req):
#
#         print(req.session)
#         # req.COOKIES.get()
#
#         if req.COOKIES.get("phone",None)==None:
#             return  False
#
#         if  req.session.get(self.phone,None)==None:
#             return  False
#
#         if req.COOKIES.get(self.phone)==req.session[self.phone] and req.COOKIES.get(self.pwd)==req.session[self.pwd]:
#             print("1")
#             return True
#
#         else:
#             return False
#
#     def  delSession(self):
#         phone=str(self.phone)
#         return   phone
from django.shortcuts import render_to_response,render
class InvalidSession():
    def __init__(self, phone, pwd):
        self.phone = phone
        self.pwd = pwd
    def cookiesInspect(self,req):
        if req.COOKIES.get("phone", None) == None:

            return False
        if req.session.get(self.phone, None) == None:
            return False
        if req.COOKIES.get(self.phone) == req.session[self.phone] and req.COOKIES.get(self.pwd) == req.session[
            self.pwd]:
            print("1")
            return True
        else:
            return False
    def cookiesVerify(self,*args):
        def invalidLogin(func):
            def inv(req):
                func(req)
                print(req.session)
                if self.cookiesInspect(req):
                    return render(req,*args)

                else:
                    return render(req,"login.html")
            return  inv
        return  invalidLogin







    def delSession(self):
        phone = str(self.phone)
        return phone










