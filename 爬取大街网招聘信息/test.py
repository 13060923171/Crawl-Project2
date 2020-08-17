import requests
import re
from lxml import etree
import pandas as pd


headers = {
    'accept-language': 'zh-CN,zh;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-requested-with": "XMLHttpRequest",
    "referer": "https://so.dajie.com/job/search?keyword=%E6%97%85%E8%A1%8C%E9%A1%BE%E9%97%AE&from=job&clicktype=blank",
    'cookie': 'DJ_UVID=MTU5NzMyNzYzNjYxODExNTQw; _ga=GA1.2.2113787223.1597327635; _gid=GA1.2.1553008633.1597327635; MEIQIA_TRACK_ID=1g2znXAAakoQxBn9cSd2boCOxHN; _close_autoreg=1597334910407; _close_autoreg_num=5; DJ_RF=https%3A%2F%2Fwww.google.com%2F; DJ_EU=http%3A%2F%2Fwww.dajie.com%2F; Hm_lvt_6822a51ffa95d58bbe562e877f743b4f=1597327635,1597376484; SO_COOKIE_V2=91b1/LLiPqrkBlt1yP4yx5bqjB/kwilwrtdVxRTRUZqmpMjU/5RtNWD+oAPPvHtuxGQn3mc9q71BMOx/GNkNbKVMO6Mx3uVTF2yf; MEIQIA_VISIT_ID=1g4aoj42bTgLv7gu9WBU5MFANSd; USER_ACTION="request^A-^A-^Ajobdetail:^A-"; Hm_lpvt_6822a51ffa95d58bbe562e877f743b4f=1597376528',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
}

def get_parse(url):
    html = requests.get(url,headers =headers)
    if html.status_code ==200:
        get_html(html)
    else:
        print(html.status_code)

def get_html(html):
    content = html.text
    # 招聘企业名称
    company_names = re.compile('"compName":"(.*?)",', re.S | re.I)
    company_name = company_names.findall(content)
    # 招聘企业规模
    companysize_texts = re.compile('"scaleName":"(.*?)",', re.S | re.I)
    companysize_text = companysize_texts.findall(content)
    # 招聘工作地区
    workarea_texts = re.compile('"pubCity":"(.*?)",', re.S | re.I)
    workarea_text = workarea_texts.findall(content)
    # 招聘职位名称
    job_names = re.compile('"jobName":"(.*?)",', re.S | re.I)
    job_name = job_names.findall(content)
    # 招聘岗位薪资
    providesalary_texts = re.compile('"salary":"(.*?)",', re.S | re.I)
    providesalary_text = providesalary_texts.findall(content)

    jids = re.compile('"jid":"(.*?)",', re.S | re.I)
    jid = jids.findall(content)
    JobDescribe = []
    Companytype = []
    for i in range(len(jid)):
        href = "https://job.dajie.com/{}.html".format(jid[i])
        html = requests.get(href,headers=headers)
        content = html.text
        soup = etree.HTML(content)
        job_describe = soup.xpath("//pre/text()")
        companytype = soup.xpath('//ul[@class = "info"]/li/span/text()')[-1]
        JobDescribe.append(job_describe)
        Companytype.append(companytype)
    df = pd.DataFrame()
    df["企业名称"] = company_name
    df["企业规模"] = companysize_text
    df["企业性质"] = Companytype
    df["工作地区"] = workarea_text
    df["职位名称"] = job_name
    df["岗位薪资"] = providesalary_text[:-1]
    df["岗位描述"] = JobDescribe
    try:
        df.to_csv("大街网.csv", mode="a+", header=None, index=None, encoding="gbk")
        print("写入成功")
    except:
        print("当页数据写入失败")

if __name__ == '__main__':
    for i in range(1,3,1):
        url = "https://so.dajie.com/job/ajax/search/filter?keyword=%E6%97%85%E6%B8%B8&order=0&city=&recruitType=&salary=&experience=&page=1&positionFunction=&_CSRFToken=&ajax={}".format(i)
        get_parse(url)