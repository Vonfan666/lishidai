from   django.shortcuts  import  redirect,render_to_response,render,HttpResponse
def  login(req):
    return render_to_response('login.html')

