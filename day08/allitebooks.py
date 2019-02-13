import requests
from bs4 import BeautifulSoup
from lxml import etree
import re
import json
import csv



class AllitebooksSpider(object):

    def __init__(self):
        self.base_url = 'http://www.allitebooks.com/page/{}/'
        self.urls = [self.base_url.format(str(i)) for i in range(1,2)]
        self.url = 'http://www.allitebooks.com/'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'
        }
        self.json_path = 'allitebooks.json'
        self.csv_path = 'allitebooks.csv'
        self.book_list = []


    def get_html(self, url):
        resp = requests.get(url, headers = self.headers).content.decode()
        return resp

    def use_bs4_parse_html(self, resp):
        soup = BeautifulSoup(resp, 'lxml')
        items = soup.select('h2.entry-title a')
        authors = soup.select('.entry-author')
        descriptions = soup.select('.entry-summary p')

        # for author in authors:
        #     print(author.get_text()[3:]) # Hans-Jürgen Schönig, Zoltan Böszörmenyi
        # #     print(list(i for i in author.stripped_strings if len(i) > 3))
        for item, author, description in zip(items, authors, descriptions):
            data = {
                'title': item.get_text(),
                'link': item.get('href'),
                'author': list(i for i in author.stripped_strings if len(i) > 3),
                'description': description.get_text()
            }
            print(data)
            self.book_list.append(data)

    def use_lxml_parse_html(self, resp):
        html = etree.HTML(resp)
        for book in html.xpath('//article'):
            author = book.xpath('.//h5[@class="entry-author"]/a/text()')
            print(author) # ['Hans-Jürgen Schönig', 'Zoltan Böszörmenyi']
        # titles = html.xpath('//h2/a[@rel="bookmark"]/text()')
        # links = html.xpath('//h2/a[@rel="bookmark"]/@href')
        # authors = html.xpath('//article//h5[@class="entry-author"]//a/text()')
        # descriptions = html.xpath('//div[@class="entry-summary"]/p/text()')
        # imags_urls = html.xpath('//img/@src')
        # print(titles, len(titles))
        # print(links, len(links))
        # print(authors, len(authors))
        # print(descriptions, len(descriptions))
        # print(imags_urls, len(imags_urls))
        # for title, link, author, description in zip(titles, links, authors, descriptions):
        #     data = {
        #         'title': title,
        #         'link': link,
        #         'author': author,
        #         'description': description
        #     }
            # print(data)
            # self.book_list.append(data)

    def use_re_parse_html(self, resp):
        # <h2 class="entry-title"><a href="http://www.allitebooks.com/building-xamarin-forms-mobile-apps-using-xaml/" rel="bookmark" class="">Building Xamarin.Forms Mobile Apps Using XAML</a></h2>
        pattern = re.compile('<div class="entry-body">.*?<h2 class="entry-title"><a href="(.*?)".*?>(.*?)</a></h2>', re.S)
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
        for url in self.urls:
            resp = self.get_html(url)
            # print('use_re_parse_html'+'\n')
            self.use_lxml_parse_html(resp)
            # print(self.book_list)
        # self.save_data_to_json()
            # self.save_data_to_csv()
            # print('use_lxml_parse_html'+'\n')
            # self.use_lxml_parse_html(resp)
            # print('use_bs4_parse_html'+'\n')
            # self.use_bs4_parse_html(resp)


if __name__ == '__main__':
    AllitebooksSpider().run_spider()