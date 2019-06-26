from   django.shortcuts  import  redirect,render_to_response,render,HttpResponse
import  json
from  apps.lib import fromInvalid

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

            a={'msg':'登录成功','statu':200,'errorMassage':'null'}

            return HttpResponse(json.dumps(a))
        else:
            print(obj.cleaned_data)
            print(obj.clean())
            print("错误信息",obj.errors)

            try:
                errorMassagePhone=obj.errors['phone']
                data['errorMassagePhone']=obj.errors['phone']
            except:
                errorMassagePwd = obj.errors['pwd']
                a1=print(obj.errors['pwd'])
                print(errorMassagePwd)

                a={'errorMassage':errorMassagePwd}
                a=json.dumps(a)
                return HttpResponse(a)

