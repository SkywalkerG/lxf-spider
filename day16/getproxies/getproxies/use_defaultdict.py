from collections import defaultdict
import json

proxies = defaultdict(list)
with open('E:\pythonProject\lxf-spider\day16\getproxies\getproxies\spiders\\2019-1-16canuse.json') as f:
    proxy_list = json.load(f)
    for item in proxy_list:
        cate = item['proxy'].split(':')[0]
        ip_port = item['proxy'].split('/')[-1]

        proxies[cate].append(ip_port)


print(proxies)