import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.globals import ThemeType

def weibo_sum():
    df1 = pd.read_excel('./台湾文本-数据/微博/微博台海局势1-12月/1.xlsx').loc[:,['from']]
    sum_weibo = []
    for d1 in df1['from']:
        d1 = str(d1)
        d1 = d1[0:8]
        sum_weibo.append(d1)

    df2 = pd.read_excel('./台湾文本-数据/微博/微博台海局势1-12月/2.xlsx').loc[:,['from']]
    for d2 in df2['from']:
        d2 = str(d2)
        d2 = d2[0:8]
        if 'nan' not in d2:
            sum_weibo.append(d2)

    df3 = pd.read_excel('./台湾文本-数据/微博/微博台海局势1-12月/3.xlsx').loc[:,['from']]
    for d3 in df3['from']:
        d3 = str(d3)
        d3 = d3[0:8]
        if 'nan' not in d3:
            sum_weibo.append(d3)

    df4 = pd.read_excel('./台湾文本-数据/微博/微博台海局势1-12月/4.xlsx').loc[:,['from']]
    for d4 in df4['from']:
        d4 = str(d4)
        d4 = d4[0:8]
        if 'nan' not in d4:
            sum_weibo.append(d4)

    df5 = pd.read_excel('./台湾文本-数据/微博/微博台海局势1-12月/4.xlsx').loc[:,['from']]
    for d5 in df5['from']:
        d5 = str(d5)
        d5 = d5[0:8]
        if 'nan' not in d5:
            sum_weibo.append(d5)

    df6 = pd.read_excel('./台湾文本-数据/微博/微博台海局势1-12月/6.xlsx').loc[:,['from']]
    for d6 in df6['from']:
        d6 = str(d6)
        d6 = d6[0:8]
        if 'nan' not in d6:
            sum_weibo.append(d6)

    df7 = pd.read_excel('./台湾文本-数据/微博/微博台海局势1-12月/7.xlsx').loc[:, ['from']]
    for d7 in df7['from']:
        d7 = str(d7)
        d7 = d7[0:8]
        if 'nan' not in d7:
            sum_weibo.append(d7)

    df8 = pd.read_excel('./台湾文本-数据/微博/微博台海局势1-12月/8.xlsx').loc[:, ['from']]
    for d8 in df8['from']:
        d8 = str(d8)
        d8 = d8[0:8]
        if 'nan' not in d8:
            sum_weibo.append(d8)

    df9 = pd.read_excel('./台湾文本-数据/微博/微博台海局势1-12月/9.xlsx').loc[:, ['from']]
    for d9 in df9['from']:
        d9 = str(d9)
        d9 = d9[0:8]
        if 'nan' not in d9:
            sum_weibo.append(d9)

    df10 = pd.read_excel('./台湾文本-数据/微博/微博台海局势1-12月/10.xlsx').loc[:, ['from']]
    for d10 in df10['from']:
        d10 = str(d10)
        d10 = d10[0:8]
        if 'nan' not in d10:
            sum_weibo.append(d10)

    df11 = pd.read_excel('./台湾文本-数据/微博/微博台海局势1-12月/11.xlsx').loc[:, ['from']]
    for d11 in df11['from']:
        d11 = str(d11)
        d11 = d11[0:8]
        if 'nan' not in d11:
            sum_weibo.append(d11)

    df12 = pd.read_excel('./台湾文本-数据/微博/微博台海局势1-12月/12.xlsx').loc[:, ['from']]
    for d12 in df12['from']:
        d12 = str(d12)
        d12 = d12[0:8]
        if 'nan' not in d12:
            sum_weibo.append(d12)

    df13 = pd.read_excel('./台湾文本-数据/微博/两岸关系微博.xlsx').loc[:, ['from']]
    for d13 in df13['from']:
        d13 = str(d13)
        d13 = d13[0:8]
        if 'nan' not in d13:
            sum_weibo.append(d13)

    df14 = pd.read_excel('./台湾文本-数据/微博/微博中国内政.xlsx').loc[:, ['from']]
    for d14 in df14['from']:
        d14 = str(d14)
        d14 = d14[0:8]
        if 'nan' not in d14:
            sum_weibo.append(d14)

    df15 = pd.read_excel('./台湾文本-数据/微博/微博分裂势力.xlsx').loc[:, ['from']]
    for d15 in df15['from']:
        d15 = str(d15)
        d15 = d15[0:8]
        if 'nan' not in d15:
            sum_weibo.append(d15)

    df16 = pd.read_excel('./台湾文本-数据/微博/微博台军.xlsx').loc[:, ['from']]
    for d16 in df16['from']:
        d16 = str(d16)
        d16 = d16[0:8]
        if 'nan' not in d16:
            sum_weibo.append(d16)

    df17 = pd.read_excel('./台湾文本-数据/微博/微博台湾政治.xlsx').loc[:, ['from']]
    for d17 in df17['from']:
        d17 = str(d17)
        d17 = d17[0:8]
        if 'nan' not in d17:
            sum_weibo.append(d17)

    df18 = pd.read_excel('./台湾文本-数据/微博/微博台湾海峡.xlsx').loc[:, ['from']]
    for d18 in df18['from']:
        d18 = str(d18)
        d18 = d18[0:8]
        if 'nan' not in d18:
            sum_weibo.append(d18)

    df19 = pd.read_excel('./台湾文本-数据/微博/微博台湾牌.xlsx').loc[:, ['from']]
    for d19 in df19['from']:
        d19 = str(d19)
        d19 = d19[0:8]
        if 'nan' not in d19:
            sum_weibo.append(d19)

    df20 = pd.read_excel('./台湾文本-数据/微博/微博台湾疫情.xlsx').loc[:, ['from']]
    for d20 in df20['from']:
        d20 = str(d20)
        d20 = d20[0:8]
        if 'nan' not in d20:
            sum_weibo.append(d20)

    df21 = pd.read_excel('./台湾文本-数据/微博/微博台湾经济.xlsx').loc[:, ['from']]
    for d21 in df21['from']:
        d21 = str(d21)
        d21 = d21[0:8]
        if 'nan' not in d21:
            sum_weibo.append(d21)

    df22 = pd.read_excel('./台湾文本-数据/微博/微博台独.xlsx').loc[:, ['from']]
    for d22 in df22['from']:
        d22 = str(d22)
        d22 = d22[0:8]
        if 'nan' not in d22:
            sum_weibo.append(d22)

    df23 = pd.read_excel('./台湾文本-数据/微博/微博和平统一.xlsx').loc[:, ['from']]
    for d23 in df23['from']:
        d23 = str(d23)
        d23 = d23[0:8]
        if 'nan' not in d23:
            sum_weibo.append(d23)

    df24 = pd.read_excel('./台湾文本-数据/微博/微博拜登台湾.xlsx').loc[:, ['from']]
    for d24 in df24['from']:
        d24 = str(d24)
        d24 = d24[0:8]
        if 'nan' not in d24:
            sum_weibo.append(d24)

    df25 = pd.read_excel('./台湾文本-数据/微博/微博武统.xlsx').loc[:, ['from']]
    for d25 in df25['from']:
        d25 = str(d25)
        d25 = d25[0:8]
        if 'nan' not in d25:
            sum_weibo.append(d25)

    df26 = pd.read_excel('./台湾文本-数据/微博/微博特朗普台湾.xlsx').loc[:, ['from']]
    for d26 in df26['from']:
        d26 = str(d26)
        d26 = d26[0:8]
        if 'nan' not in d26:
            sum_weibo.append(d26)

    df27 = pd.read_excel('./台湾文本-数据/微博/微博美台.xlsx').loc[:, ['from']]
    for d27 in df27['from']:
        d27 = str(d27)
        d27 = d27[0:8]
        if 'nan' not in d27:
            sum_weibo.append(d27)

    df28 = pd.read_excel('./台湾文本-数据/微博/微博蔡英文.xlsx').loc[:, ['from1']]
    for d28 in df28['from1']:
        d28 = str(d28)
        d28 = d28[0:8]
        if 'nan' not in d28:
            sum_weibo.append(d28)

    df29 = pd.read_excel('./台湾文本-数据/微博/微博领土主权.xlsx').loc[:, ['from']]
    for d29 in df29['from']:
        d29 = str(d29)
        d29 = d29[0:8]
        if 'nan' not in d29:
            sum_weibo.append(d29)

    d = {}
    for s in sum_weibo:
        d[s] = d.get(s, 0) + 1
    ls = list(d.items())
    ls.sort(key=lambda x: x[0], reverse=True)
    del ls[-10:]
    del ls[0]
    return ls

