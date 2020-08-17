import requests
import re
import json
from urllib import parse


headers = {
    "Origin": "https://bj.meituan.com",
    "Host": "apimobile.meituan.com",
    "Referer": "https://bj.meituan.com/s/%E7%81%AB%E9%94%85/",
    "Cookie": "uuid=692a53319ce54d0c91f3.1597223761.1.0.0; ci=1; rvct=1; _lxsdk_cuid=173e1f47707c8-0dcd4ff30b4ae3-3323765-e1000-173e1f47707c8; _lxsdk_s=173e1f47708-21d-287-4d9%7C%7C35",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}

def get_parse(url):
    html = requests.get(url,headers = headers)
    if html.status_code:
        get_html(html)
    else:
        print(html.status_code)

def get_html(html):

    content = html.text
    #店名
    titles= re.compile('","title":"(.*?)",',re.S|re.I)
    title = titles.findall(content)
    #地址
    addresses = re.compile(',"address":"(.*?)",', re.S | re.I)
    address = addresses.findall(content)
    #评分
    avgscores = re.compile(',"avgscore":(.*?),', re.S | re.I)
    avgscore = avgscores.findall(content)
    #评价人数
    commentses = re.compile(',"comments":(.*?),', re.S | re.I)
    comments = commentses.findall(content)
    #联系电话
    phones = re.compile('"phone":"(.*?)",', re.S | re.I)
    phone = phones.findall(content)
    for i in range(len(title)):
        try:
            t = title[i]
            a = address[i]
            avg = avgscore[i]
            c = comments[i]
            p = phone[i]
            print(t,a,avg,c,p)
            dowload(t,a,avg,c,p)
        except:
            pass

def dowload(t,a,avg,c,p):
    data = {
        '店铺名称': t,
        '店铺地址': a,
        '店铺评分': avg,
        '评价人数': c,
        '电话': p
    }
    with open("美团信息.txt","a+",encoding="utf-8")as f:
        f.write(json.dumps(data,ensure_ascii=False)+"\n")
        print("写入成功")
if __name__ == '__main__':
    #在这个URL里面offse参数每次翻页增加32，limit参数是一次请求的数据量，q是搜索关键词poi/pcsearch/1？其中的1是北京城市的id编号。
    for i in range(0,33,32):
        url = "https://apimobile.meituan.com/group/v4/poi/pcsearch/1?uuid=692a53319ce54d0c91f3.1597223761.1.0.0&userid=-1&limit=32&offset={}&cateId=-1&q=%E7%81%AB%E9%94%85".format(i)
        get_parse(url)