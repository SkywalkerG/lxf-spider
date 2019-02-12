import re
import requests
from lxml import etree
from bs4 import BeautifulSoup
import time

url = 'http://8btc.com/'
urls = 'http://8btc.com/forum-61-{}.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36',
}
r = requests.get(url = url, headers = headers)
# print(r.text)
# use re
# <a href="http://8btc.com/thread-138665-1-1.html" style="font-weight: bold;color: #EE1B2E;" onclick="atarget(this)" class="s xst"> 【巴比特直播间】聚合贴：零距离对话圈内大佬</a>
#<a href="http://8btc.com/thread-155659-1-1.html" style="font-weight: bold;color: #EE1B2E;" onclick="atarget(this)" class="s xst"> 【巴比特区块链新人学堂】从0到1，区块链速成指南！</a>
#<a href="http://8btc.com/thread-266159-1-1.html" onclick="atarget(this)" class="s xst"> 【老金谈币】 每日行情分析！客观！简单！粗暴！</a>

# pattern = re.compile('<a href="(.*?)".*?class="s xst">(.*?)</a>', re.S)
# pattern = re.compile('<a href="(.*?)".*?class="s xst">(.*?)</a>', re.S)
#
# result = pattern.findall(r.text)
# print(result,print(len(result)))

# use xpath is faster 10 than bs4
# t1 = time.clock()
html = etree.HTML(r.text)
titles = html.xpath('//a[@class="s xst"]/text()')
links = html.xpath('//a[@class="s xst"]/@href')
print(titles, len(titles))
print(links, len(links))
# t2 = time.clock()
# print(t2-t1)

# use bs4
# t1 = time.clock()
soup = BeautifulSoup(r.text, 'html5lib')
titles = [i.text for i in soup.select('a.s.xst')]
links = [i.get('href') for i in soup.select('a.s.xst')]
print(titles, len(titles))
print(links, len(links))
# t2 = time.clock()
# print(t2-t1)