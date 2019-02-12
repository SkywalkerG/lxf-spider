import requests
from lxml import etree
import json
class BtcClass(object):

    def __init__(self):
        # self.url = 'http://8btc.com/'
        self.urls = 'http://8btc.com/forum-61-{}.html'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36',
        }
        self.news_list = []
        # self.resp = requests.get(self.url, headers = self.headers).text

    # 发请求
    def send_request(self, url):
        resp = requests.get(url, headers=self.headers).text
        return resp

    # 解析网页返回来的数据
    def parse_html(self, resp):
        html = etree.HTML(resp)
        titles = html.xpath('//a[@class="s xst"]/text()')
        links = html.xpath('//a[@class="s xst"]/@href')
        for title, link in zip(titles, links):
            data = {
                'title': title,
                'link': link
            }
            # print(data)
            self.news_list.append(data)

    # 保存数据
    def save_data(self):
        with open('btc.json', 'w') as f:
            f.write(json.dumps(self.news_list) + '\n')
    # 运行爬虫
    def run(self):
        for i in range(1,3):
            url = self.urls.format(str(i))
            print(url)
            resp = self.send_request(url)
            self.parse_html(resp)
            self.save_data()



if __name__ == '__main__':
    BtcClass().run()