import requests

# 发送 post 请求
# data = {
#
# }
#
# resp = requests.post(url, data)

# 内网
auth = ('user', 'pass')
url = 'https://api.github.com/user'
resp = requests.get(url, auth=auth)
print(resp.json())