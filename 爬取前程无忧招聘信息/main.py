import requests
import re
from lxml import etree
import pandas as pd
import time
from tqdm import tqdm
import warnings
warnings.filterwarnings("ignore")

headers = {
    "Host": "search.51job.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
}
session = requests.session()
session.headers = headers

def get_parse(url):
    html = session.get(url)
    if html.status_code ==200:
        get_html(html)
    else:
        print(html.status_code)

def get_html(html):
    content =html.text
    #招聘企业名称
    company_names = re.compile('"company_name":"(.*?)",',re.S|re.I)
    company_name = company_names.findall(content)
    #招聘企业规模
    companysize_texts = re.compile('"companysize_text":"(.*?)",', re.S | re.I)
    companysize_text = companysize_texts.findall(content)
    #招聘企业性质
    companytype_texts = re.compile('"companytype_text":"(.*?)",', re.S | re.I)
    companytype_text = companytype_texts.findall(content)
    #招聘工作地区
    workarea_texts = re.compile('"workarea_text":"(.*?)",', re.S | re.I)
    workarea_text = workarea_texts.findall(content)
    #招聘职位名称
    job_names = re.compile('"job_name":"(.*?)",', re.S | re.I)
    job_name = job_names.findall(content)
    #招聘岗位薪资
    providesalary_texts = re.compile('"providesalary_text":"(.*?)",', re.S | re.I)
    providesalary_text = providesalary_texts.findall(content)
    job_hrefs = re.compile('"job_href":"(.*?)",', re.S | re.I)
    job_href = job_hrefs.findall(content)

    JobDescribe = []
    providesalary = []
    for i in job_href:
        job_url = i.replace("\\","")
        html = session.get(job_url)
        html.encoding = "gbk"
        content = html.text
        dom_test = etree.HTML(content)
        job_describe = dom_test.xpath('//div[@class="tBorderTop_box"]//div[@class="bmsg job_msg inbox"]/p/text()')
        JobDescribe.append(job_describe)
    for pt in providesalary_text:
        p = pt.replace("\\","")
        providesalary.append(p)
    df = pd.DataFrame()
    df["企业名称"] = company_name
    df["企业规模"] = companysize_text
    df["企业性质"] = companytype_text
    df["工作地区"] = workarea_text
    df["职位名称"] = job_name
    df["岗位薪资"] = providesalary
    df["岗位描述"] = JobDescribe
    try:
        df.to_csv("前程无忧1.csv", mode="a+", header=None, index=None, encoding="gbk")
        print("写入成功")
    except:
        print("当页数据写入失败")
    time.sleep(1)


if __name__ == '__main__':
    for i in tqdm(range(1,2,1)):
        url = "https://search.51job.com/list/000000,000000,0000,00,9,99,%25E6%2599%25AF%25E5%258C%25BA%25E8%25AE%25B2%25E8%25A7%25A3%25E5%2591%2598,2,{}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=".format(i)
        get_parse(url)