import requests

url = 'http://www.baidu.com/s'

resp = requests.get(url, params={'wd':'美女'})
with open('baidu.html', 'wb') as f:
    f.write(resp.content)