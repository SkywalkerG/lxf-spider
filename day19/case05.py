# python 执行一段更加复杂的lua脚本
# 抓取京东商品信息


import json
import requests
from lxml import etree
from urllib.parse import quote

lua = '''
function main(splash, args)
    local treat = require('treat')
    local response = splash:http_get("https://search.jd.com/Search?keyword=相机&enc=utf-8")
        return {
            html = treat.as_string(response.body),
            url = response.url,
            status = response.status
        }
end
'''

url = 'http://192.168.99.100:8050/execute?lua_source=' + quote(lua)

r = requests.get(url).content.decode()
# print(json.loads(r)['html'])
html = etree.HTML(json.loads(r)['html'])

prices = html.xpath('//div[@class="p-price"]/strong/i/text()')
titles = html.xpath('//div[@class="p-name p-name-type-2"]/a/em/text()')
for p,t in zip(prices, titles):
    print(p,t)
