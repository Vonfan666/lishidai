from   django.shortcuts  import  redirect,render_to_response,render,HttpResponse
import  json
from  apps.lib import fromInvalid
from apps import models

def  index(req):
    return render_to_response('login.html')

def  login(req):
    data={}
    print(req.method)
    if req.method=='GET':
        data['errorMassage'] = '请求类型错误'
        a = json.dumps(data)
        return render_to_response('login.html',locals())
    else:
        obj=fromInvalid.LoginInvalid(req.POST)
        isInvalid=obj.is_valid()
        if  isInvalid:
            obj=models.Login.objects.filter(phone=req.POST.get('phone')).values('pwd')
            if  obj:
                print(obj,obj[0])
                if req.POST.get('pwd')==obj[0]["pwd"]:
                    data={'msg':'登录成功','status':200,'errorMassage':'null'}
                else:
                    data['errorMassage']='您输入的密码有误！'
            else:
                data['errorMassage'] = '您输入的账号不存在！'
            a = json.dumps(data)
            return HttpResponse(a)
        else:
            for  a  in  obj.errors:
                try:
                    data['errorMassage']=obj.errors[a][0]
                except:
                    pass
            a=json.dumps(data)
            return HttpResponse(a)



def  home(req):
    return  render_to_response('home.html')
