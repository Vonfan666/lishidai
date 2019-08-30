from  django.shortcuts import render,HttpResponse,redirect,render_to_response
from  django.utils.deprecation import MiddlewareMixin
import  re,json,os
from  apps.log.logCof  import  logger
logger=logger(os.path.basename(__file__))

class MyMiddleware(MiddlewareMixin):
    def process_request(self,request):

        data={}
        logger.info("执行过滤器---------0")
        self.request = request
        self.noIncludedPath = ["/apps/login/", '/apps/backLogin/']
        self.rePath = [re.compile(item) for item in self.noIncludedPath]
        path=self.request.path
        for item in  self.rePath:

            logger.info("url地址：%s"%item)
            logger.info("执行地址是：%s" % __file__)
            if  item.match(path):
                print(item.match(path))
                return
            else:
                if self.request.COOKIES.get("phone", None) == None:
                    if self.request.method=="GET":
                        return render_to_response("login.html")
                    else:
                        logger.info("执行过滤器---------1")
                        data["status"]=0
                        return HttpResponse(json.dumps(data))
                if self.request.session.get("phone", None) == None:
                    if self.request.method=="GET":
                        return render_to_response("login.html")
                    else:
                        logger.info("执行过滤器---------2")
                        data["status"]=0
                        return HttpResponse(json.dumps(data))
                if self.request.COOKIES.get("phone") == self.request.session["phone"] and self.request.COOKIES.get("pwd") == self.request.session["pwd"]:
                    logger.info("执行过滤器---------3")
                    return
                else:
                        if self.request.method=="GET":
                            return render_to_response("login.html")
                        else:
                            data["status"] = 0
                            return HttpResponse(json.dumps(data))


