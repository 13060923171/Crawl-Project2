import requests
from lxml import etree
import re
import pandas as pd
import time
headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    'Cookie': 'lianjia_uuid=ae6c77cd-3401-44c5-83ad-1093c56d867c; lianjia_ssid=fe62532e-4daa-41b2-9a47-10d1a2e0a6ed; sajssdk_2015_cross_new_user=1; UM_distinctid=1756e750021c37-0381229d32ba41-303464-e1000-1756e750022a95; CNZZDATA1254525948=707208356-1603874827-https%253A%252F%252Fwww.google.com%252F%7C1603874827; CNZZDATA1253491255=1070754301-1603875510-https%253A%252F%252Fwww.google.com%252F%7C1603875510; _ga=GA1.2.723279650.1603875963; _gid=GA1.2.419342807.1603875963; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1603875963; select_city=440100; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1603875997; csrfSecret=_xfk7dic-iRRYR4oxfhTcPmC; activity_ke_com=undefined; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221756e74fe968dc-0498872ded9ff6-303464-921600-1756e74fe97977%22%2C%22%24device_id%22%3A%221756e74fe968dc-0498872ded9ff6-303464-921600-1756e74fe97977%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24latest_referrer_host%22%3A%22www.google.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_utm_source%22%3A%22guanwang%22%7D%7D; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiNDY5NGZiNWJiYzkzM2IzMmUyNzBmYmRhNmMwYjFiMjg5OWI0NThmN2VlNjA0MzZmYTIyNmNlZmU1Y2MxN2FhODkzZDRjYTEwMjBhNmU0NmIwODZkODQyOGFhOTc1NmZiYTFjNmZkMDc2YjViMjk0YzFiNjBiYjI1NjNjM2FkZTZjNDg0NTUwODk2ZDQ4OWRkZmJkMTBlZjk4NmM0MTE0NmRlZDYzZWU3YjMwM2YzZjYzYmMwMWQzZTU0NzkzMDRjZDE0MzZmM2RhMDA1MGU2NDQwZTY2ODRhYmVjZjkzY2Q3N2M3NGUwMmQ5NDVlNGU5ZGM2NWU0OTEyOWE0NjI1NjBlZmY1MTA4NmUyZGNmNTExOTllMTRjMTE1NDkzOWYzNzVmYWVjMjdmZGQ0ZDQxYzk5NWY5ZTU5ZTE1NGExZDI4NGNkNjcyOTdiZTZlOTJkY2JhODU5OWJlNmExMGVhYlwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCJkZjZiYjQ5MFwifSIsInIiOiJodHRwczovL20ubGlhbmppYS5jb20vY2h1enUvZ3ovenVmYW5nL0daMjU2NTA1Mzc1OTAwMDQxMjE2MC5odG1sP2g9R1oyNTY1MDUzNzU5MDAwNDEyMTYwJnQ9ZGVmYXVsdCZjbGlja19wb3NpdGlvbj0wJmFkX2NvZGU9MCZhZF90eXBlPTAmZGlzdHJpYnV0aW9uX3R5cGU9MjAzNTAwMDAwMDAxJnVuaXF1ZV9pZD1hZTZjNzdjZDM0MDE0NGM1ODNhZDEwOTNjNTZkODY3Y2NodXp1Z3p6dWZhbmdXZWRPY3QyODIwMjAxNzA2MzkiLCJvcyI6IndlYiIsInYiOiIwLjEifQ==',
     'Host': 'm.lianjia.com',
    'Referer': 'https://m.lianjia.com/',
}
def parse_url(url):
    html = requests.get(url,headers=headers)
    if html.status_code ==200:
        get_html(html)
    else:
        print(html.status_code)
def get_html(html):
    content = html.text
    soup = etree.HTML(content)
    href = soup.xpath('//div/a[@data-el ="jumpDetailEl"]/@href')
    title = soup.xpath('//div/p[@class="content__item__title"]/text()')
    nerong = soup.xpath('//div/p[@class="content__item__content"]/text()')
    prices = soup.xpath('//div/p[@class="content__item__bottom"]/text()')
    prices = str(prices)
    prices_list = re.findall(r"\d+\.?\d*",prices)
    tag = soup.xpath('//div/p[@class="content__item__tag--wrapper"]')
    biaoqian_list = []
    for t in tag:
        biaoqian = t.xpath('./i/text()')
        tag = '|'.join(biaoqian)
        biaoqian_list.append(tag)
    print(prices_list,href,title,nerong,biaoqian_list)
    downloads(title,nerong,prices_list,href)

def downloads(title,nerong,prices_list,href):
    df = pd.DataFrame()
    df['标题'] = title
    df['内容'] = nerong
    # df['标签'] = biaoqian_list
    df['价格'] = prices_list
    df['链接'] = href
    try:
        df.to_csv("链家广州租房信息.csv", mode="a+", header=None, index=None, encoding="gbk")
        print("写入成功")
    except:
        print("当页数据写入失败")
    time.sleep(1)
if __name__ == '__main__':
    for i in range(1,2):
        url = 'https://m.lianjia.com/chuzu/gz/zufang/pg{}'.format(i)
        parse_url(url)