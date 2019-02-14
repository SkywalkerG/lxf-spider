import requests
from bs4 import BeautifulSoup
from lxml import etree
# from faker import Faker

# fake = Faker(locale="zh-CN")
headers = {
	'user-agent' : 'Opera/9.82.(X11; Linux x86_64; iw-IL) Presto/2.9.183 Version/10.00'
}

url_base = 'http://bj.ganji.com'

def parse_index():
	url = 'http://bj.ganji.com/wu/'
	r = requests.get(url, headers=headers).content.decode()
	html = etree.HTML(r)
	links = html.xpath('//dl[@class="fenlei"]/dt/a/@href')
	fenlei_link = [url_base + i for i in links]
	return fenlei_link

def parse_fenlei(fenlei_link):
	all_links = []
	for link in fenlei_link:
		r = requests.get(link, headers=headers).content.decode()
		html = etree.HTML(r)
		links = html.xpath('//dd[@class="w-short"]/a/@href')
		for i in links[1:]:
			cate_links = url_base + i + 'allcity/'
			all_links.append(cate_links)

	return all_links


if __name__ == '__main__':
	fenlei_link = parse_index()
	all_links = parse_fenlei(fenlei_link)
	for i in all_links:
		print(i)

channel_extract = '''
http://bj.ganji.com/chuangdian/allcity/
http://bj.ganji.com/chuangdianzi/allcity/
http://bj.ganji.com/shafachaji/allcity/
http://bj.ganji.com/zhuoyi/allcity/
http://bj.ganji.com/yizi/allcity/
http://bj.ganji.com/guizi/allcity/
http://bj.ganji.com/jiazi/allcity/
http://bj.ganji.com/jingzi/allcity/
http://bj.ganji.com/bangongjiaju/z1/allcity/
http://bj.ganji.com/qitajiaju/allcity/
http://bj.ganji.com/chuangshangyongpin/allcity/
http://bj.ganji.com/gerenyongpin/allcity/
http://bj.ganji.com/anmobaojian/allcity/
http://bj.ganji.com/xiyiyuntang/allcity/
http://bj.ganji.com/weiyu/allcity/
http://bj.ganji.com/zhuangshibaishe/allcity/
http://bj.ganji.com/chuweiyongpin/z1/allcity/
http://bj.ganji.com/jingzi/z1/allcity/
http://bj.ganji.com/shoubiao/z1/allcity/
http://bj.ganji.com/qitariyongpin/allcity/
http://bj.ganji.com/iphone/allcity/
http://bj.ganji.com/mi/allcity/
http://bj.ganji.com/huawei/allcity/
http://bj.ganji.com/sanxingshouji/allcity/
http://bj.ganji.com/oppo/allcity/
http://bj.ganji.com/lianxiangshouji/allcity/
http://bj.ganji.com/bbk/allcity/
http://bj.ganji.com/coolpad/allcity/
http://bj.ganji.com/meizu/allcity/
http://bj.ganji.com/zte/allcity/
http://bj.ganji.com/nubia/allcity/
http://bj.ganji.com/lgshouji/allcity/
http://bj.ganji.com/htc/allcity/
http://bj.ganji.com/nokia/allcity/
http://bj.ganji.com/suoniailixin/allcity/
http://bj.ganji.com/motorola/allcity/
http://bj.ganji.com/shoujipeijian/allcity/
http://bj.ganji.com/bangongjiaju/allcity/
http://bj.ganji.com/zhanguihuojia/allcity/
http://bj.ganji.com/haocai/allcity/
http://bj.ganji.com/dianhuatongxun/allcity/
http://bj.ganji.com/shangyongdiannao/z1/allcity/
http://bj.ganji.com/meirongmeifayongpin/z1/allcity/
http://bj.ganji.com/wujingongju/allcity/
http://bj.ganji.com/nongyongjixie/z1/allcity/
http://bj.ganji.com/tiyujianshensheshi/allcity/
http://bj.ganji.com/qitabangong/allcity/
http://bj.ganji.com/bangong/allcity/
http://bj.ganji.com/bangong/n100/allcity/
http://bj.ganji.com/bangong/n99/allcity/
http://bj.ganji.com/bangong/n95/allcity/
http://bj.ganji.com/bangong/n90/allcity/
http://bj.ganji.com/bangong/n80/allcity/
http://bj.ganji.com/bangong/n69/allcity/
http://bj.ganji.com/miaomu/allcity/
http://bj.ganji.com/zhongzi/allcity/
http://bj.ganji.com/feiliao/allcity/
http://bj.ganji.com/nongyongjixie/allcity/
http://bj.ganji.com/guangaidapeng/allcity/
http://bj.ganji.com/jiachujiaqin/allcity/
http://bj.ganji.com/siliao/allcity/
http://bj.ganji.com/shucaishuiguo/allcity/
http://bj.ganji.com/roudanshuichan/allcity/
http://bj.ganji.com/qitanongyongpin/allcity/
http://bj.ganji.com/nongyongpin/allcity/
http://bj.ganji.com/nongyongpin/n100/allcity/
http://bj.ganji.com/nongyongpin/n99/allcity/
http://bj.ganji.com/nongyongpin/n95/allcity/
http://bj.ganji.com/nongyongpin/n90/allcity/
http://bj.ganji.com/nongyongpin/n80/allcity/
http://bj.ganji.com/nongyongpin/n69/allcity/
http://bj.ganji.com/dajiadian/allcity/
http://bj.ganji.com/xiaoxingdianqi/allcity/
http://bj.ganji.com/kongdiaozhileng/allcity/
http://bj.ganji.com/yingyinjiadian/allcity/
http://bj.ganji.com/chuweiyongpin/allcity/
http://bj.ganji.com/qitadianqi/allcity/
http://bj.ganji.com/bijibendiannao/allcity/
http://bj.ganji.com/pingbandiannao/z1/allcity/
http://bj.ganji.com/bijibenyingjian/allcity/
http://bj.ganji.com/pingbandiannaopeijian/allcity/
http://bj.ganji.com/tushu/allcity/
http://bj.ganji.com/yinxiang/allcity/
http://bj.ganji.com/yueqi/allcity/
http://bj.ganji.com/yundongqicai/allcity/
http://bj.ganji.com/yunfuyongpin/allcity/
http://bj.ganji.com/yingyouyongpin/allcity/
http://bj.ganji.com/ertongyongpin/allcity/
http://bj.ganji.com/taishidiannaozhengji/allcity/
http://bj.ganji.com/yitiji/allcity/
http://bj.ganji.com/diannaoyingjian/allcity/
http://bj.ganji.com/diannaowaishe/allcity/
http://bj.ganji.com/wangluoshebei/allcity/
http://bj.ganji.com/shangwangkuandai/allcity/
http://bj.ganji.com/shangyongdiannao/allcity/
http://bj.ganji.com/zibubaojian/z1/allcity/
http://bj.ganji.com/shipinliangyou/z1/allcity/
http://bj.ganji.com/jiu/z1/allcity/
http://bj.ganji.com/chaye/z1/allcity/
http://bj.ganji.com/bawanwujian/z1/allcity/
http://bj.ganji.com/gongyipin/z1/allcity/
http://bj.ganji.com/kalei/allcity/
http://bj.ganji.com/shoubiao/z3/allcity/
http://bj.ganji.com/qitalipinzhuanrang/allcity/
http://bj.ganji.com/xianzhilipin/allcity/
http://bj.ganji.com/xianzhilipin/n100/allcity/
http://bj.ganji.com/xianzhilipin/n99/allcity/
http://bj.ganji.com/xianzhilipin/n95/allcity/
http://bj.ganji.com/xianzhilipin/n90/allcity/
http://bj.ganji.com/xianzhilipin/n80/allcity/
http://bj.ganji.com/xianzhilipin/n69/allcity/
http://bj.ganji.com/fushi/allcity/
http://bj.ganji.com/xiangbao/allcity/
http://bj.ganji.com/xuemao/allcity/
http://bj.ganji.com/shoubiao/allcity/
http://bj.ganji.com/peishi/allcity/
http://bj.ganji.com/shipin/allcity/
http://bj.ganji.com/shuiyineiyi/allcity/
http://bj.ganji.com/qitafushixiaobaxuemao/allcity/
http://bj.ganji.com/hufupin/allcity/
http://bj.ganji.com/huazhuangpin/allcity/
http://bj.ganji.com/meirongmeifayongpin/allcity/
http://bj.ganji.com/meijiayongpin/allcity/
http://bj.ganji.com/qitameironghuazhuang/allcity/
http://bj.ganji.com/shumaxiangji/allcity/
http://bj.ganji.com/shumashexiangji/allcity/
http://bj.ganji.com/pingbandiannao/allcity/
http://bj.ganji.com/suishenting/allcity/
http://bj.ganji.com/youxiji/allcity/
http://bj.ganji.com/qitashuma/allcity/
http://bj.ganji.com/anmobaojian/z1/allcity/
http://bj.ganji.com/zibubaojian/z2/allcity/
http://bj.ganji.com/bawanwujian/allcity/
http://bj.ganji.com/zhanghaozhuangbei/allcity/
http://bj.ganji.com/chongzhidianka/allcity/
http://bj.ganji.com/qqhao/z1/allcity/
http://bj.ganji.com/qitaxuniwupin/allcity/
'''