import requests
from bs4 import BeautifulSoup


url = 'https://news.baidu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36',
}
r = requests.get(url, headers=headers)
#
soup = BeautifulSoup(r.text, 'lxml')
a = soup.find_all('a')
for i in a:
    s = i.get('href')
    if s is not None:
        if 'http' in s:
            print(i.get('href'))