def huanqiuw_sum():
    df = pd.read_excel('./台湾文本-数据/环球网/环球网台海.xlsx').loc[:, ['time']]
    sum_list = []
    for d in df['time']:
        d = str(d)
        d = d[0:7]
        if 'nan' not in d:
            sum_list.append(d)
    d = {}
    for s in sum_list:
        d[s] = d.get(s, 0) + 1
    ls = list(d.items())
    ls.sort(key=lambda x: x[0], reverse=False)
    return ls

def zhongguotaiwanwang():
    df1 = pd.read_excel('./台湾文本-数据/中国台湾网/两岸.xlsx').loc[:, ['info']]
    sum_list = []
    for d1 in df1['info']:
        d1 = str(d1)
        d1 = d1[0:7]
        if 'nan' not in d1:
            sum_list.append(d1)

    df2 = pd.read_excel('./台湾文本-数据/中国台湾网/两岸快评.xlsx').loc[:, ['info']]
    for d2 in df2['info']:
        d2 = str(d2)
        d2 = d2[0:7]
        if 'nan' not in d2:
            sum_list.append(d2)

    df3 = pd.read_excel('./台湾文本-数据/中国台湾网/台商.xlsx').loc[:, ['info']]
    for d3 in df3['info']:
        d3 = str(d3)
        d3 = d3[0:7]
        if 'nan' not in d3:
            sum_list.append(d3)

    df4 = pd.read_excel('./台湾文本-数据/中国台湾网/台湾自2020年12月-2021.1.4时事.xlsx').loc[:, ['info']]
    for d4 in df4['info']:
        d4 = str(d4)
        d4 = d4[0:7]
        if 'nan' not in d4:
            sum_list.append(d4)

    df5 = pd.read_excel('./台湾文本-数据/中国台湾网/文化.xlsx').loc[:, ['info']]
    for d5 in df5['info']:
        d5 = str(d5)
        d5 = d5[0:7]
        if 'nan' not in d5:
            sum_list.append(d5)

    df6 = pd.read_excel('./台湾文本-数据/中国台湾网/海峡时评.xlsx').loc[:, ['info']]
    for d6 in df6['info']:
        d6 = str(d6)
        d6 = d6[0:7]
        if 'nan' not in d6:
            sum_list.append(d6)

    df7 = pd.read_excel('./台湾文本-数据/中国台湾网/经贸.xlsx').loc[:, ['info']]
    for d7 in df7['info']:
        d7 = str(d7)
        d7 = d7[0:7]
        if 'nan' not in d7:
            sum_list.append(d7)

    df8 = pd.read_excel('./台湾文本-数据/中国台湾网/网友专栏.xlsx').loc[:, ['日期时间']]
    for d8 in df8['日期时间']:
        d8 = str(d8).replace('年','-')
        d8 = d8[0:7]
        if 'nan' not in d8:
            sum_list.append(d8)

    df9 = pd.read_excel('./台湾文本-数据/中国台湾网/网友快言.xlsx').loc[:, ['info']]
    for d9 in df9['info']:
        d9 = str(d9)
        d9 = d9[0:7]
        if 'nan' not in d9:
            sum_list.append(d9)

    df10 = pd.read_excel('./台湾文本-数据/中国台湾网/萧萧话两岸.xlsx').loc[:, ['info']]
    for d10 in df10['info']:
        d10 = str(d10)
        d10 = d10[0:7]
        if 'nan' not in d10:
            sum_list.append(d10)

    df11 = pd.read_excel('./台湾文本-数据/中国台湾网/部委.xlsx').loc[:, ['info']]
    for d11 in df11['info']:
        d11 = str(d11)
        d11 = d11[0:7]
        if 'nan' not in d11:
            sum_list.append(d11)

    d = {}
    for s in sum_list:
        d[s] = d.get(s, 0) + 1
    ls = list(d.items())
    ls.sort(key=lambda x: x[0], reverse=True)
    del ls[-13:]
    return ls

