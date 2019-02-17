import requests
import json
from lxml import etree
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def get_links_and_id_use_selenium():
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome()
    url = 'https://y.qq.com/n/yqq/toplist/26.html'
    timeout = 5
    driver.get(url)
    links = WebDriverWait(driver, timeout).until(
        lambda d:d.find_elements_by_class_name('js_song')
    )

    for link in links :
        music_id = link.get_attribute('href').split('/')[-1].split('.')[0]
        music_title = link.get_attribute('title')
        music_list.append({
            'music_id': music_id,
            'music_title': music_title
        })
    driver.close()
def get_links_and_id_use_ajax():
    url = 'https://c.y.qq.com/v8/fcg-bin/fcg_v8_toplist_cp.fcg?tpl=3&page=detail&date=2019_06&topid=26&type=top&song_begin=0&song_num=30&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'

    r = requests.get(url).content.decode()
    songlist = json.loads(r)['songlist']
    for song in songlist:
        print(song['data']['songmid'])
        print(song['data']['songname'])
        print('和'.join([i['name'] for i in song['data']['singer']]))

def get_download_link(music_name ,music_id):

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Origin': 'https://y.qq.com',
        'Referer': 'https://y.qq.com/portal/player.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
    }
    # url + param 不好用。。。。url里面会带加号
    # url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?'

    # parmas = {
    #     '-': 'getplaysongvkey8961925220406175',
    #     'g_tk': 5381,
    #     'loginUin': 0,
    #     'hostUin': 0,
    #     'format': 'json',
    #     'inCharset': 'utf8',
    #     'outCharset': 'utf-8',
    #     'notice': 0,
    #     'platform': 'yqq.json',
    #     'needNewCode': 0,
    #     'data': json.dumps({"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch","param":{"guid":"7661004004","calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"7661004004","songmid":[music_id],"songtype":[0],"uin":"0","loginflag":1,"platform":"20"}},"comm":{"uin":0,"format":"json","ct":24,"cv":0}})
    # }
    data = json.dumps({"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch","param":{"guid":"7661004004","calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"7661004004","songmid":[music_id],"songtype":[0],"uin":"0","loginflag":1,"platform":"20"}},"comm":{"uin":0,"format":"json","ct":24,"cv":0}})
    url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?-=getplaysongvkey8961925220406175&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data={}'.format(data)

    r = requests.get(url, headers=headers).content.decode()
    domain = json.loads(r)['req']['data']['sip'][0]
    end_link = json.loads(r)['req_0']['data']['midurlinfo'][0]['purl']

    print(music_name)
    print(domain + end_link)


if __name__ == '__main__':
    music_list = []
    # get_links_and_id_use_selenium()
    get_links_and_id_use_ajax()
    # for item in music_list:
    #     music_id = item['music_id']
    #     music_title = item['music_title']
    #     get_download_link(music_title, music_id)


'''
http://221.204.62.16/amobile.music.tc.qq.com/C400002E3MtF0IAMMY.m4a?guid=7661004004&vkey=431372E3D0E3DDF95A5C9CAA60E0786A0C6D95A0EE58D3021D042D70429762B221D7D3238814A9588E8BBEB39157CB2FDE1A22CDD506C9DA&uin=0&fromtag=66
http://221.204.62.16/amobile.music.tc.qq.com/C400002E3MtF0IAMMY.m4a?guid=7661004004&vkey=8F8336ED7E36968B1D77DBAF4AD0C22D28AA18572313E6469D15DD3DBDCAF7B0BAB089C7D0EDC71BCBC374D9AA63DD42757F5AF8DD1DC44D&uin=0&fromtag=66
8F8336ED7E36968B1D77DBAF4AD0C22D28AA18572313E6469D15DD3DBDCAF7B0BAB089C7D0EDC71BCBC374D9AA63DD42757F5AF8DD1DC44D

'''
'''
正确的
https://u.y.qq.com/cgi-bin/musicu.fcg?-=getplaysongvkey8961925220406175&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&
'''
'''
错误的
https://u.y.qq.com/cgi-bin/musicu.fcg?-=getplaysongvkey8961925220406175&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22req%22%3A+%7B%22module%22%3A+%22CDN.SrfCdnDispatchServer%22%2C+%22method%22%3A+%22GetCdnDispatch%22%2C+%22param%22%3A+%7B%22guid%22%3A+%227661004004%22%2C+%22calltype%22%3A+0%2C+%22userip%22%3A+%22%22%7D%7D%2C+%22req_0%22%3A+%7B%22module%22%3A+%22vkey.GetVkeyServer%22%2C+%22method%22%3A+%22CgiGetVkey%22%2C+%22param%22%3A+%7B%22guid%22%3A+%227661004004%22%2C+%22songmid%22%3A+%5B%22002E3MtF0IAMMY%22%5D%2C+%22songtype%22%3A+%5B0%5D%2C+%22uin%22%3A+%220%22%2C+%22loginflag%22%3A+1%2C+%22platform%22%3A+%2220%22%7D%7D%2C+%22comm%22%3A+%7B%22uin%22%3A+0%2C+%22format%22%3A+%22json%22%2C+%22ct%22%3A+24%2C+%22cv%22%3A+0%7D%7D
'''
'''
http://isure.stream.qqmusic.qq.com/C400002E3MtF0IAMMY.m4a?guid=7661004004&vkey=14E07371252DB746D7453B083640169AE6F6886FFAC6B5F6322DC2CC2325B8AC64271AF25C2613E2A05B1E565D859094101BEABC6C164EB1&uin=0&fromtag=66
http://isure.stream.qqmusic.qq.com/C400004TsFuW2mZbRR.m4a?guid=7661004004&vkey=56A19ACDAC9218D784A8F372B93FA6ED3EA9E5563F2C5CA8429F1A33B4C2F628E90C144F87230B9CA6FA24666C97035AFB276C49EB8A42BF&uin=0&fromtag=66
'''