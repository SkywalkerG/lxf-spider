# python 处理 lua 脚本

import requests
from urllib.parse import quote

lua = '''
function main(splash, args)
    local treat = require('treat')
    local response = splash:http_get("http://ww.baidu.com")
        return {
        html = treat.as_string(response.body),
        url = response.url,
        status = response.status
        }
end
'''

url = 'http://192.168.99.100:8050/execute?lua_source=' + quote(lua)

r = requests.get(url)
print(r.text)