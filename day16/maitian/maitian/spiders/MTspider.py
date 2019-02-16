# -*- coding: utf-8 -*-
import scrapy
from maitian.items import MaitianItem
from scrapy.loader import ItemLoader


class MtSpider(scrapy.Spider):
    name = 'mt'
    allowed_domains = ['bj.maitian.cn']
    # start_urls = ['http://bj.maitian.cn/esfall/PG1',
    #  'http://bj.maitian.cn/esfall/PG2',
    #  'http://bj.maitian.cn/esfall/PG3',
    #  'http://bj.maitian.cn/esfall/PG4',
    #  'http://bj.maitian.cn/esfall/PG5']
    # start_urls = ['http://bj.maitian.cn/esfall']
    start_urls = ['http://bj.maitian.cn/esfall/PG{}'.format(str(i)) for i in range(1,101)]

    def parse(self, response):
        items = response.xpath('//div[@class="list_title"]')
        for item in items:
            title = item.xpath('..//h1/a/text()').get()
            link = response.urljoin(item.xpath('..//h1/a/@href').get())
            price = item.xpath('..//div[@class="the_price"]//span/text()').get()
            single_price = item.xpath('..//div[@class="the_price"]//ol/text()').get().split('元')[0]
            location = item.xpath('..//p/text()').get().strip().split(']')[0][1:]
            # /html/body/section[2]/div[2]/div[2]/ul/li[8]/div[2]/p/span[1]
            area = item.xpath('..//p/span[1]/text()').get()
            data = {
                'title': title,
                'link': link,
                'price': price,
                'single_price': int(single_price),
                'location': location,
                'area': eval(area)
            }
            yield data
            # l = ItemLoader(item=MaitianItem(), response=response)
            # l.add_xpath('title', '..//h1/a/text()')
            # l.add_xpath('price', '..//div[@class="the_price"]//span/text()')
            # l.add_xpath('disrict','..//div[@class="the_price"]//ol/text()')
            # l._add_value('area', location)
            # return l.load_item()
        # next_page = response.xpath('//a[@class="down_page"]/@href')
        # if next_page is not None:
        #     yield response.follow(next_page, callback = self.parse)