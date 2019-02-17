import requests
from lxml import etree

import json
from bs4 import BeautifulSoup
url = 'https://mp.weixin.qq.com/s?timestamp=1550371452&src=3&ver=1&signature=cPRRJaaSQ45xLpzA98R9M3AvUOoLchbTsxrahyCbcMx9FyZQFicKxJP3FRR7tlBC3hfPguK8aK-nIMIuumj8eusJqj-wNV4lp6lmETQ5GU2wwo2kg7MkMfTMBWONVfiIienfNRLOXhN8ixESjFU1aWorkX60wWvnBASHelQggGA='
r = requests.get(url).content.decode()
# soup = BeautifulSoup(r, 'lxml')
# print(soup.prettify())
html = etree.HTML(r)
# sections =  html.xpath('//section[@data-preserve-color="t"]')
# print(sections)
contents = html.xpath('//section[@data-tools="新媒体排版"]')
with open('mugglecode.json', 'w') as f:
    for content in contents[1:-3]:
        content = ' '.join(content.xpath('.//span/text() | .//strong/text()'))
        f.write(json.dumps(content))
        print(content)
        print('-------------')

