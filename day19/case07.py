import requests
import re
import json
url = 'https://etherscan.io/searchHandler?term=eos'

r = requests.get(url).content.decode()

for item in eval(r):
    result = re.findall('0x.*\t?', item)[0][:43]
    print(result)