from  django.shortcuts import render,HttpResponse,redirect,render_to_response
from  django.utils.deprecation import MiddlewareMixin
import  re


class MyMiddleware(object):
    def __init__(self,request):
        self.request=request
        self.noIncludedPath=["apps/login/",'apps/backLogin/']
        self.rePath=[re.compile(item)  for item in  self.noIncludedPath]


    def process_request(self,request):
        path=self.request.path
        for item in  self.rePath:
            if  item.match(path):
                return render_to_response("login.html")
        else:
            if self.request.COOKIES.get("phone", None) == None:
                return None
            if self.request.session.get("phone", None) == None:
                return None
            if self.request.COOKIES.get("phone") == self.request.session["phone"] and self.request.COOKIES.get("pwd") == self.request.session["pwd"]:
                return True
    def process_view(self,request):
        pass

    def process_exception(self,request):
        pass

    def process_response(self,request):
        pass


