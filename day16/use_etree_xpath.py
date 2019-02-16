from lxml import etree
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
}

r = requests.get('https://www.xicidaili.com/nn/1', headers=headers).content.decode()

html = etree.HTML(r)
trs = html.xpath('//tr')
for tr in trs[1:]:
    ip = tr.xpath('.//td[2]/text()')[0]
    port = tr.xpath('.//td[3]/text()')[0]
    cate = tr.xpath('.//td[6]/text()')[0]
    print(ip,type(ip), port, cate)
    print('------------'*3)