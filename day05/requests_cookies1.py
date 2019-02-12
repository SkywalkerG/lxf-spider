import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36',
}
login_url = 'https://www.yaozh.com/login'
form_data = {
    'username': 'gy89676992',
    'pwd': '8951270o',
    'formhash': '58F6BFE9A2',
    'backurl': 'https%3A%2F%2Fwww.yaozh.com%2F'

}

# session 可以自动保存cookie === cookiesJar
session = requests.session()
session.post(login_url, headers=headers, data = form_data, verify = False)

url = 'https://www.yaozh.com/member/'
# resp = session.get(url, headers=headers).content.decode()
print(session.cookies)
# with open('yaozhi.html', 'w', encoding='utf-8') as f:
#     f.write(resp)