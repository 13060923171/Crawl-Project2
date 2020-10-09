import re
import requests
import json
from urllib import parse
from lxml import etree

# 预设
requests.packages.urllib3.disable_warnings()
session = requests.session()
session.verify = False
session.timeout = 20
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3970.5 Safari/537.36"
}


def getweiboremark(name, index=1, num=-1):
    # name参数代表微博主页的名称
    # index参数代表目标微博的序号
    # num代表要爬的评论数，-1代表所有评论
    # 返回结果为评论列表
    home_url = 'https://weibo.com/' + name
    tid = get_tid()
    get_cookie(tid=tid)
    mids = get_mids(home_url=home_url)
    remark_data = get_remarkdata(num=num, file=name,mids=mids, index=index)
    return remark_data


def get_tid():
    # 获取tid
    url1 = "https://passport.weibo.com/visitor/genvisitor"
    data = "cb=gen_callback&fp=%7B%22os%22%3A%221%22%2C%22browser%22%3A%22Chrome80%2C0%2C3970%2C5%22%2C%22fonts%22%3A%22undefined%22%2C%22screenInfo%22%3A%221920*1080*24%22%2C%22plugins%22%3A%22Portable%20Document%20Format%3A%3Ainternal-pdf-viewer%3A%3AChrome%20PDF%20Plugin%7C%3A%3Amhjfbmdgcfjbbpaeojofohoefgiehjai%3A%3AChrome%20PDF%20Viewer%7C%3A%3Ainternal-nacl-plugin%3A%3ANative%20Client%22%7D"

    headers.update({'Content-Type': 'application/x-www-form-urlencoded'})
    res=session.post(url=url1, headers=headers, data=data).content.decode('utf-8')[36:-2]
    tid = json.loads(res)['data']['tid']
    del headers['Content-Type']
    return tid


def get_cookie(tid, session=session):
    # 获取访客cookie
    url2 = "https://passport.weibo.com/visitor/visitor?a=incarnate&t=" + parse.quote(
        tid) + "&w=2&c=095&gc=&cb=cross_domain&from=weibo"
    session.get(url=url2.encode('utf-8'), headers=headers)


def get_mids(home_url, session=session, try_num=0):
    # 访问微博主页，解析获取评论页面
    # 要想获取mids，必须先获取cookie
    res = session.get(url=home_url, headers=headers).content
    html = etree.HTML(res)
    # 含有mid的html代码被隐藏在这一个json中
    mid_scripts = html.xpath ("//script")
    for mid_script in mid_scripts:
        try:
            mid_json = json.loads(mid_script.text[8:-1])
            mid_html = etree.HTML(mid_json['html'])
            name = mid_html.xpath("//div/@tbinfo")
            mids = mid_html.xpath("//div[@tbinfo='" + name[0] + "']/@mid")
            print("//div[@tbinfo=" + name[0] + "]/@mid")
            print(mids[0])
            break
        except:
            continue

    return mids


def get_remarkdata(num, mids, file,index=1):
    # 获取评论数据
    url_remarkdata = 'https://weibo.com/aj/v6/comment/big?ajwvr=6&id={mid}&page={page}&sum_comment_number={comment_number}&from=singleWeiBo'
    # 请求地址

    current_num = 0
    page = 1
    male = []
    female = []
    a = True
    user_list = []
    while True:
        print("-" * 50)
        number = 0

        url_remarkdata_new = url_remarkdata.format(mid=str(mids[index]),comment_number=str(current_num),page=str(page))
        # 进行赋值
        print(url_remarkdata_new)

        data = session.get(url_remarkdata_new,headers=headers)
        # 发送请求
        remark_html = etree.HTML(json.loads(data.content.decode (encoding='utf-8'))['data']['html'])

        # 转换
        remark_num = json.loads(data.content.decode(encoding='utf-8'))['data']['count']
        # 获取微博评论总条数
        if num == -1:
            num = remark_num
        elif num > remark_num:
            num = remark_num

        user = remark_html.xpath("//div[@class='WB_face W_fl']/a/@href")

        # for i in user:
        #     if i is not user_list:
        #         user_list.append(i)

        name = remark_html.xpath("//div[@class='WB_face W_fl']/a/img/@alt")
        img = remark_html.xpath("//div[@class='WB_face W_fl']/a/img/@src")

        user_url = "https:"
        # 用户主页
        for i in user:
            url = user_url+i
            user_sex = session.get(url, headers=headers).content.decode()
            try:
                sex = re.compile(r'<a><i class=\\"W_icon(.*?)\\"',re.S).findall(user_sex)[0].strip()
                approve = re.compile(r'<em title= \\"(微博机构认证)\\" class=\\"W_icon_co2 icon_pf_approve_co\\"',
                                     re.S).findall(user_sex)
                changdu = re.compile(r'<h1 class=\\"username\\">(.*?)<\\/h1>', re.S).findall(user_sex)[0].strip()
            except:
                pass
            if i is not user:
                if len(changdu) <= 6:
                    if len(approve) == 0:
                        if sex == 'icon_pf_male':
                            if len(male) <= num * 0.4:
                                male.append(url)
                                print("添加男")
                                try:
                                    with open(file + ".txt",'a') as fp:
                                        fp.write(name[number] + "\t" + "男" + "\n")
                                except:
                                    pass
                                try:
                                    img_name = name[number].split("=")[-1]
                                    img_url = session.get(img[number])
                                except:
                                    pass

                                with open(file +"/"+ img_name + '.png','wb+') as fp:
                                    fp.write(img_url.content)
                            else:
                                continue
                        else:
                            if len(female) <= num * 0.6:
                                female.append (url)
                                print("添加女")
                                try:
                                    with open(file + ".txt",'a') as fp:
                                        fp.write(name[number] + "\t" + "女" + "\n")
                                except:
                                    pass
                                try:
                                    img_name = name[number].split ("=")[-1]
                                    img_url = session.get(img[number])
                                except:
                                    pass
                                with open(file +"/"+ img_name + '.png', 'wb+') as fp:
                                    fp.write(img_url.content)

                            else:
                                continue
                if len(female) >=num*0.6 and len(male) >= num*0.4:
                    a = False
                    break

                number += 1
                print(number)

        if a==False:
            break
        else:
            page += 1

    print("男" + str(len(male)))
    print("女" + str(len(female)))


if __name__ == '__main__':
    #清华
    # getweiboremark(name="tsinghua",index=0,num=-1)
    #北大
    # getweiboremark(name='PKU',index=0,num=-1)
    #上海交通大学
    # getweiboremark(name='chiaotunguniv',index=0,num=-1)
    #上海外国语大学
    # getweiboremark(name='shisu1949',index=6,num=-1)
    #喵星人星球
    # getweiboremark (name='234517972', index=3, num=-1)
    #全球影视指南
    # getweiboremark (name='2142513527', index=4, num=-1)
    #江苏校园事
    getweiboremark(name='6114482167', index=0, num=-1)
    #财经网
    # getweiboremark (name='caijing', index=8, num=-1)