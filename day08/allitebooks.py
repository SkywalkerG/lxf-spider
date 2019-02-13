import requests
from bs4 import BeautifulSoup
from lxml import etree
import re
import json
import csv



class AllitebooksSpider(object):

    def __init__(self):
        self.base_url = 'http://www.allitebooks.com/page/{}/'
        self.url = 'http://www.allitebooks.com/'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'
        }
        self.json_path = 'allitebooks.json'
        self.csv_path = 'allitebooks.csv'
        self.book_list = []


    def get_html(self):
        resp = requests.get(self.url, headers = self.headers).content.decode()
        return resp

    def use_bs4_parse_html(self, resp):
        soup = BeautifulSoup(resp, 'lxml')
        items = soup.select('h2.entry-title a')
        for item in items:
            data = {
                'title': item.get_text(),
                'link': item.get('href')
            }
            # print(data)
            self.book_list.append(data)

    def use_lxml_parse_html(self, resp):
        html = etree.HTML(resp)
        titles = html.xpath('//h2/a[@rel="bookmark"]/text()')
        links = html.xpath('//h2/a[@rel="bookmark"]/@href')
        # print(titles, len(titles))
        # print(links, len(links))
        for title, link in zip(titles, links):
            data = {
                'title': title,
                'link': link
            }
            # print(data)
            # self.book_list.append(data)

    def use_re_parse_html(self, resp):
        # <h2 class="entry-title"><a href="http://www.allitebooks.com/building-xamarin-forms-mobile-apps-using-xaml/" rel="bookmark" class="">Building Xamarin.Forms Mobile Apps Using XAML</a></h2>
        pattern = re.compile('<h2 class="entry-title"><a href="(.*?)".*?>(.*?)</a></h2>', re.S)
        results = pattern.findall(resp)
        for item in results:
            data = {
                'title': item[1],
                'link': item[0]
            }
            self.book_list.append(data)

    def save_data_to_json(self):
        with open(self.json_path, 'w') as f:
            json.dump(self.book_list, f)


    def save_data_to_csv(self):
        with open(self.csv_path, 'w') as f:
            writer = csv.writer(f)
            sheet_title = self.book_list[0].keys()
            writer.writerow(sheet_title)
            sheet_data = []
            for book_item in self.book_list:
                sheet_data.append(book_item.values())
            writer.writerows(sheet_data)


    def run_spider(self):
        resp = self.get_html()
        # print('use_re_parse_html'+'\n')
        self.use_re_parse_html(resp)
        print(self.book_list)
        # self.save_data_to_json()
        self.save_data_to_csv()
        # print('use_lxml_parse_html'+'\n')
        # self.use_lxml_parse_html(resp)
        # print('use_bs4_parse_html'+'\n')
        # self.use_bs4_parse_html(resp)


if __name__ == '__main__':
    AllitebooksSpider().run_spider()