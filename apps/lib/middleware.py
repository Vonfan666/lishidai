from  django.shortcuts import render,HttpResponse,redirect,render_to_response
from  django.utils.deprecation import MiddlewareMixin
import  re


class MyMiddleware(object):
    def __init__(self,request):
        self.request=request
        self.noIncludedPath=["/login/",'/backLogin/']
        self.rePath=[re.compile(item)  for item in  self.noIncludedPath]


    def process_request(self,request):
        path=self.request.path

