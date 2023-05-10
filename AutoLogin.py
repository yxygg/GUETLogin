import requests
def is_online() -> bool:
    try:
        requests.get('https://www.baidu.com/favicon.ico', timeout=3)
        return True
    except:
        return False
def login():
    if not is_online():
        url = "http://10.0.1.5:801/eportal/portal/login"
        params = {
            "callback":"dr1003",
            "login_method":"1",
            "user_account":",0,学号", # 账号 后缀@cmcc移动@unicom联通@telecom电信
            "user_password":"密码", # 密码
            "wlan_user_mac":"000000000000",
            "terminal_type":"1",
            "lang":"zh-cn"
            }
        try:
            requests.request("GET", url, params=params)
        except:
            pass
    else:
        return True
if __name__ == '__main__':
    login()
