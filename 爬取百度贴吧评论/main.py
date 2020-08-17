import requests
import re
from bs4 import BeautifulSoup
import time
import random
from tqdm import tqdm
headers = {
    "Cookie": "BAIDUID=D69331E6E1E87361E4D2CF7D29C6F88F:FG=1; cflag=13%3A3; BDUSS=pZU21UZTB3ZDZqfnVkdll1RXlJM25NaFpZc2poUGg4cDJod1hkcC1uUGZ2RTlmRVFBQUFBJCQAAAAAAAAAAAEAAAAIy~xb09DDqMTl0f3f9wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN8vKF~fLyhfLX; BDUSS_BFESS=pZU21UZTB3ZDZqfnVkdll1RXlJM25NaFpZc2poUGg4cDJod1hkcC1uUGZ2RTlmRVFBQUFBJCQAAAAAAAAAAAEAAAAIy~xb09DDqMTl0f3f9wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN8vKF~fLyhfLX; TIEBA_USERTYPE=e505b528fbde41505f23f7c8; STOKEN=a5508f08d097646a778c21658e3987cb5902f51f62473da6201df6272fd0dad8; TIEBAUID=cd4907611a79bbddb5ca5bd8; BIDUPSID=D69331E6E1E87361E4D2CF7D29C6F88F; PSTM=1596697528; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1596527801,1596530614,1596531175,1597031432; st_key_id=17; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1597031455; 1543293704_FRSVideoUploadTip=1; st_data=0a5883fb0fc699bffc73f684ec144c86f6a7ff72bc982a3d9b893cfdf71c85067afc10846c0578b3a2d3cf7a39cf6fce0a7d94c8c058483b6d3aad1ea0d3b28e8d6e0dc7d57bedf1678ca25f934650085b71636edfd764fb76bc2130551236aa32b797479da33a2d3a5a33fe2232a3fcf6de1c7d40e23987a568a025614488ed; st_sign=470808a4",
    "Host": "tieba.baidu.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}
session = requests.session()
session.headers = headers
#检查是否反应正确
def get_parse(url):
    html = session.get(url)
    if html.status_code ==200:
        print(html.status_code)
        get_html(html)
    else:
        print(html.status_code)
#获取每一页的贴吧的URL
def get_html(html):
    content = html.text
    daihao = re.compile("data-tid='(.*?)'",re.S|re.I)
    result = daihao.findall(content)
    for i in result:
        get_page(i)
#获取每一个贴里面的页数
def get_page(i):
    url = "https://tieba.baidu.com/p/" + i
    r = session.get(url)
    soup = BeautifulSoup(r.text,'lxml')
    try:
        #用BeautifulSoup去获取每一个贴里面有多少页
        span = soup.find_all('span',class_ = 'red')
        tiebayeshu = str(span[1]).replace('<span class="red">', '').replace('</span>', '')
        get_pinglin(i, tiebayeshu)
    except:
        pass
#获取贴吧里面评论的页数的URL
def get_pinglin(i,yeshu):
    list = []
    for j in range(1, int(yeshu) + 1):
        url = "https://tieba.baidu.com/p/{}?pn={}".format(i,j)
        list.append(url)
        get_neirong(list)

#获取每一个URL里面的评论内容
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
        #设置一个时间缓存带，防止被系统识别
        time.sleep(random.randint(1, 2))
        #最后将获取到的内容写入txt文本里面
    with open("上海仁济医院.txt",'a+', encoding='utf-8') as f:
        for i in range(len(new)):
            f.write(new[i])
            f.write('\n')
            print("写入成功")
if __name__ == '__main__':
    #50为一页
    for i in tqdm(range(0,251,50)):
        url = "https://tieba.baidu.com/f?kw=%E4%B8%8A%E6%B5%B7%E4%BB%81%E6%B5%8E%E5%8C%BB%E9%99%A2&ie=utf-8&pn={}".format(i)
        get_parse(url)