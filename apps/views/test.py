'''
数据：
[
    {"jobs": {"chroots": {"env": "#LIST#"}}},
    {"jobs": {"chroots": {"restartPolicy": "Never"}}},
    {"jobs": {"chroots": {"enabled": "false"}}},
]

[
{"jobs":
    {"chroots": {"env": "#LIST#"}}



    }

]

变成：

{
    "jobs": {
        "chroots":{
            "env": "#LIST#",
            "restartPolicy": "Never",
            "enabled": "false"
        }
    }
}
'''

a=[
    {"jobs": {"chroots": {"env": "#LIST#"}}},
    {"jobs": {"chroots": {"restartPolicy": "Never"}}},
    {"jobs": {"chroots": {"enabled": "false"}}},
    {"cao":"haha"},
]

alen = len(a)
def  one(ele):


    listKey=[]


    for  n in  range(alen):
       for  key,value in  a[n].items():
           listKey.append({key:value})
           # listValue.append(value)
    print(listKey)
    return listKey

def  com():
    i=1
    dictCode={}
    for  n in  range(len(one(alen))-1):
        if  one(alen)[n]==one(alen)[n+1][0]:
            print(one(alen)[n][0])
            dictCode[one(alen)[n][0]]=one(alen)[n][1]

        else:
            pass

    print(dictCode)


com()

