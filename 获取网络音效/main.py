import requests
from lxml import etree
from urllib import parse
import os
import time
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    'Cookie': 'isworkdesign=1; hostfrom=www.tukuppt.com; Hm_lvt_a620c01aafc084582f0ec24d96b73ad8=1602660495; Hm_lpvt_a620c01aafc084582f0ec24d96b73ad8=1602662440',
    'Host': 'www.tukuppt.com',
}
session = requests.session()
session.headers = headers

def get_parse(url):
    html = requests.get(url,headers=headers)
    if html.status_code ==200:
        get_html(html)
    else:
        print(html.status_code)
def get_html(html):
    content = html.text
    soup = etree.HTML(content)
    href = soup.xpath("//dt[@class = 'info']/a[@class='title']/@href")
    for i in range(40):
        url = parse.urljoin('https://www.tukuppt.com',href[i])
        get_yinxiao(url)

def get_yinxiao(url):
        html = requests.get(url,headers=headers)
        content = html.text
        soup = etree.HTML(content)
        mp3 = soup.xpath("//audio[@preload = 'none']/source/@src")
        url = parse.urljoin('https:',mp3[0])
        title = soup.xpath("//div[@class='banquan']/h1[@class='title']/text()")[0]
        print(url)
        dowloand(url,title)
def dowloand(url,title):
    if not os.path.exists('./音效'):
        os.mkdir('./音效')
    html = requests.get(url,headers=headers).content
    with open("./音效/{}.mp3".format(title),'wb')as f:
        f.write(html)
        print('{}下载成功'.format(title))


if __name__ == '__main__':
    for i in range(1,4,1):
        url = 'https://www.tukuppt.com/yinxiaomuban/zhuanchang/__dnum_0_0_0_0_0_0_{}.html'.format(i)
        time.sleep(1)
        get_parse(url)