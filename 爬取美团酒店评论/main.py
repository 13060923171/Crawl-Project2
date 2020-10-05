import requests
import re
import json
import threading
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'Cookie': '_lxsdk_cuid=173e1f47707c8-0dcd4ff30b4ae3-3323765-e1000-173e1f47707c8; _hc.v=5f3d72e8-ba19-4712-5fce-55b10b156df5.1597224599; ci=30; rvct=30%2C1; iuuid=5507984E87AFD6AA06E2F4757AB74FA91C04750435F6A4892A8830402F602188; cityname=%E6%B7%B1%E5%9C%B3; _lxsdk=5507984E87AFD6AA06E2F4757AB74FA91C04750435F6A4892A8830402F602188; IJSESSIONID=1rw0g3kq87i22vq71xmg1yry7; i_extend=E047220785835618635935358089570402201858_c0_e6489321064218812656_a%e4%b8%9c%e9%97%a8_b400201_o1_dhotelpoitagb_k1002Gempty__xhotelhomepage__yselect__zday; _lxsdk_s=174f270209f-928-903-49f%7C%7C23',
}
#去判断一个页面是否是正常，如果正常那么进行下一步抓取
def get_parse(url):
    html = requests.get(url,headers= headers)
    if html.status_code ==200:
        print('页面正常')
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
    #定位最低价
    lowestPrices = re.compile('"lowestPrice":(.*?),"', re.I | re.S)
    lowestPrice = lowestPrices.findall(content)
    #定位评分
    scoreIntros = re.compile('"scoreIntro":"(.*?)",', re.I | re.S)
    scoreIntro = scoreIntros.findall(content)
    #定位酒店id
    realPoiIds = re.compile('"realPoiId":(.*?),"', re.I | re.S)
    realPoiId = realPoiIds.findall(content)
    # 获取总评论数
    commentsCountDescs = re.compile('"commentsCountDesc":"(.*?)条评论",', re.I | re.S)
    commentsCountDesc = commentsCountDescs.findall(content)
    #加一个防错机制，这样的目的是为了防止列表出现问题
    try:
        for i in range(len(name)):
            #去获取评分在4.5以上酒店的评论，因为当你抓取太多评论的时候，ip容易被封，所以适度抓取就好了
            if '很好' in scoreIntro[i]:
                print(name[i], addr[i], lowestPrice[i], scoreIntro[i],realPoiId[i],commentsCountDesc[i])
                #传参，把对应的参数传入到dowload函数里面，便于下载
                dowload(name[i], addr[i], lowestPrice[i], scoreIntro[i],realPoiId[i])
                #开一个多线程来抓取评论，因为有些评论很多，有的几千几万条，这样太消耗时间了。因此需要写一个多线程来加快我们的抓取速度
                t = threading.Thread(target=get_comment,args=(realPoiId[i],commentsCountDesc[i],))
                t.start()
    except:
        pass
#写一个获取评论的函数
def get_comment(id,comment):
    #根据获取评论的URL，我们可以知道，start为翻页，每加15便是翻一页，
    # 所以构建这个url我们只需将总评论数除以15得出的数字就是我们需要翻页的次数
    for i in range(0,int(int(comment)/15+1),15):
        url = 'https://ihotel.meituan.com/api/v2/comments/biz/' \
              'reviewList?referid={}&limit=15&start={}&filterid=800&querytype=1&utm_medium=pc'.format(id,i)
        #在获取这个URL之后，我们再用请求这个URL来获取相应的内容
        html = requests.get(url, headers=headers).text
        # 获取评论
        Contents = re.compile('"Content":(.*?)",', re.I | re.S)
        Content = Contents.findall(html)
        #最后把获取到的评论数量输出到我们的dowload1函数里面，然后下载我们需要的评论数
        dowload1(id,Content)

def dowload(t,a,avg,c,p):
    data = {
        '酒店名字': t,
        '酒店地址': a,
        '最低价': avg,
        '评分': c,
        '酒店的id': p,
    }
    with open("酒店的基本信息.txt","a+",encoding="utf-8")as f:
        f.write(json.dumps(data,ensure_ascii=False)+"\n")
        print("写入成功")

def dowload1(id,comment):
    with open("{}.txt".format(id),"a+",encoding="utf-8")as f:
        f.write(json.dumps(comment,ensure_ascii=False)+"\n")
        print("写入成功")


if __name__ == '__main__':
    #根据我们的URL得知，它的offset为翻页，20为翻一页，所以我们写一个循环，20为一跳转，这样便于我们爬取
    #20为翻一页，cateId为城市对应的数字，这里的20代表的是广州
    for i in range(0,201,20):
        url = 'https://ihotel.meituan.com/hbsearch/HotelSearch?utm_medium=touch&version_name=999.9&' \
          'platformid=1&cateId=20&newcate=1&limit=20&offset={}&cityId=20&ci=20&startendday=20201004~20201004&' \
          'startDay=20201004&endDay=20201004&attr_28=129&sort=defaults&uuid=5507984E87AFD6AA06E2F4757AB74' \
          'FA91C04750435F6A4892A8830402F602188&accommodationType=1'.format(i)
        get_parse(url)


