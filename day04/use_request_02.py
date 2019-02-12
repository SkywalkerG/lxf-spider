import requests


class RequestsSpider(object):
    def __init__(self):
        self.url = 'http://www.baidu.com'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'
        }
        self.resp = requests.get(url = self.url, headers = self.headers)

    def parse(self):
        html = self.resp.content
        # 获取请求头
        # print(self.resp.request.headers)
        # 获取响应头
        # print(self.resp.headers)
        # 响应状态码
        # print(self.resp.status_code)
        # 请求的cookie
        print(self.resp.request._cookies)
        # 响应的cookie
        print(self.resp.cookies)



RequestsSpider().parse()