def zhihu():
    df = pd.read_excel('./台湾文本-数据/知乎/知乎台海局势的数据.xlsx').loc[:, ['ContentItem-action']]
    sum_list = []
    for d in df['ContentItem-action']:
        d = str(d)
        d = d[0:7]
        if 'nan' not in d:
            sum_list.append(d)
    d = {}
    for s in sum_list:
        d[s] = d.get(s, 0) + 1
    ls = list(d.items())
    ls.sort(key=lambda x: x[0], reverse=False)
    del ls[0:13]
    del ls[-2:]
    return ls

def ribao_sum():
    sum_list = []
    df = pd.read_excel('./台湾文本-数据/中国日报网/中国日报网两岸关系.xlsx').loc[:, ['日期时间']]
    for d in df['日期时间']:
        d = str(d)
        d = d.replace('年', '-')
        d = d[0:7]
        if 'nan' not in d:
            sum_list.append(d)

    df2 = pd.read_excel('./台湾文本-数据/中国日报网/中国日报网台海局势.xlsx').loc[:, ['日期时间']]
    for d2 in df2['日期时间']:
        d2 = str(d2)
        d2 = d2.replace('年', '-')
        d2 = d2[0:7]
        if 'nan' not in d2:
            sum_list.append(d2)

    df3 = pd.read_excel('./台湾文本-数据/中国日报网/中国日报网台湾牌.xlsx').loc[:, ['日期时间']]
    for d3 in df3['日期时间']:
        d3 = str(d3)
        d3 = d3.replace('年', '-')
        d3 = d3[0:7]
        if 'nan' not in d3:
            sum_list.append(d3)

    df4 = pd.read_excel('./台湾文本-数据/中国日报网/中国日报网和平统一.xlsx').loc[:, ['日期时间']]
    for d4 in df4['日期时间']:
        d4 = str(d4)
        d4 = d4.replace('年', '-')
        d4 = d4[0:7]
        if 'nan' not in d4:
            sum_list.append(d4)

    df5 = pd.read_excel('./台湾文本-数据/中国日报网/微博民进党.xlsx').loc[:, ['from']]
    for d5 in df5['from']:
        d5 = str(d5)
        d5 = d5.replace('年','-')
        d5 = d5[0:7]
        if 'nan' not in d5:
            sum_list.append(d5)

    d = {}
    for s in sum_list:
        d[s] = d.get(s, 0) + 1
    ls = list(d.items())
    ls.sort(key=lambda x: x[0], reverse=False)
    return ls

