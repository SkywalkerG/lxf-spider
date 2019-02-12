import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36',

}
cookies = 'acw_tc=2f624a3915499530483294956e7007d97cc45cd8bd6085d588f50e47704411; PHPSESSID=dflnrc071n69lhsbc83em98po5; _ga=GA1.2.792587635.1549953051; _gid=GA1.2.268250215.1549953051; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; MEIQIA_VISIT_ID=1H4EcmzWjRD4actya2E9ndDXOFh; MEIQIA_EXTRA_TRACK_ID=1H4Ecms0Kw16450pOhzTpK7GXBS; yaozh_userId=691885; _gat=1; yaozh_uidhas=1; yaozh_mylogin=1549953121; acw_tc=2f624a3915499530483294956e7007d97cc45cd8bd6085d588f50e47704411; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; MEIQIA_VISIT_ID=1H4EcmzWjRD4actya2E9ndDXOFh; MEIQIA_EXTRA_TRACK_ID=1H4Ecms0Kw16450pOhzTpK7GXBS; UtzD_f52b_saltkey=bYlYSU3x; UtzD_f52b_lastvisit=1549949524; yaozh_logintime=1549954101; yaozh_user=691885%09gy89676992; db_w_auth=637427%09gy89676992; UtzD_f52b_lastact=1549954102%09uc.php%09; UtzD_f52b_auth=4179cVs3TwDN5EoYQgxB0iZYoXOsSy2ZG2mV1iNqtE8heTH7LOrrVoWJ4%2FBCvJc7azFI34haULVvvdWZ7mBSV9nZwH0'
# cookie_dict = {}
cookie_list = cookies.split('; ')
# for cookie in cookie_list:
#     a,b = cookie.split('=')
#     cookie_dict[a] = b
# 字典推导式
cookie_dict = { cookie.split('=')[0]: cookie.split('=')[1] for cookie in cookie_list}
print(cookie_dict)

