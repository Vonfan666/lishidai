class InvalidSession():
    def  __init__(self,phone,pwd):
        self.phone=phone
        self.pwd=pwd


    def  invalidLogin(self,req):

        if req.COOKIES.get("phone",None)==None:
            return  False

        if req.COOKIES.get(self.phone)==req.session[self.phone] and req.COOKIES.get(self.pwd)==req.session[self.pwd]:

            return True

        else:
            return False

if  __name__=="__main__":
    authUserLogin=InvalidSession("phone","pwd")






