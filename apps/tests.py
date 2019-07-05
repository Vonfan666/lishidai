import requests
ur = 'https://h5test.buylala.cn/shoppingmall/anon/loginForCode'
he = {'req-source': 'IOS',
     'Content-Type': 'application/json',
     'Host': 'h5test.buylala.cn'}
dd = {"code": "123456", "userName": "15900000000"}

ur1 ="https://h5test.buylala.cn/shoppingmall/anon/getDetail"
he1 ={'req-source': 'IOS',
     'Content-Type': 'application/json',
      # 'token':'response.json()["data"]["jwt"]',
     'Host': 'h5test.buylala.cn'}
dd1 = {"goodsId":"193435496555610112"}
class Tets():
    def __init__(self,url,headers,data):
        self.url=url
        self.headers=headers
        self.data=data


    def post(self):
        response = requests.post(url=self.url ,headers=self.headers,json=self.data)
        print(response.json()["data"]["jwt"])
        self.token=response.json()["data"]["jwt"]

        self.xingxing=1
        print(response.text)


class css():
    def __init__(self,url1,headers1,data1):
        self.url1=url1
        self.headers1=headers1
        self.headers1["token"]=pr.token
        self.data1=data1
    def post1(self):
        response1 = requests.post(url=self.url1 ,headers=self.headers1 , json=self.data1)
        print(response1.json())

pr=Tets(ur,he,dd)
pr.post()

pr1=css(ur1,he1,dd1)
pr1.post1()


print(pr.__dict__)
