from  django.shortcuts import render,HttpResponse,redirect,render_to_response
from  django.utils.deprecation import MiddlewareMixin
import  re,json


class MyMiddleware(MiddlewareMixin):
    print(11111)
    def process_request(self,request):
        data={}
        print("执行过滤器--------------1")
        self.request = request
        self.noIncludedPath = ["/apps/login/", '/apps/backLogin/']
        self.rePath = [re.compile(item) for item in self.noIncludedPath]
        path=self.request.path
        for item in  self.rePath:
            print("执行过滤器--------------0")
            print(item.match(path))
            if  item.match(path):
                print(item.match(path))
                return
            else:
                if self.request.COOKIES.get("phone", None) == None:
                    print("执行过滤器--------------2")
                    data["status"]=0
                    return HttpResponse(json.dumps(data))
                if self.request.session.get("phone", None) == None:
                    print("执行过滤器--------------3")
                    data["status"] = 0
                    return HttpResponse(json.dumps(data))
                if self.request.COOKIES.get("phone") == self.request.session["phone"] and self.request.COOKIES.get("pwd") == self.request.session["pwd"]:
                    print("执行过滤器--------------4")
                else:
                        return HttpResponse(json.dumps({"status": 0}))
                return
