import re
import requests
import time
import random
import os
from lxml import etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    'cookie': 'uuid_tt_dd=10_16975234530-1596381685482-747666; dc_session_id=10_1596381685482.628592; UserName=zyh960; UserInfo=facd41192d0d49849d297f58b48c9222; UserToken=facd41192d0d49849d297f58b48c9222; UserNick=zyh960; AU=D4E; UN=zyh960; BT=1596381694889; p_uid=U000000; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_16975234530-1596381685482-747666!5744*1*zyh960; _ga=GA1.2.1794079522.1596731011; Hm_up_e5ef47b9f471504959267fd614d579cd=%7B%22islogin%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22uid_%22%3A%7B%22value%22%3A%22zyh960%22%2C%22scope%22%3A1%7D%7D; Hm_ct_e5ef47b9f471504959267fd614d579cd=5744*1*zyh960!6525*1*10_16975234530-1596381685482-747666; Hm_lvt_e5ef47b9f471504959267fd614d579cd=1597239786,1597239793; Hm_up_6bcd52f51e9b3dce32bec4a3997715ac=%7B%22uid_%22%3A%7B%22value%22%3A%22zyh960%22%2C%22scope%22%3A1%7D%2C%22islogin%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%7D; announcement=%257B%2522isLogin%2522%253Atrue%252C%2522announcementUrl%2522%253A%2522https%253A%252F%252Flive.csdn.net%252Froom%252Fyzkskaka%252F5n5O4pRs%253Futm_source%253D1598583200%2522%252C%2522announcementCount%2522%253A0%257D; searchHistoryArray=%255B%2522%25E7%2588%25AC%25E5%258F%2596%25E6%2588%25BF%25E5%25A4%25A9%25E4%25B8%258B%25E7%25A7%259F%25E6%2588%25BF%25E4%25BF%25A1%25E6%2581%25AF%2522%252C%2522%25E6%2588%25BF%25E5%25A4%25A9%25E4%25B8%258B%25E6%259C%2580%25E6%2596%25B0%25E7%2588%25AC%25E5%258F%2596%2522%255D; log_Id_click=186; dc_sid=1cb5e65ff7c12e4d19234ebfc2ff9124; TY_SESSION_ID=31b32d34-8469-4756-8104-2ebaf3066e5e; c_first_ref=www.google.com; c_first_page=https%3A//blog.csdn.net/u013424864/article/details/60778031; c_segment=2; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1602635270,1602648656,1602658826,1602662512; _gid=GA1.2.1579581287.1602662513; c_ref=https%3A//blog.csdn.net/; log_Id_view=1174; c_page_id=default; dc_tos=qi6nt0; log_Id_pv=376; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1602664453',
    'referer': 'https://blog.csdn.net/',
}
def get_blog_url(url):
    html = requests.get(url,headers=headers)
    if html.status_code ==200:
        get_html(html)
    else:
        print(html.status_code)

def get_html(html):
    content = html.text
    soup = etree.HTML(content)
    url = soup.xpath("//h4/a/@href")
    fangwen_url(url)
def fangwen_url(url):
    i = 0
    for u in url:
        requests.get(u,headers=headers)
        print(u)
        time.sleep(random.random()/1000)
        i +=1
        sum = int(i/12)
    print('把博客浏览了{}遍'.format(sum))
if __name__ == '__main__':
    url = 'https://blog.csdn.net/zyh960'
    get_blog_url(url)