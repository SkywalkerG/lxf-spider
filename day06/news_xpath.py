import requests
from lxml import etree


url = 'https://news.baidu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36',
}
r = requests.get(url, headers=headers).text
# print(r)
# 1. 转成xpath能解析的类型
xpath_data = etree.HTML(r)

# xpath 语法 1. 节点 /
#            2. 跨节点 //
#            3. 精确标签 //a[@属性名="属性标签"]
#            4. 标签包裹的内容 text()
#            5. 属性:@href
# 注意事项 //li[3] 可以取到平级li标签的第三个  //li//a[2] 取到的是空  a必须为平级标签才能用列表
# 2. 调用xpath的方法
result = xpath_data.xpath('/html/head/title/text()')
print(result)
result = xpath_data.xpath('//a/text()')
print(result)
print(len(result))
result = xpath_data.xpath('//a[@mon="r=1"]/text()')
print(result)
result = xpath_data.xpath('//a[@mon="r=1"]/@href')
print(result)