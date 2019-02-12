import requests
'''
模拟登陆百度  失败
'''
url = 'https://tieba.baidu.com/index.html'
login_url = 'https://passport.baidu.com/v2/api/?login'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36',
}
form_data = {
    'username': '327635390',
    'password': '8951270o'
}
session = requests.session()
session.post(login_url, headers=headers, data=form_data)
r = session.get(url, headers=headers)
with open('tieba.html', 'w', encoding='utf-8') as f:
    f.write(r.content.decode())

