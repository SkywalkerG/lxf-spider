import requests
from lxml import etree
from bs4 import BeautifulSoup

url = 'https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'
}
r = requests.get(url, headers=headers)
print(r.text)