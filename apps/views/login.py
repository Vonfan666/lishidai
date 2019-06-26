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

        return render_to_response('login.html')
    else:
        obj=fromInvalid.LoginInvalid(req.POST)
        isInvalid=obj.is_valid()
        if  isInvalid:
            print('验证成功',obj.cleaned_data)
            print(obj.clean())
            print('phone',req.POST.get('phone'))
            obj=models.Login.objects.filter(phone=req.POST.get('phone')).values('pwd')
            if req.POST.get('pwd')==obj[0]["pwd"]:
                a={'msg':'登录成功','statu':200,'errorMassage':'null'}
            else:
                data['errorMassage']='账号或密码错误'
                a = json.dumps(data)


            return HttpResponse(a)
        else:
            print(obj.cleaned_data)
            print(obj.clean())
            print("错误信息",obj.errors)
            for  a  in  obj.errors:
                try:
                    data['errorMassage']=obj.errors[a][0]
                except:
                    pass
            a=json.dumps(data)
            return HttpResponse(a)