def zhongxing_sum():
    sum_list = []
    df = pd.read_excel('./台湾文本-数据/中新网/中新网两岸关系.xlsx').loc[:, ['日期时间']]
    for d in df['日期时间']:
        d = str(d)
        d = d[0:7]
        if 'nan' not in d:
            sum_list.append(d)

    df2 = pd.read_excel('./台湾文本-数据/中新网/中新网台海局势.xlsx').loc[:, ['日期时间']]
    for d2 in df2['日期时间']:
        d2 = str(d2)
        d2 = d2[0:7]
        if 'nan' not in d2:
            sum_list.append(d2)

    df3 = pd.read_excel('./台湾文本-数据/中新网/中新网台军.xlsx').loc[:, ['日期时间']]
    for d3 in df3['日期时间']:
        d3 = str(d3)
        d3 = d3[0:7]
        if 'nan' not in d3:
            sum_list.append(d3)

    df4 = pd.read_excel('./台湾文本-数据/中新网/中新网台湾政治.xlsx').loc[:, ['日期时间']]
    for d4 in df4['日期时间']:
        d4 = str(d4)
        d4 = d4[0:7]
        if 'nan' not in d4:
            sum_list.append(d4)

    df5 = pd.read_excel('./台湾文本-数据/中新网/中新网台湾海峡.xlsx').loc[:, ['日期时间']]
    for d5 in df5['日期时间']:
        d5 = str(d5)
        d5 = d5[0:7]
        if 'nan' not in d5:
            sum_list.append(d5)

    df6 = pd.read_excel('./台湾文本-数据/中新网/中新网台湾牌.xlsx').loc[:, ['日期时间']]
    for d6 in df6['日期时间']:
        d6 = str(d6)
        d6 = d6[0:7]
        if 'nan' not in d6:
            sum_list.append(d6)

    df7 = pd.read_excel('./台湾文本-数据/中新网/中新网台湾疫情.xlsx').loc[:, ['日期时间']]
    for d7 in df7['日期时间']:
        d7 = str(d7)
        d7 = d7[0:7]
        if 'nan' not in d7:
            sum_list.append(d7)

    df8 = pd.read_excel('./台湾文本-数据/中新网/中新网台湾经济.xlsx').loc[:, ['日期时间']]
    for d8 in df8['日期时间']:
        d8 = str(d8)
        d8 = d8[0:7]
        if 'nan' not in d8:
            sum_list.append(d8)

    df9 = pd.read_excel('./台湾文本-数据/中新网/中新网台独.xlsx').loc[:, ['日期时间']]
    for d9 in df9['日期时间']:
        d9 = str(d9)
        d9 = d9[0:7]
        if 'nan' not in d9:
            sum_list.append(d9)

    df10 = pd.read_excel('./台湾文本-数据/中新网/中新网和平统一.xlsx').loc[:, ['日期时间']]
    for d10 in df10['日期时间']:
        d10 = str(d10)
        d10 = d10[0:7]
        if 'nan' not in d10:
            sum_list.append(d10)

    df11 = pd.read_excel('./台湾文本-数据/中新网/中新网武统.xlsx').loc[:, ['日期时间']]
    for d11 in df11['日期时间']:
        d11 = str(d11)
        d11 = d11[0:7]
        if 'nan' not in d11:
            sum_list.append(d11)

    df12 = pd.read_excel('./台湾文本-数据/中新网/中新网民进党.xlsx').loc[:, ['日期时间']]
    for d12 in df12['日期时间']:
        d12 = str(d12)
        d12 = d12[0:7]
        if 'nan' not in d12:
            sum_list.append(d12)

    df13 = pd.read_excel('./台湾文本-数据/中新网/中新网美台.xlsx').loc[:, ['日期时间']]
    for d13 in df13['日期时间']:
        d13 = str(d13)
        d13 = d13[0:7]
        if 'nan' not in d13:
            sum_list.append(d13)

    df14 = pd.read_excel('./台湾文本-数据/中新网/中新网蔡英文.xlsx').loc[:, ['日期时间']]
    for d14 in df14['日期时间']:
        d14 = str(d14)
        d14 = d14[0:7]
        if 'nan' not in d14:
            sum_list.append(d14)

    d = {}
    for s in sum_list:
        d[s] = d.get(s, 0) + 1
    ls = list(d.items())
    ls.sort(key=lambda x: x[0], reverse=False)
    del ls[0:46]
    return ls


