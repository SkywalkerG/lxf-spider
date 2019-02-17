# AJAX 当当

import requests
import json
from lxml import etree
# from faker import Faker

# fake = Faker()
# user_agent = fake.user_agent()
urls = 'http://product.dangdang.com/index.php?r=comment%2Flist&productId=26445135&categoryPath=01.21.01.01.00.00&mainProductId=26445135&mediumId=0&pageIndex={}&sortType=1&filterType=1&isSystem=1&tagId=0&tagFilterCount=0&template=publish&long_or_short=short'

# url = 'http://product.dangdang.com/index.php?r=comment%2Flist&productId=26445135&categoryPath=01.21.01.01.00.00&mainProductId=26445135&mediumId=0&pageIndex=2&sortType=1&filterType=1&isSystem=1&tagId=0&tagFilterCount=0&template=publish&long_or_short=short'

url = 'https://api.jinse.com/v4/live/list?limit=20&reading=false&source=web'
headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/3.1)'
}
def get_comment(url):
    r = requests.get(url, headers=headers).content.decode()
    html = etree.HTML(json.loads(r)['data']['list']['html'])
    comment_list = html.xpath('//div[@class="items_right"]')
    for comment in comment_list:
        comment_content = comment.xpath('.//div[@class="describe_detail"]/span/a/text()')[0]
        comment_grade = comment.xpath('.//div[@class="pinglun"]/em/text()')[0]
        print(comment_content, comment_grade)

if __name__ == '__main__':
    for i in range(1, 11):
        url = urls.format(str(i))
        get_comment(url)