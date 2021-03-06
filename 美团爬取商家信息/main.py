import requests
import re
import json
from urllib import parse
import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns
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
    # 人均消费
    df = pd.DataFrame()
    df['店名'] = title
    df['地址'] = address
    df['评分'] = avgscore
    df['评价人数'] = comments
    df['联系电话'] = phone

    df = df.drop_duplicates()
    df = df.fillna('暂无数据')
    cut = lambda x:'一般' if x<=3.5 else('不错' if x <=4.0 else("好" if x <=4.5 else "很好"))
    df["评分类型"] = df['评分'].map(cut)
    try:
        df.to_csv("火锅信息.csv", mode="a+", header=None, index=None)
        print("写入成功")
    except:
        print("当页数据写入失败")
    time.sleep(1)
    # #设置加载的字体名
    # plt.rcParams['font.sans-serif'] = ['SimHei']
    # #解放保存图像是负号"-"显示为方块的问题
    # plt.rcParams['axes.unicode_minus'] = False
    # fig,axes = plt.subplots(2,1,figsize=(12,12))
    # sns.regplot(x= "人均消费",y = "评分",data = df,color='r',marker="+",ax = axes[0])
    # sns.regplot(x="评价人数", y="评分", data=df, color='g', marker="*", ax=axes[1])


if __name__ == '__main__':
    #在这个URL里面offse参数每次翻页增加32，limit参数是一次请求的数据量，q是搜索关键词poi/pcsearch/1？其中的1是北京城市的id编号。
    for i in range(0,33,32):
        url = "https://apimobile.meituan.com/group/v4/poi/pcsearch/1?uuid=692a53319ce54d0c91f3.1597223761.1.0.0&userid=-1&limit=32&offset={}&cateId=-1&q=%E7%81%AB%E9%94%85".format(i)
        get_parse(url)