def jinri_sum():
    sum_list = []
    df = pd.read_excel('./台湾文本-数据/今日头条/今日头条两岸关系.xlsx').loc[:, ['lbtn1']]
    for d in df['lbtn1']:
        d = str(d)
        if 'nan' not in d:
            sum_list.append(d)

    df2 = pd.read_excel('./台湾文本-数据/今日头条/今日头条台军.xlsx').loc[:, ['lbtn1']]
    for d2 in df2['lbtn1']:
        d2 = str(d2)
        if 'nan' not in d2:
            sum_list.append(d2)

    df3 = pd.read_excel('./台湾文本-数据/今日头条/今日头条台海局势.xlsx').loc[:, ['time']]
    for d3 in df3['time']:
        d3 = str(d3)
        if 'nan' not in d3:
            sum_list.append(d3)

    df4 = pd.read_excel('./台湾文本-数据/今日头条/今日头条台湾政治.xlsx').loc[:, ['lbtn1']]
    for d4 in df4['lbtn1']:
        d4 = str(d4)
        if 'nan' not in d4:
            sum_list.append(d4)

    df5 = pd.read_excel('./台湾文本-数据/今日头条/今日头条台湾海峡.xlsx').loc[:, ['lbtn1']]
    for d5 in df5['lbtn1']:
        d5 = str(d5)
        if 'nan' not in d5:
            sum_list.append(d5)

    df6 = pd.read_excel('./台湾文本-数据/今日头条/今日头条台湾牌.xlsx').loc[:, ['lbtn1']]
    for d6 in df6['lbtn1']:
        d6 = str(d6)
        if 'nan' not in d6:
            sum_list.append(d6)

    df7 = pd.read_excel('./台湾文本-数据/今日头条/今日头条台湾疫情.xlsx').loc[:, ['lbtn1']]
    for d7 in df7['lbtn1']:
        d7 = str(d7)
        if 'nan' not in d7:
            sum_list.append(d7)

    df8 = pd.read_excel('./台湾文本-数据/今日头条/今日头条台独.xlsx').loc[:, ['lbtn1']]
    for d8 in df8['lbtn1']:
        d8 = str(d8)
        if 'nan' not in d8:
            sum_list.append(d8)

    df9 = pd.read_excel('./台湾文本-数据/今日头条/今日头条和平统一.xlsx').loc[:, ['lbtn1']]
    for d9 in df9['lbtn1']:
        d9 = str(d9)
        if 'nan' not in d9:
            sum_list.append(d9)

    df10 = pd.read_excel('./台湾文本-数据/今日头条/今日头条拜登台湾.xlsx').loc[:, ['lbtn1']]
    for d10 in df10['lbtn1']:
        d10 = str(d10)
        if 'nan' not in d10:
            sum_list.append(d10)

    df11 = pd.read_excel('./台湾文本-数据/今日头条/今日头条武统.xlsx').loc[:, ['lbtn1']]
    for d11 in df11['lbtn1']:
        d11 = str(d11)
        if 'nan' not in d11:
            sum_list.append(d11)

    df12 = pd.read_excel('./台湾文本-数据/今日头条/今日头条民进党.xlsx').loc[:, ['lbtn1']]
    for d12 in df12['lbtn1']:
        d12 = str(d12)
        if 'nan' not in d12:
            sum_list.append(d12)

    df13= pd.read_excel('./台湾文本-数据/今日头条/今日头条特朗普台湾.xlsx').loc[:, ['lbtn1']]
    for d13 in df13['lbtn1']:
        d13 = str(d13)
        if 'nan' not in d13:
            sum_list.append(d13)

    df14 = pd.read_excel('./台湾文本-数据/今日头条/今日头条美台.xlsx').loc[:, ['lbtn1']]
    for d14 in df14['lbtn1']:
        d14 = str(d14)
        if 'nan' not in d14:
            sum_list.append(d14)

    df15 = pd.read_excel('./台湾文本-数据/今日头条/今日头条蔡英文.xlsx').loc[:, ['lbtn1']]
    for d15 in df15['lbtn1']:
        d15 = str(d15)
        if 'nan' not in d15:
            sum_list.append(d15)

    df16 = pd.read_excel('./台湾文本-数据/今日头条/台湾经济.xlsx').loc[:, ['lbtn1']]
    for d16 in df16['lbtn1']:
        d16 = str(d16)
        if 'nan' not in d16:
            sum_list.append(d16)

    d = {}
    for s in sum_list:
        d[s] = d.get(s, 0) + 1
    ls = list(d.items())
    ls.sort(key=lambda x: x[0], reverse=False)

    return ls

def guangming_sum():
    sum_list = []
    df = pd.read_excel('./台湾文本-数据/光明网/光明网两岸关系.xlsx').loc[:, ['日期时间']]
    for d in df['日期时间']:
        d = str(d)
        d = d[0:7]
        if 'nan' not in d:
            sum_list.append(d)

    df2 = pd.read_excel('./台湾文本-数据/光明网/光明网台军.xlsx').loc[:, ['m-news-box2']]
    for d2 in df2['m-news-box2']:
        d2 = str(d2)
        d2 = d2[0:7]
        if 'nan' not in d2:
            sum_list.append(d2)



    df4 = pd.read_excel('./台湾文本-数据/光明网/光明网台湾政治.xlsx').loc[:, ['m-news-box1']]
    for d4 in df4['m-news-box1']:
        d4 = str(d4)
        d4 = d4[0:7]
        if 'nan' not in d4:
            sum_list.append(d4)

    df5 = pd.read_excel('./台湾文本-数据/光明网/光明网台湾海峡.xlsx').loc[:, ['m-news-box1']]
    for d5 in df5['m-news-box1']:
        d5 = str(d5)
        d5 = d5[0:7]
        if 'nan' not in d5:
            sum_list.append(d5)

    df6 = pd.read_excel('./台湾文本-数据/光明网/光明网台湾牌.xlsx').loc[:, ['日期时间']]
    for d6 in df6['日期时间']:
        d6 = str(d6)
        d6 = d6[0:7]
        if 'nan' not in d6:
            sum_list.append(d6)

    df7 = pd.read_excel('./台湾文本-数据/光明网/光明网台湾疫情.xlsx').loc[:, ['m-news-box1']]
    for d7 in df7['m-news-box1']:
        d7 = str(d7)
        d7 = d7[0:7]
        if 'nan' not in d7:
            sum_list.append(d7)

    df8 = pd.read_excel('./台湾文本-数据/光明网/光明网台湾经济.xlsx').loc[:, ['m-news-box1']]
    for d8 in df8['m-news-box1']:
        d8 = str(d8)
        d8 = d8[0:7]
        if 'nan' not in d8:
            sum_list.append(d8)

    df9 = pd.read_excel('./台湾文本-数据/光明网/光明网台独.xlsx').loc[:, ['m-news-box1']]
    for d9 in df9['m-news-box1']:
        d9 = str(d9)
        d9 = d9[0:7]
        if 'nan' not in d9:
            sum_list.append(d9)

    df10 = pd.read_excel('./台湾文本-数据/光明网/光明网和平统一.xlsx').loc[:, ['日期时间']]
    for d10 in df10['日期时间']:
        d10 = str(d10)
        d10 = d10[0:7]
        if 'nan' not in d10:
            sum_list.append(d10)

    df11 = pd.read_excel('./台湾文本-数据/光明网/光明网武统.xlsx').loc[:, ['m-news-box1']]
    for d11 in df11['m-news-box1']:
        d11 = str(d11)
        d11 = d11[0:7]
        if 'nan' not in d11:
            sum_list.append(d11)

    df12 = pd.read_excel('./台湾文本-数据/光明网/光明网民进党.xlsx').loc[:, ['m-news-box1']]
    for d12 in df12['m-news-box1']:
        d12 = str(d12)
        d12 = d12[0:7]
        if 'nan' not in d12:
            sum_list.append(d12)

    df13 = pd.read_excel('./台湾文本-数据/光明网/光明网蔡英文.xlsx').loc[:, ['m-news-box1']]
    for d13 in df13['m-news-box1']:
        d13 = str(d13)
        d13 = d13[0:7]
        if 'nan' not in d13:
            sum_list.append(d13)

    d = {}
    for s in sum_list:
        d[s] = d.get(s, 0) + 1
    ls = list(d.items())
    ls.sort(key=lambda x: x[0], reverse=False)
    del ls[0:20]
    return ls


