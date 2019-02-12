import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'
}

url = 'http://www.baidu.com'

proxy = {
    'http': '171.41.82.86:9999'
}
resp = requests.get(url, headers, proxies = proxy)
print(resp.status_code)
print(resp.headers)