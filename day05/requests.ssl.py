import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'
}

url = 'https://www.12306.cn/'
# requests.exceptions.SSLError
resp = requests.get(url, headers=headers, verify=False)
print(resp.content.decode())