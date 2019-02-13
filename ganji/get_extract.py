import requests
from bs4 import BeautifulSoup
from lxml import etree
# from faker import Faker

# fake = Faker(locale="zh-CN")
headers = {
	'user-agent' : 'Opera/9.82.(X11; Linux x86_64; iw-IL) Presto/2.9.183 Version/10.00'
}

url_base = 'http://bj.ganji.com'

def parse_index():
	url = 'http://bj.ganji.com/wu/'
	r = requests.get(url, headers=headers).content.decode()
	html = etree.HTML(r)
	links = html.xpath('//dl[@class="fenlei"]/dt/a/@href')
	fenlei_link = [url_base + i for i in links]
	return fenlei_link

def parse_fenlei(fenlei_link):
	all_links = []
	for link in fenlei_link:
		r = requests.get(link, headers=headers).content.decode()
		html = etree.HTML(r)
		links = html.xpath('//dd[@class="w-short"]/a/@href')
		cate_links = [url_base + i for i in links]	
		for i in cate_links:
			all_links.append(i)
	print(all_links)

if __name__ == '__main__':
	fenlei_link = parse_index()
	parse_fenlei(fenlei_link)