def fenghuan_sum():
    sum_list = []
    df = pd.read_excel('./台湾文本-数据/凤凰网/凤凰台军.xlsx').loc[:, ['字段2']]
    for d in df['字段2']:
        d = str(d)
        d = d[0:7]
        if 'nan' not in d:
            sum_list.append(d)


    df3 = pd.read_excel('./台湾文本-数据/凤凰网/凤凰台湾海峡.xlsx').loc[:, ['字段2']]
    for d3 in df3['字段2']:
        d3 = str(d3)
        d3 = d3[0:7]
        if 'nan' not in d3:
            sum_list.append(d3)


    df6 = pd.read_excel('./台湾文本-数据/凤凰网/凤凰台独.xlsx').loc[:, ['字段2']]
    for d6 in df6['字段2']:
        d6 = str(d6)
        d6 = d6[0:7]
        if 'nan' not in d6:
            sum_list.append(d6)

    df9 = pd.read_excel('./台湾文本-数据/凤凰网/凤凰民进党.xlsx').loc[:, ['字段2']]
    for d9 in df9['字段2']:
        d9 = str(d9)
        d9 = d9[0:7]
        if 'nan' not in d9:
            sum_list.append(d9)

    df11 = pd.read_excel('./台湾文本-数据/凤凰网/凤凰网两岸关系.xlsx').loc[:, ['字段2']]
    for d11 in df11['字段2']:
        d11 = str(d11)
        d11 = d11[0:7]
        if 'nan' not in d11:
            sum_list.append(d11)

    df14 = pd.read_excel('./台湾文本-数据/凤凰网/凤凰网和平统一.xlsx').loc[:, ['字段2']]
    for d14 in df14['字段2']:
        d14 = str(d14)
        d14 = d14[0:7]
        if 'nan' not in d14:
            sum_list.append(d14)


    d = {}
    for s in sum_list:
        d[s] = d.get(s, 0) + 1
    ls = list(d.items())
    ls.sort(key=lambda x: x[0], reverse=False)
    del ls[-18:]
    del ls[0:36]
    ls.append(('2021/01',36))
    return ls

