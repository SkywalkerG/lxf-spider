import requests
from lxml import etree

# url = 'https://www.toutiao.com/'
url = 'http://192.168.99.100:8050/render.html?url=https://www.toutiao.com/'
r = requests.get(url).content.decode()
html = etree.HTML(r)
titles = html.xpath('//div[@class="bui-left index-content"]//a[@class="link"]/text()')
print(titles)