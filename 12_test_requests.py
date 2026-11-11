import requests

print("requests 版本：", requests.__version__)

r = requests.get("https://www.baidu.com", timeout=5)
print("状态码：", r.status_code)
print("返回内容长度：", len(r.text))