def xinhua_sum():
    sum_list = []
    df = pd.read_excel('./台湾文本-数据/新华网/新华网两岸关系.xlsx').loc[:, ['日期时间']]
    for d in df['日期时间']:
        d = str(d)
        d = d.replace('新华网\\u2003\\t\\t\\t\\t', '')
        d = d[0:7]
        if 'nan' not in d:
            sum_list.append(d)


    df3 = pd.read_excel('./台湾文本-数据/新华网/新华网台海局势.xlsx').loc[:, ['newstime']]
    for d3 in df3['newstime']:
        d3 = str(d3)
        d3 = d3.replace('新华网\\u2003\\t\\t\\t\\t', '')
        d3 = d3[0:7]
        if 'nan' not in d3:
            sum_list.append(d3)

    df4 = pd.read_excel('./台湾文本-数据/新华网/新华网台湾政治.xlsx').loc[:, ['newstime']]
    for d4 in df4['newstime']:
        d4 = str(d4)
        d4 = d4.replace('新华网\\u2003\\t\\t\\t\\t', '')
        d4 = d4[0:7]
        if 'nan' not in d4:
            sum_list.append(d4)

    df5 = pd.read_excel('./台湾文本-数据/新华网/新华网台湾海峡.xlsx').loc[:, ['newstime']]
    for d5 in df5['newstime']:
        d5 = str(d5)
        d5 = d5.replace('新华网\\u2003\\t\\t\\t\\t', '')
        d5 = d5[0:7]
        if 'nan' not in d5:
            sum_list.append(d5)

    df6 = pd.read_excel('./台湾文本-数据/新华网/新华网台湾牌.xlsx').loc[:, ['newstime']]
    for d6 in df6['newstime']:
        d6 = str(d6)
        d6 = d6.replace('新华网\\u2003\\t\\t\\t\\t', '')
        d6 = d6[0:7]
        if 'nan' not in d6:
            sum_list.append(d6)

    df7 = pd.read_excel('./台湾文本-数据/新华网/新华网台湾疫情.xlsx').loc[:, ['newstime']]
    for d7 in df7['newstime']:
        d7 = str(d7)
        d7 = d7.replace('新华网\\u2003\\t\\t\\t\\t', '')
        d7 = d7[0:7]
        if 'nan' not in d7:
            sum_list.append(d7)

    df8 = pd.read_excel('./台湾文本-数据/新华网/新华网台湾经济.xlsx').loc[:, ['newstime']]
    for d8 in df8['newstime']:
        d8 = str(d8)
        d8 = d8.replace('新华网\\u2003\\t\\t\\t\\t', '')
        d8 = d8[0:7]
        if 'nan' not in d8:
            sum_list.append(d8)

    df9 = pd.read_excel('./台湾文本-数据/新华网/新华网台独.xlsx').loc[:, ['newstime']]
    for d9 in df9['newstime']:
        d9 = str(d9)
        d9 = d9.replace('新华网\\u2003\\t\\t\\t\\t', '')
        d9 = d9[0:7]
        if 'nan' not in d9:
            sum_list.append(d9)

    df10 = pd.read_excel('./台湾文本-数据/新华网/新华网和平统一.xlsx').loc[:, ['newstime']]
    for d10 in df10['newstime']:
        d10 = str(d10)
        d10 = d10.replace('新华网\\u2003\\t\\t\\t\\t', '')
        d10 = d10[0:7]
        if 'nan' not in d10:
            sum_list.append(d10)

    df11 = pd.read_excel('./台湾文本-数据/新华网/新华网武统.xlsx').loc[:, ['newstime']]
    for d11 in df11['newstime']:
        d11 = str(d11)
        d11 = d11.replace('新华网\\u2003\\t\\t\\t\\t', '')
        d11 = d11[0:7]
        if 'nan' not in d11:
            sum_list.append(d11)

    df12 = pd.read_excel('./台湾文本-数据/新华网/新华网民进党.xlsx').loc[:, ['newstime']]
    for d12 in df12['newstime']:
        d12 = str(d12)
        d12 = d12.replace('新华网\\u2003\\t\\t\\t\\t', '')
        d12 = d12[0:7]
        if 'nan' not in d12:
            sum_list.append(d12)

    df13 = pd.read_excel('./台湾文本-数据/新华网/新华网美台.xlsx').loc[:, ['newstime']]
    for d13 in df13['newstime']:
        d13 = str(d13)
        d13 = d13.replace('新华网\\u2003\\t\\t\\t\\t', '')
        d13 = d13[0:7]
        if 'nan' not in d13:
            sum_list.append(d13)

    df14 = pd.read_excel('./台湾文本-数据/新华网/新华网蔡英文.xlsx').loc[:, ['newstime']]
    for d14 in df14['newstime']:
        d14 = str(d14)
        d14 = d14.replace('新华网\\u2003\\t\\t\\t\\t', '')
        d14 = d14[0:7]
        d14 = d14.replace('新华网\\u2003\\t\\t\\t\\t','')
        if 'nan' not in d14:
            sum_list.append(d14)

    d = {}
    for s in sum_list:
        d[s] = d.get(s, 0) + 1
    ls = list(d.items())
    ls.sort(key=lambda x: x[0], reverse=False)
    del ls[-13:]
    del ls[0:10]
    ls.append(('2020-02', 0))
    ls.append(('2020-03', 0))
    ls.append(('2020-04', 0))
    ls.append(('2020-05', 0))
    ls.append(('2020-06', 0))
    ls.append(('2020-07', 0))
    ls.append(('2020-10', 0))
    ls.sort(key=lambda x: x[0], reverse=False)
    return ls


def terrace_line():
    list1 = weibo_sum()
    list1.sort(key=lambda x: x[0], reverse=False)
    x_data1 = []
    y_data1 = []
    for l in list1:
        x = l[0].replace('年','-').replace('月','')
        x_data1.append(x)
        y_data1.append(l[1])

    list2 = huanqiuw_sum()
    x_data2 = []
    y_data2 = []
    for l in list2:
        x_data2.append(l[0])
        y_data2.append(l[1])
    y_data2.insert(0,0)
    y_data2.insert(0,0)
    y_data2.insert(0,0)
    list3 = zhongguotaiwanwang()
    x_data3 = []
    y_data3 = []
    list3.sort(key=lambda x: x[0], reverse=False)
    for l in list3:
        x_data3.append(l[0])
        y_data3.append(l[1])
    list4 = zhihu()
    x_data4 = []
    y_data4 = []
    for l in list4:
        x_data4.append(l[0])
        y_data4.append(l[1])
    y_data4.insert(1,0)

    list5 = ribao_sum()
    x_data5 = []
    y_data5 = []
    list5.sort(key=lambda x: x[0], reverse=False)
    for l in list5:
        x_data5.append(l[0])
        y_data5.append(l[1])


    list6 = zhongxing_sum()
    x_data6 = []
    y_data6 = []
    list6.sort(key=lambda x: x[0], reverse=False)
    for l in list6:
        x_data6.append(l[0])
        y_data6.append(l[1])


    list7 = jinri_sum()
    x_data7 = ['2020-01', '2020-02', '2020-03', '2020-04', '2020-05', '2020-06', '2020-07', '2020-08', '2020-09', '2020-10', '2020-11', '2020-12', '2021-01']
    y_data7 = [315, 255, 172, 84, 85, 30,42,36,64,14, 3, 141, 308]


    list8 = guangming_sum()
    x_data8 = []
    y_data8 = []
    list8.sort(key=lambda x: x[0], reverse=False)
    for l in list8:
        x_data8.append(l[0])
        y_data8.append(l[1])

    list9 = fenghuan_sum()
    x_data9 = []
    y_data9 = []
    list9.sort(key=lambda x: x[0], reverse=False)
    for l in list9:
        x = l[0].replace('/','-')
        x_data9.append(x)
        y_data9.append(l[1])

    list10 = xinhua_sum()
    x_data10 = []
    y_data10 = []
    list10.sort(key=lambda x: x[0], reverse=False)
    for l in list10:
        x_data10.append(l[0])
        y_data10.append(l[1])

    return x_data3,y_data1,y_data2,y_data3,y_data4,y_data5,y_data6,y_data7,y_data8,y_data9,y_data10
