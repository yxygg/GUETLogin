import requests
data={
'DDDDD': '',
'upass': ''
}
respond=requests.post("",data).status_code
print("登录成功" if respond==200 else "登录失败")