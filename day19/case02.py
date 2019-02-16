# 抓取 我不是药神 的豆瓣评论

import csv
import time
import requests
from lxml import etree

# fw = open('douban_comments.csv', 'w')
# writer = csv.writer()
# writer.writerow(['comment_time','comment_content'])

url = 'https://movie.douban.com/subject/26752088/comments?start=0&limit=20'
# url = 'http://192.168.99.100:8050/render.html?url=https://movie.douban.com/subject/26752088/comments?start=0&limit=20'
r = requests.get(url).content.decode()
html = etree.HTML(r)

comments = html.xpath('//div[@class="comment"]')
for comment in comments:
    pub_time = comment.xpath('.//span[@class="comment-time "]/@title')[0]
    #  字符串 转 时间戳
    comment_time = int(time.mktime(time.strptime(pub_time, '%Y-%m-%d %H:%M:%S')))
    comment_content = comment.xpath('.//span[@class="short"]/text()')[0]
    print(comment_time)