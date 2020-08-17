import requests
import re
from lxml import etree
from urllib import parse
import time
import random
from tqdm import tqdm
from bs4 import BeautifulSoup
headers = {
    "Cookie": "BAIDUID=D69331E6E1E87361E4D2CF7D29C6F88F:FG=1; cflag=13%3A3; BDUSS=pZU21UZTB3ZDZqfnVkdll1RXlJM25NaFpZc2poUGg4cDJod1hkcC1uUGZ2RTlmRVFBQUFBJCQAAAAAAAAAAAEAAAAIy~xb09DDqMTl0f3f9wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN8vKF~fLyhfLX; BDUSS_BFESS=pZU21UZTB3ZDZqfnVkdll1RXlJM25NaFpZc2poUGg4cDJod1hkcC1uUGZ2RTlmRVFBQUFBJCQAAAAAAAAAAAEAAAAIy~xb09DDqMTl0f3f9wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN8vKF~fLyhfLX; TIEBA_USERTYPE=e505b528fbde41505f23f7c8; STOKEN=a5508f08d097646a778c21658e3987cb5902f51f62473da6201df6272fd0dad8; TIEBAUID=cd4907611a79bbddb5ca5bd8; BIDUPSID=D69331E6E1E87361E4D2CF7D29C6F88F; PSTM=1596697528; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1596527801,1596530614,1596531175,1597031432; st_key_id=17; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1597031455; 1543293704_FRSVideoUploadTip=1; st_data=0a5883fb0fc699bffc73f684ec144c86f6a7ff72bc982a3d9b893cfdf71c85067afc10846c0578b3a2d3cf7a39cf6fce0a7d94c8c058483b6d3aad1ea0d3b28e8d6e0dc7d57bedf1678ca25f934650085b71636edfd764fb76bc2130551236aa32b797479da33a2d3a5a33fe2232a3fcf6de1c7d40e23987a568a025614488ed; st_sign=470808a4",
    "Host": "tieba.baidu.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}
session = requests.session()
session.headers = headers
def get_parse(url):
    html = session.get(url)
    if html.status_code ==200:
        print(html.status_code)
        get_html(html)
    else:
        print(html.status_code)
def get_html(html):
    content = html.text
    soup  = etree.HTML(content)
    href = soup.xpath('//span[@class="p_title"]/a/@href')
    for h in href:
        url = parse.urljoin("https://tieba.baidu.com",h)
        get_pinglin(url)
def get_pinglin(url):
    list = []
    list.append(url)
    get_neirong(list)

def get_neirong(list):
    new = []
    #传入列表里面的URL
    for i in list:
        r = session.get(i)
        soup = BeautifulSoup(r.text, 'lxml')
        #获取每一个贴里面每一页的楼层回复的内容
        div = soup.find_all('div',class_ = 'd_post_content j_d_post_content')
        #把这些内容一个个写入一个列表里面
        for name in div:
            new.append(name.text.strip())
        #最后将获取到的内容写入txt文本里面
    with open("301医院.txt",'a+', encoding='utf-8') as f:
        for i in range(len(new)):
            f.write(new[i])
            f.write('\n')
            print("写入成功")

if __name__ == '__main__':
    for i in tqdm(range(1,77,1)):
        url = "https://tieba.baidu.com/f/search/res?isnew=1&kw=&qw=301%D2%BD%D4%BA&rn=10&un=&only_thread=0&sm=1&sd=&ed=&pn={}".format(i)
        get_parse(url)