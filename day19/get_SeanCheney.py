# 获取简书 SeanCheney 所有文章名和链接

import requests
from lxml import etree
from urllib.parse import urljoin

url = 'https://www.jianshu.com/u/130f76596b02?order_by=shared_at&page=1'
def get_onepage(url):
    headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    html = etree.HTML(r.text)
    titles = html.xpath('//a[@class="title"]/text()')
    links = html.xpath('//a[@class="title"]/@href')
    for title, link in zip(titles, links):
        data = {
                'title':title,
                'link' :urljoin(url, link)
            }
        article_list.append(data)
        print(data)

def get_allpage():
    url_base = 'https://www.jianshu.com/u/130f76596b02?order_by=shared_at&page={}'
    for i in range(1,22):
        url = url_base.format(str(i))
        get_onepage(url)


import csv
def write_to_csv(article_list):
    with open('SeanCheney.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['title', 'link'])
        for i in article_list:
            writer.writerow([i['title'], i['link']])

import json
def write_to_json(article_list):
    with open('SeanCheney.json', 'w') as f:
        f.write(json.dumps(article_list))

if __name__ == '__main__':
    article_list = []
    get_allpage()
    write_to_csv(article_list)
    write_to_json(article_list)