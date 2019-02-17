import requests

data = {
    'name': 'author',
    'age': 2
}
url = 'http://httpbin.org/post'

r = requests.post(url, data = data)
print(r.url)
print(r.text)