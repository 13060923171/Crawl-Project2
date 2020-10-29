import requests
from lxml import etree
import random
import time
import pandas as pd
import openpyxl
from tqdm import tqdm
user_agent = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]

headers = {
    "User-Agent": random.choice(user_agent)
}
wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(['土地位置', '出让形式', '推出时间', '土地面积', '规划建筑面积', '土地地址', '成交状态', '土地代号', '规划用途'])
def get_parse(url):
    html = requests.get(url,headers=headers)
    if html.status_code == 200:
        get_html(html)
    else:
        print(html.status_code)
def get_html(html):
    content = html.text
    soup = etree.HTML(content)
    lis = soup.xpath('//div[@class="land-l-cont"]/dl')
    for li in lis:
        try:
            location = li.xpath('.//dd/p[7]/text()')[0]  # 土地位置
            transfer_form = li.xpath('.//dt/i/text()')[0]  # 出让形式
            launch_time = li.xpath('.//dd/p[1]/text()')[0]  # 推出时间
            land_area = li.xpath('.//dd/p[3]/text()')[0]  # 土地面积
            planning_area = li.xpath('.//dd/p[5]/text()')[0]  # 规划建筑面积
            address = li.xpath('.//dd/p[4]/text()')[0]  # 土地地址
            state = li.xpath('.//dd/p[2]/text()')[0]  # 成交状态
            area_code = li.xpath('.//dt/span/text()')[0]  # 土地代号
            planned_use = li.xpath('.//dd/p[6]/text()')[0]  # 规划用途
            data = [location,transfer_form,launch_time,land_area,planning_area,address,state,area_code,planned_use]
            sheet.append(data)
        except:
            pass
    wb.save(filename="real_estate_info.xlsx")
    time.sleep(2)

def downloads(location,transfer_form,launch_time,land_area,planning_area,address,state,area_code,planned_use):
    df = pd.DataFrame()
    df['土地位置'] = location
    df['出让形式'] = transfer_form
    df['推出时间'] = launch_time
    df['土地面积'] = land_area
    df['规划建筑面积'] = planning_area
    df['土地地址'] = address
    df['成交状态'] = state
    df['土地代号'] = area_code
    df['规划用途'] = planned_use
    try:
        df.to_csv("土地租聘信息.csv", mode="a+", header=None, index=None, encoding="gbk")
        print("写入成功")
    except:
        print("当页数据写入失败")
if __name__ == '__main__':
    for i in tqdm(range(10)):
        url = 'https://www.tudinet.com/market-0-0-0-0/list-pg{}.html'.format(i)
        get_parse(url)