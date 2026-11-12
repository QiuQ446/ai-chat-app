import requests

url = "https://api.github.com/users/this_user_does_not_exist_12345"

try:
    r = requests.get(url,timeout = 10)
    r.raise_for_status()
    data = r.json()

    print("类型：", type(data))
    print("用户名：", data["login"])
    print("粉丝数：", data["followers"])
    print("主页：", data["html_url"])

except requests.RequestException as e:
    print("请求失败：",e)