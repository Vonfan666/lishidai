from django.test import TestCase

# Create your tests here.
import requests,json


class Tets():
    def __init__(self,ip):
        self.ip=ip

    def post(self,url,data,headers):
        ur2 = self.ip +url
        response = requests.post(ur2,data,headers=headers)
        print(response.text)

url_post= '/shoppingmall/anon/loginForCode/'
headers_post= {'req-source': 'IOS',
     'Content-Type': 'application/json',
     'Host': 'h5test.buylala.cn'}
data_post= {"code":"123456","userName":"15900000000"}

pr=Tets('https://h5test.buylala.cn/')
data_post=json.dumps(data_post)  #用data就要转成json格式
pr.post(url_post,data_post,headers_post)
