import requests
import re
from lxml import etree
import pandas as pd
import time
from tqdm import tqdm
import hashlib
import random
from urllib import parse

md5 = hashlib.md5()
id = str(random.random())
md5.update(id.encode('utf-8'))
random_id = md5.hexdigest()
keyword = parse.quote(input("请输入你要的关键词:"))
def get_cookie():
    url = 'https://www.lagou.com/jobs/list_{}?labelWords=&fromSearch=true&suginput='.format(keyword)
    # 注意如果url中有中文，需要把中文字符编码后才可以正常运行
    headers = {
        'User-Agent': 'ozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400'
    }
    response = requests.get(url=url,headers=headers,allow_redirects=False)
    return response.cookies


def get_html(url,i):

    headers = {
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        'referer': 'https://www.lagou.com/jobs/list_{}?labelWords=&fromSearch=true&suginput='.format(keyword),
        'User-Agent': 'ozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400'
    }
    data = {
        'first': 'false',
        'pn':int(i),
        'kd': '景区讲解员',
        'sid':str(random_id),
    }
    s = requests.Session()
    response = s.post(url,data=data,headers=headers,cookies=get_cookie())
    # 这里的请求是post且获取的内容是json格式，因此使用json=data的方式才能获取到数据
    response.encoding = response.apparent_encoding  # 根据网页内容分析出的编码方式。
    content = response.text
    # 招聘企业名称
    company_names = re.compile('"companyFullName":"(.*?)",', re.S | re.I)
    company_name = company_names.findall(content)
    # 招聘企业规模
    companysize_texts = re.compile('"companySize":"(.*?)",', re.S | re.I)
    companysize_text = companysize_texts.findall(content)
    # 招聘企业性质
    companytype_texts = re.compile('"financeStage":"(.*?)",', re.S | re.I)
    companytype_text = companytype_texts.findall(content)
    # 招聘工作地区
    workarea_texts = re.compile('"city":"(.*?)",', re.S | re.I)
    workarea_text = workarea_texts.findall(content)
    # 招聘职位名称
    job_names = re.compile('"positionName":"(.*?)",', re.S | re.I)
    job_name = job_names.findall(content)
    # 招聘岗位薪资
    providesalary_texts = re.compile('"salary":"(.*?)",', re.S | re.I)
    providesalary_text = providesalary_texts.findall(content)
    job_hrefs = re.compile('"positionId":(.*?),"', re.S | re.I)
    job_href = job_hrefs.findall(content)
    params = {
        'show':str(random_id),
    }
    jobdescribe = []
    JobDescribe = []
    Jobname = []
    for j in job_href:
        href = "https://www.lagou.com/jobs/{}.html?show={}".format(j,str(random_id))
        html = requests.get(href, headers=headers, params=params, cookies=get_cookie())
        context = html.text
        soup = etree.HTML(context)
        job_describe = soup.xpath('//div[@class= "job-detail"]/p/text()')
        j_d = soup.xpath('//div[@class= "job-detail"]/text()')
        job_name = soup.xpath('//h1[@class = "name"]/text()')
        Jobname.append(job_name)
        JobDescribe.append(job_describe)
        jobdescribe.append(j_d)
    df = pd.DataFrame()
    df["企业名称"] = company_name
    df["企业规模"] = companysize_text
    df["企业性质"] = companytype_text
    df["工作地区"] = workarea_text
    df["职位名称"] = Jobname
    df["岗位薪资"] = providesalary_text
    df["岗位描述"] = JobDescribe
    df["岗位介绍"] = jobdescribe
    try:
        df.to_csv("拉勾网.csv", mode="a+", header=None, index=None, encoding="gbk")
        print("写入成功")
    except:
        print("当页数据写入失败")
    time.sleep(1)

if __name__ == '__main__':
    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    for i in tqdm(range(1,23,1)):
        get_html(url,i)