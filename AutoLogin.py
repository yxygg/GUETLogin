import requests
def is_online() -> bool:
    try:
        requests.get('https://www.baidu.com/favicon.ico', timeout=2)
        return True
    except:
        return False
def login():
    if not is_online():
        url = "http://10.0.1.5/drcom/login"
        params = {
            "callback":"dr1003",
            "DDDDD":"学号@运营商(例如unicom)",
            "upass":"密码", 
            }
        try:
            return(requests.request("GET", url, params=params))
        except:
            return 'Fail to login!'
    else:
        return 'Already online!'
if __name__ == '__main__':
    print(login())
