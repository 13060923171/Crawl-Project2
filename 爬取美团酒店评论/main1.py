import requests
import re
import json
import time
import random


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
    'User-Agent': random.choice(user_agent),
    'Cookie': 'uuid=13a0ebb3eb3f4e4ca3ab.1609749998.1.0.0; _lxsdk_cuid=176cc938bb490-0040463f3d68d8-c791039-e1000-176cc938bb5c8; iuuid=25A31E7553EB400F96942D62BCA7FFBAE7732C1D202A34A2546AD68C9161CB68; _lxsdk=25A31E7553EB400F96942D62BCA7FFBAE7732C1D202A34A2546AD68C9161CB68; Hm_lvt_f66b37722f586a240d4621318a5a6ebe=1609852138; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; IJSESSIONID=g6l850xqurcl1otf9tpe9753a; ci=101; rvct=101%2C60%2C45%2C207; cityname=%E5%A4%AA%E5%8E%9F; _lxsdk_s=176f5727756-670-5a-cae%7C%7C13',
}

#去判断一个页面是否是正常，如果正常那么进行下一步抓取
def get_parse(url):
    html = requests.get(url,headers= headers)
    time.sleep(random.random())
    if html.status_code == 200:
        get_html(html)
    else:
        print(html.status_code)

#用正则去获取当前酒店的名称，地址，最低价，评分，酒店的id，评论的总数
def get_html(html):
    content = html.text
    #定位酒店名称
    names = re.compile('"name":"(.*?)",', re.I | re.S)
    name = names.findall(content)
    #定位酒店地址
    addrs = re.compile('"addr":"(.*?)",', re.I | re.S)
    addr = addrs.findall(content)
    #定位城市
    citys = re.compile('"cityName":(.*?),"', re.I | re.S)
    city = citys.findall(content)
    #定位评分
    scoreIntros = re.compile('"scoreIntro":"(.*?)",', re.I | re.S)
    scoreIntro = scoreIntros.findall(content)
    # 酒店类型
    hotelStars = re.compile('"hotelStar":"(.*?)",', re.I | re.S)
    hotelStar = hotelStars.findall(content)
    #酒店开业时间
    start_businesss = re.compile('(\d+年开业)', re.I | re.S)
    start_business = start_businesss.findall(content)
    # 酒店装修时间
    finishs = re.compile('(\d+年装修)', re.I | re.S)
    finish = finishs.findall(content)
    # 加一个防错机制，这样的目的是为了防止列表出现问题
    try:
        for i in range(len(name)):
            print(name[i],hotelStar[i],start_business[i],finish[i],scoreIntro[i],city[i],addr[i])
            #传参，把对应的参数传入到dowload函数里面，便于下载
            dowload(name[i],hotelStar[i],start_business[i],finish[i],scoreIntro[i],city[i],addr[i])
    except:
        pass

def dowload(t,h,k,z,c,city,a):
    data = {
        '酒店名字': t,
        '酒店类型': h,
        '开业时间': k,
        '装修时间': z,
        '酒店评分': c,
        '所在省份': '重庆市',
        '所在城市': city,
        '酒店地址': a,
    }
    with open("重庆市酒店的基本信息.txt","a+",encoding="utf-8")as f:
        f.write(json.dumps(data,ensure_ascii=False)+"\n")
        print("写入成功")

