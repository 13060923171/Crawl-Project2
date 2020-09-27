import requests
from lxml import etree
import pandas as pd
from tqdm import tqdm
headers = {
    'Cookie': 'JSESSIONID=9C98AC57F4323FB7FDE6A49463E0F72B; clientlanguage=zh_CN',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
    'Host': 'www.xtxh.net',
}

def get_parse(url):
    html = requests.get(url,headers=headers)
    if html.status_code ==200:
        get_html(html)
    else:
        print(html.status_code)

def get_html(html):
    content = html.text
    soup = etree.HTML(content)
    title = soup.xpath('//div[@class = "title"]/a/text()')
    time = soup.xpath('//div[@class = "time"]/text()')
    df = pd.DataFrame()
    df['时间'] = time
    df['标题'] = title
    try:
        df.to_csv("中国信托.csv", mode="a+", header=None, index=None, encoding="utf-8")
        print("写入成功")
    except:
        print("当页数据写入失败")

if __name__ == '__main__':
    for i in tqdm(range(1,37,1)):
        url = 'http://www.xtxh.net/xtxh/responsibilitynews/index_{}.htm'.format(i)
        get_parse(url)