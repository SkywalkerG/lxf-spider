import requests

url = 'https://passport.mafengwo.cn/login/'
url1 = 'http://www.mafengwo.cn/path/35844003.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
}

data = {
    'passport': '18535703288',
    'password': '8951270o'
}
session = requests.session()

session.post(url, headers=headers, data=data)
r = session.get(url1, headers=headers)
print(r.status_code)
print(r.text)

'''
Qj25lL5P41S3mw7X/9hxM9P/+JQlJbAXGuAV8ZfrQZ4U8BZATOiSc3O6gYX+S+WLhwu4pjruxir6TRh6d/rgjQ==
YVfxSk/+75e71TebdvHqf2UWJeju7f2eP2lt1yXI7qJPryN4bjwZiooDta9SmEcrs6sHoDeaYFNR1Sd7gSwPKw==
2TF8oycwLJ8+j8vJ7wIC+DZNdrj6xVVqzYCseGryiaL3ya6RBvLagg9ZSf3La6+s4PBU8COyyKejPObUzhZoKw==
'''