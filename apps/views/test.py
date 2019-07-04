# from   django.shortcuts  import  HttpResponse
# # from django.utils.check_code import create_validate_code
#
#
#
# class A():
#     def __init__(self,m):
#         self.m=m
#         self.n=0
#     #     self.req=req
#
#     # def ee(self,a):
#     #     return a+1
#
#     def  deco(self,func,*args):
#
#         def coo(a,*args):
#
#
#             c=1
#             print(*args,type(*args))
#             qq=func(a,*args)+c
#
#             return qq
#
#
#         return coo
#
#
#
#
#
# test=A(1)
# @test.deco(1)
# def add(a,*args):
#     return a
#
#
#
# print(add(1,3))

def  a(req):
    print(req)
    return  1


b=a
print(b)


