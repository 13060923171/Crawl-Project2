import requests
import re
from urllib import parse

keyword = parse.quote(input("请输入你需要搜索的关键词:"))
headers = {
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-requested-with": "XMLHttpRequest",
    "referer": "https://so.dajie.com/job/search?keyword={}&from=job&clicktype=blank".format(keyword),
    'cookie': 'DJ_RF=https%3A%2F%2Fwww.google.com%2F; DJ_EU=http%3A%2F%2Fwww.dajie.com%2F; DJ_UVID=MTU5NzMyNzYzNjYxODExNTQw; Hm_lvt_6822a51ffa95d58bbe562e877f743b4f=1597327635; _ga=GA1.2.2113787223.1597327635; _gid=GA1.2.1553008633.1597327635; USER_ACTION="request^A-^A-^Ajobdetail:^A-"; MEIQIA_TRACK_ID=1g2znXAAakoQxBn9cSd2boCOxHN; MEIQIA_VISIT_ID=1g307zmD0usHANNftgWsM3Eof2J; _close_autoreg=1597327844276; _close_autoreg_num=4; Hm_lpvt_6822a51ffa95d58bbe562e877f743b4f=1597327891; SO_COOKIE_V2=fdd5K4X11FqT4QuFRF5nToN93sSFBOWW16eUsGyS5RKwPL7ibzT2tqeTuSUaPyOhYM5cz62PL0Q9UGBMvKuu4Z2RBdTR/keQQizP',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
}
def get_parse(url):
    html = requests.get(url,headers =headers)
    if html.status_code ==200:
        get_html(html)
    else:
        print(html.status_code)

def get_html(html):
    content = html.text
    print(content)

if __name__ == '__main__':
    for i in range(1,2,1):
        url = "https://so.dajie.com/job/ajax/search/filter?keyword={}&order=0&city=&recruitType=&salary=&experience=&page=1&positionFunction=&_CSRFToken=&ajax={}".format(keyword,i)
        get_parse(url)