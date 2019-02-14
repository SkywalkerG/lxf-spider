import requests
from bs4 import BeautifulSoup
from lxml import etree
from pymongo import MongoClient
import time




client = MongoClient('localhost', 27017)
ganji = client['ganji']
url_list = ganji['url_list']
err_url_list = ganji['err_url_list']

headers = {
	'user-agent' : 'Opera/9.82.(X11; Linux x86_64; iw-IL) Presto/2.9.183 Version/10.00'
}

url = 'http://bj.ganji.com/chuangdian/allcity/'
url1 = 'http://bj.ganji.com/qitaxuniwupin/allcity/'

def get_page_link(url):
    try:
        r = requests.get(url, headers=headers, timeout = 6).content
        time.sleep(1)
        # cate = url.split('/')[-3]
        html = etree.HTML(r)
        if not html.xpath('//div[@class="noinfo"]'):
            items = html.xpath('//table[@class="tbimg"]//td[@class="t"]/a[@class="t"]')
            for item in items:
                data = {}
                data['title'] = item.xpath('.//text()')[0]
                data['href'] = item.xpath('.//@href')[0]
                # data['cate'] = cate
                print(data)
                url_list.insert_one(data)
        else:
            return
    except:
        err_url_list.insert_one(url)
        print(url)


def get_one_cate(url):
    url_format = url + 'o{}'
    for i in range(0,34):
        if i == 1:
            pass
        else:
            url = url_format.format(str(i))
            get_page_link(url)



def get_detail(item_url):
    r = requests.get(url, headers=headers).content.decode()
    html = etree.HTML(r)
