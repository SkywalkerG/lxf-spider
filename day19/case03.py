# python 处理 lua 脚本

import requests
from urllib.parse import quote

lua = '''
function main(splash)
    return 'hello'
end
'''

url = 'http://192.168.99.100:8050/execute?lua_source=' + quote(lua)

r = requests.get(url)
print(r.text)