def city_number():
    headers = {
        'X-FOR-WITH': 'f34yJXBymO9/nLKKQNBCoOyOeXvb8mP1dIHo3fPlirAY2Yq1iJCrFfoFSpm8Ei3Y46j7TngamXaPsl+FJ//yY3IWzckDaU9LqotXgVl8dxdZ2ZcI3a7UpQ4Q5Ooo6NSgz0ov5LTWwLgAmCQ83uid0tLfXnei7TVYOcIJlGCPoSZITZlnxeg+8gObkiEubTQW6VJ8SYFrJC0WUBNKIssHYA==',
        'Cookie': 'uuid=13a0ebb3eb3f4e4ca3ab.1609749998.1.0.0; _lxsdk_cuid=176cc938bb490-0040463f3d68d8-c791039-e1000-176cc938bb5c8; iuuid=25A31E7553EB400F96942D62BCA7FFBAE7732C1D202A34A2546AD68C9161CB68; _lxsdk=25A31E7553EB400F96942D62BCA7FFBAE7732C1D202A34A2546AD68C9161CB68; Hm_lvt_f66b37722f586a240d4621318a5a6ebe=1609852138; IJSESSIONID=177ybmei9ddit1d926tv41n3vk; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; ci=45; rvct=45%2C207%2C60; hotel_city_id=45; hotel_city_info=%7B%22id%22%3A45%2C%22name%22%3A%22%E9%87%8D%E5%BA%86%22%2C%22pinyin%22%3A%22chongqing%22%7D; cityname=%E9%87%8D%E5%BA%86; _lxsdk_s=176d5a7ea7a-33f-425-929%7C%7C66',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    }
    url = 'https://hotel.meituan.com/dist/static/data/city.json?utm_medium=pc&version_name=999.9'
    html = requests.get(url, headers=headers)
    content = html.json()
    data = content['data']
    with open('省份城市.txt', 'r', encoding='utf-8') as f:
        content1 = f.readlines()
    city = []
    for c in content1:
        c = str(c)
        c = c.split('(')
        city.append(c[0])
    number_list = []
    for d in range(len(data)):
        name = data[d]['name']
        id = data[d]['id']
        for c in city:
            if name in c:
                number_list.append(id)
    return number_list

if __name__ == '__main__':
    # 根据我们的URL得知，它的offset为翻页，20为翻一页，所以我们写一个循环，20为一跳转，这样便于我们爬取
    # 20为翻一页，cateId为城市对应的数字，这里的20代表的是广州
    # list1 = city_number()
    # for l in list1:
    for i in range(0,1121,20):
        url = 'https://ihotel.meituan.com/hbsearch/HotelSearch?utm_medium=pc&version_name=999.9&cateId=20&attr_28=129&uuid=25A31E7553EB400F96942D62BCA7FFBAE7732C1D202A34A2546AD68C9161CB68%401610435737059&cityId=45&offset={}&limit=20&startDay=20210112&endDay=20210112&q=&sort=defaults&X-FOR-WITH=Jo6wwC0IQuYAQ9ZO9mXlbhpAAlyu8NRHyI7Jew8M9ICXAj3lFQo%2BOcckMzqCP34JLask2JO%2B8NUVSQxaZTqcpVYm%2Bi0%2BBTRPjZvX7%2FxpQ8Xd8SrIVNfvoO3TrPtZGZ9K4wSUFaKJvpgC9TB%2B%2BsWJ0hyC7VXbwZnS%2FIZmJ5hvy%2BJmu6qjc%2FlmupzoQTmH8CwfFB6O3PO5nPiY64sKxbwhWQ%3D%3D'.format(i)
        get_parse(url)
    # url = 'https://ihotel.meituan.com/hbsearch/HotelSearch?utm_medium=pc&version_name=999.9&cateId=20&attr_28=129&uuid=25A31E7553EB400F96942D62BCA7FFBAE7732C1D202A34A2546AD68C9161CB68%401610419861240&cityId=45&offset=0&limit=20&startDay=20210112&endDay=20210112&q=&sort=defaults&X-FOR-WITH=drT%2BLVdQBIXux2nsOKSwjpxYmaM4Nrpye2eal6kbfzVcVOT8vssVlfMkuHNFmBxG5253iAh1et4ZU0xiee8aYbEnC2flcCBPs2W0STKT2hGWZ97%2F2Dv62iwBHP42KSNdR6DygKzw1HCAukHuSGe%2FGiEPqGd7lFvumXyG8dGxx2L7ht6tIhsQaiP8eczllWLOoo7GbsW7uNXUa4n0AIFz5Q%3D%3D'
    # get_parse(url)


