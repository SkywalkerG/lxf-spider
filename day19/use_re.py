s = '''
{
req: {
data: {
expiration: 86400,
freeflowsip: [
"http://221.204.59.151/amobile.music.tc.qq.com/",
"http://221.204.59.152/amobile.music.tc.qq.com/",
"http://221.204.59.157/amobile.music.tc.qq.com/"
],
keepalivefile: "C400004TsFuW2mZbRR.m4a?guid=7661004004&vkey=56A19ACDAC9218D784A8F372B93FA6ED3EA9E5563F2C5CA8429F1A33B4C2F628E90C144F87230B9CA6FA24666C97035AFB276C49EB8A42BF&uin=0&fromtag=3",
msg: "ok",
retcode: 0,
servercheck: "7d70d26b98f921a205949c6a48cc90be",
sip: [
"http://dl.stream.qqmusic.qq.com/",
"http://isure.stream.qqmusic.qq.com/",
"http://221.204.59.151/amobile.music.tc.qq.com/",
"http://221.204.59.152/amobile.music.tc.qq.com/",
"http://221.204.59.157/amobile.music.tc.qq.com/"
],
testfile2g: "C400003mAan70zUy5O.m4a?guid=7661004004&vkey=27297F5AC52B0D7A807CEB7B8C6B7DDFFD71E7AC3BF0D6E9C8A5AEF850D66EB5A47B388A33323610617BDFFDBA20E34107E48DB3190F4703&uin=0&fromtag=3",
testfilewifi: "C400003mAan70zUy5O.m4a?guid=7661004004&vkey=27297F5AC52B0D7A807CEB7B8C6B7DDFFD71E7AC3BF0D6E9C8A5AEF850D66EB5A47B388A33323610617BDFFDBA20E34107E48DB3190F4703&uin=0&fromtag=3",
uin: "",
userip: "60.221.133.80",
vkey: "D8790848EAF404A0E5CB5BA7B18A1368770C9306D246C73652C2FC8575DDABC357B434A7C63E3E6AD2CDC3E39C175712E45D044ADEE173DE"
},
code: 0
},
req_0: {
data: {
expiration: 80400,
login_key: "",
midurlinfo: [
{
common_downfromtag: 0,
errtype: "",
filename: "C400002E3MtF0IAMMY.m4a",
flowfromtag: "",
flowurl: "",
hisbuy: 0,
hisdown: 0,
isbuy: 0,
isonly: 0,
onecan: 0,
opi128kurl: "",
opi192koggurl: "",
opi192kurl: "",
opi48kurl: "",
opi96kurl: "",
opiflackurl: "",
p2pfromtag: 0,
pdl: 0,
pneed: 0,
pneedbuy: 0,
premain: 0,
purl: "C400002E3MtF0IAMMY.m4a?guid=7661004004&vkey=93E385BE053B5BEAE84B68750281851025082A3B2A82417580BECC0CBEA35C793D2514F9FF1AAC1C28B98E1620FC6611777813B4E55893A7&uin=0&fromtag=66",
qmdlfromtag: 0,
result: 0,
songmid: "002E3MtF0IAMMY",
tips: "",
uiAlert: 0,
vip_downfromtag: 0,
vkey: "93E385BE053B5BEAE84B68750281851025082A3B2A82417580BECC0CBEA35C793D2514F9FF1AAC1C28B98E1620FC6611777813B4E55893A7",
wififromtag: "",
wifiurl: ""
}
],
msg: "",
retcode: 0,
servercheck: "7d70d26b98f921a205949c6a48cc90be",
sip: [
"http://dl.stream.qqmusic.qq.com/",
"http://isure.stream.qqmusic.qq.com/"
],
testfile2g: "C400003mAan70zUy5O.m4a?guid=7661004004&vkey=EFCC15B8293CE01610835E6583C958394878BB388EA93027098CF485310FA9671A0913A66FBCF09D2009A50F4B2BF97BAB8DD4119433FBF8&uin=&fromtag=3",
testfilewifi: "C400003mAan70zUy5O.m4a?guid=7661004004&vkey=EFCC15B8293CE01610835E6583C958394878BB388EA93027098CF485310FA9671A0913A66FBCF09D2009A50F4B2BF97BAB8DD4119433FBF8&uin=&fromtag=3",
thirdip: [
"",
""
],
uin: "",
verify_type: 0
},
code: 0
},
code: 0,
ts: 1550387641833
}
'''
import re
result = re.search('purl: "(.*?)"', s, re.S)
print(result.group(1))

re.sub(r'[\s+|@<>:\\"/]','',music_name)