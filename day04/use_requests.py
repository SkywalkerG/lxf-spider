import requests

params = {
    'wd': '狗'
}
resp = requests.get('http://www.baidu.com/s', params=params)
print(resp.url)
# resp,text 为str 字符串
print(type(resp.text))
# resp.content 为2进制 就是bytes
print(type(resp.content))
print(resp.encoding)
print(resp.apparent_encoding)