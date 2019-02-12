import re
import requests


url = 'https://news.baidu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36',
}
r = requests.get(url, headers=headers)
#
pattern = re.compile('<a href="(.*?)".*?>(.*?)</a>', re.S)
result = pattern.findall(r.text)
print(result)