#     y_data2[0], y_data2[1],y_data2[2] = None, None,None
#     y_data4[1] = None
#     c = (
#             Line()
#             .add_xaxis(xaxis_data=x_data3)
#             .add_yaxis(
#                 series_name="微博",
#                 symbol="emptyCircle",
#                 is_symbol_show=True,
#                 color="#F2D7D5",
#                 y_axis=y_data1,
#                 label_opts=opts.LabelOpts(is_show=False),
#                 linestyle_opts=opts.LineStyleOpts(width=3)
#             )
#             .add_yaxis(
#                 series_name="环球网",
#                 symbol="emptyCircle",
#                 is_symbol_show=True,
#                 color="#C0392B",
#                 y_axis=y_data2,
#                 label_opts=opts.LabelOpts(is_show=False),
#                 linestyle_opts=opts.LineStyleOpts(width=3)
#             )
#             .add_yaxis(
#                 series_name="中国台湾网",
#                 symbol="emptyCircle",
#                 is_symbol_show=True,
#                 color="#641E16",
#                 y_axis=y_data3,
#                 label_opts=opts.LabelOpts(is_show=False),
#                 linestyle_opts=opts.LineStyleOpts(width=3)
#             )
#             .add_yaxis(
#                 series_name="知乎",
#                 symbol="emptyCircle",
#                 is_symbol_show=True,
#                 color="#9B59B6",
#                 y_axis=y_data4,
#                 label_opts=opts.LabelOpts(is_show=False),
#                 linestyle_opts=opts.LineStyleOpts(width=3)
#             )
#             .add_yaxis(
#                 series_name="中国日报网",
#                 symbol="emptyCircle",
#                 is_symbol_show=True,
#                 color="#512E5F",
#                 y_axis=y_data5,
#                 label_opts=opts.LabelOpts(is_show=False),
#                 linestyle_opts=opts.LineStyleOpts(width=3)
#             )
#             .add_yaxis(
#                 series_name="中新网",
#                 symbol="emptyCircle",
#                 is_symbol_show=True,
#                 color="#2980B9",
#                 y_axis=y_data6,
#                 label_opts=opts.LabelOpts(is_show=False),
#                 linestyle_opts=opts.LineStyleOpts(width=3)
#             )
#             .add_yaxis(
#                 series_name="今日头条",
#                 symbol="emptyCircle",
#                 is_symbol_show=True,
#                 color="#154360",
#                 y_axis=y_data7,
#                 label_opts=opts.LabelOpts(is_show=False),
#                 linestyle_opts=opts.LineStyleOpts(width=3)
#             )
#             .add_yaxis(
#                 series_name="光明网",
#                 symbol="emptyCircle",
#                 is_symbol_show=True,
#                 color="#3498DB",
#                 y_axis=y_data8,
#                 label_opts=opts.LabelOpts(is_show=False),
#                 linestyle_opts=opts.LineStyleOpts(width=3)
#             )
#             .add_yaxis(
#                 series_name="凤凰网",
#                 symbol="emptyCircle",
#                 is_symbol_show=True,
#                 color="#1ABC9C",
#                 y_axis=y_data9,
#                 label_opts=opts.LabelOpts(is_show=False),
#                 linestyle_opts=opts.LineStyleOpts(width=3)
#             )
#             .add_yaxis(
#                 series_name="新华网",
#                 symbol="emptyCircle",
#                 is_symbol_show=True,
#                 color="#0E6251",
#                 y_axis=y_data10,
#                 label_opts=opts.LabelOpts(is_show=False),
#                 linestyle_opts=opts.LineStyleOpts(width=3)
#             )
#             .set_global_opts(
#                 title_opts=opts.TitleOpts(title="各大平台台海局势热度"),
#                 tooltip_opts=opts.TooltipOpts(trigger="axis"),
#                 yaxis_opts=opts.AxisOpts(
#                     type_="value",
#                     axistick_opts=opts.AxisTickOpts(is_show=True),
#                     splitline_opts=opts.SplitLineOpts(is_show=True),
#                 ),
#                 xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False, axisline_opts=opts.AxisLineOpts(
#                     is_on_zero=False, linestyle_opts=opts.LineStyleOpts(color="#d14a61")
#                 )),
#             )
#             .render("./templates/各大平台台海热度折线图.html")
#         )
#
#
# if __name__ == '__main__':
#     terrace_line()