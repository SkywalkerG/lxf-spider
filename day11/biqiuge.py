import requests
from bs4 import BeautifulSoup

url = 'https://www.biqiuge.com/book/4772/26859742.html'
r = requests.get(url).content.decode('gbk')

soup = BeautifulSoup(r, 'lxml')
title = soup.select('h1')[0].get_text()
content = soup.select('.showtxt')[0].get_text()

print(title)
print(content)