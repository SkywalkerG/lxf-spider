import requests
from bs4 import BeautifulSoup

url = "http://wz.sun0769.com/index.php/question/reply?page=120"
r = requests.get(url).content.decode('gbk')
soup = BeautifulSoup(r, 'lxml')
# body > div.newsHead.clearfix > table:nth-child(2) > tbody > tr:nth-child(10) > td:nth-child(3) > a:nth-child(1)
results = soup.select('td.txt18 > a:nth-of-type(1)')
print(len(results))
# print(results)