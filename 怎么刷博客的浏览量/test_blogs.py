import requests
import time
import random

from lxml import etree
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL

import sys
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    "cookie": "uuid_tt_dd=10_19002881610-1614757398939-632696; ssxmod_itna=WqIx2DBDRD9D0DRhxl4iwO87I3BIx+uF4IbHKDsKqTDSxGKidDqxBnWCaBm+wRGqe1ixmiK4Q7GfqqefiflxeWtAIO4GLDmKDyYA74+oD4fKGwD0eG+DD4DWDmeHDnxAQDjgKGWDbh=GfDDoDY+=uDitD4qDBzrdDKqGg7whz7ki6tjU5vwGx=0D9D0UYxBLx3cx9FnWW1GNWQqGymPGuULt9mMrDChv3irh3I0xzewGG=AqsGDhieLqhODAa3U4YKGh3KY8F0ABXxDfKYtqxD==; ssxmod_itna2=WqIx2DBDRD9D0DRhxl4iwO87I3BIx+uF4Ib5ikvaYQDlxEWxj+K+lfdid9tRee6R=BK=1KYYTxmmtSnfybtKp6CGhvR7YkGLz3AgDMyxiesuh+F3YjCOvtE=Yuk5GRMglMH=6mXyobVEFbPcRQ4+mCKBniMgbWnBmxspAmscqsKnqIt2TmKtHrvD07hx08DYIq4D; UserName=zyh960; UserInfo=9816bdf17ae64e1388c2c5d6870b7296; UserToken=9816bdf17ae64e1388c2c5d6870b7296; UserNick=%E6%9C%89%E7%8C%AB%E8%85%BB%E5%A6%96; AU=D4E; UN=zyh960; BT=1614758050906; p_uid=U010000; Hm_up_6bcd52f51e9b3dce32bec4a3997715ac=%7B%22islogin%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22uid_%22%3A%7B%22value%22%3A%22zyh960%22%2C%22scope%22%3A1%7D%7D; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_19002881610-1614757398939-632696!5744*1*zyh960; _ga=GA1.2.445910684.1614760805; Hm_lvt_e5ef47b9f471504959267fd614d579cd=1623747613; dc_session_id=10_1627262145879.464600; _gid=GA1.2.967453966.1627262122; c_hasSub=true; dc_sid=da41888f005a7b982a11851e002cf5a0; TY_SESSION_ID=bc88a8a2-d6e5-4f3f-9e38-1fe65604d0e9; c_first_ref=default; c_first_page=https%3A//blog.csdn.net/; c_segment=8; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1627022340,1627022586,1627262122,1627264935; log_Id_click=188; c_pref=; c_ref=https%3A//blog.csdn.net/; c_page_id=default; dc_tos=qwtxvn; log_Id_pv=308; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1627265221; log_Id_view=716",
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
    url = soup.xpath("//article[@class='blog-list-box']/a/@href")
    fangwen_url(url)

def fangwen_url(url):
    try:
        for u in url:
            requests.get(u,headers=headers)
            time.sleep(random.random()/1000)
        print('把博客浏览了1遍')
    except Exception as e:
        try:
            receiver = sys.argv[1]
        except:
            receiver = 'Felix_Zeng@macroview.com'  # 收件人邮箱地址
        send_mail(receiver)  # 调用函数，发送邮件

def send_mail(receiver):
    host_server = 'smtp.qq.com'  # QQ邮箱的SMTP服务器
    sender_qq = '960751327'  # 发件人的QQ号码z
    pwd = 'fdrrjmiqqnaubdcj'  # QQ邮箱的授权码
    sender_qq_mail = '960751327@qq.com'  # 发件人邮箱地址

    mail_content = str('博客刷取失败，请注意查看脚本报错内容')  # 邮件正文内容
    mail_title = '博客告警邮件'  # 设置邮件标题

    smtp = SMTP_SSL(host_server)  # SSL 登录
    smtp.set_debuglevel(0)  # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
    smtp.ehlo(host_server)  # 连接服务器
    smtp.login(sender_qq, pwd)  # 邮箱登录

    msg = MIMEText(mail_content, "plain", 'utf-8')  # 填写正文内容
    msg["Subject"] = Header(mail_title, 'utf-8')  # 填写邮件标题
    msg["From"] = sender_qq_mail  # 发送者邮箱地址
    msg["To"] = receiver  # 接收者邮件地址

    try:
        smtp.sendmail(sender_qq_mail, receiver, msg.as_string())  # 发送邮件函数
        smtp.quit()  # 发送邮件结束
        print("Successfully Send！")  # 输出成功标志
    except:
        print("The sever is busy,please continue later.")


if __name__ == '__main__':
    url = 'https://blog.csdn.net/zyh960'
    get_blog_url(url)


