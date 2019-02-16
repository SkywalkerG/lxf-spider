# -*- coding: utf-8 -*-
import scrapy
import json

class XiciSpider(scrapy.Spider):
    name = 'xici'
    allowed_domains = ['www.xicidaili.com', 'httpbin.org']
    start_urls = ['https://www.xicidaili.com/nn/']

    def parse(self, response):
        print(response.status)
        # //*[@id="ip_list"]/tbody/tr[1]
        trs = response.xpath('//tr')
        for tr in trs[1:]:
            cate = tr.xpath('.//td[6]/text()').get()
            if self.isHTTPorHTTPS(cate):
                ip = tr.xpath('.//td[2]/text()').get()
                port = tr.xpath('.//td[3]/text()').get()
                cate = cate.lower()
                proxy_ip = cate + "://" + ip + ":" + port
                httporhttpsbin = cate + "://www.httpbin.org/ip"
                meta = {
                    'download_timeout': 10,
                    'dont_retry': True,
                    'proxy': proxy_ip,
                    'ip': ip,
                    'port': port,
                    'cate': cate
                }
                # print(proxy_ip)
                yield response.follow(url = httporhttpsbin, callback = self.check_available, meta= meta, dont_filter=True)


    def check_available(self, response):
        print(response.text)
        yield {
            'proxy': response.meta['proxy']
        }
        # ip = response.meta['ip']
        # port = response.meta['port']
        # cate = response.meta['cate']
        # response_ip = json.loads(response.text)['origin']
        # if ip == response_ip:
        #     print('success')
        #     yield {
        #         'ip': ip,
        #         'port': port,
        #         'cate': cate
        #     }

    def isHTTPorHTTPS(self, cate):
        if cate:
            if cate == 'HTTP' or cate == 'HTTPS':
                return True
