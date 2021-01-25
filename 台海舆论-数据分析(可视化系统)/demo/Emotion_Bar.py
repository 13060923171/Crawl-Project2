import pandas as pd
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.charts import Bar
from snownlp import SnowNLP

def weibo_sum():
    sum_weibo = []

    df1 = pd.read_excel('./台湾文本-数据/微博/微博台海局势1-12月/1.xlsx').loc[:,['txt']]
    for d1 in df1['txt']:
        d1 = str(d1)
        if 'nan' not in d1:
            sum_weibo.append(d1)

    df2 = pd.read_excel('./台湾文本-数据/微博/微博台海局势1-12月/2.xlsx').loc[:,['txt']]
    for d2 in df2['txt']:
        d2 = str(d2)
        if 'nan' not in d2:
            sum_weibo.append(d2)

    df3 = pd.read_excel('./台湾文本-数据/微博/微博台海局势1-12月/3.xlsx').loc[:,['txt']]
    for d3 in df3['txt']:
        d3 = str(d3)
        if 'nan' not in d3:
            sum_weibo.append(d3)

    df4 = pd.read_excel('./台湾文本-数据/微博/微博台海局势1-12月/4.xlsx').loc[:,['txt']]
    for d4 in df4['txt']:
        d4 = str(d4)
        if 'nan' not in d4:
            sum_weibo.append(d4)

    df5 = pd.read_excel('./台湾文本-数据/微博/微博台海局势1-12月/5.xlsx').loc[:,['txt']]
    for d5 in df5['txt']:
        d5 = str(d5)
        if 'nan' not in d5:
            sum_weibo.append(d5)

    df6 = pd.read_excel('./台湾文本-数据/微博/微博台海局势1-12月/6.xlsx').loc[:,['txt']]
    for d6 in df6['txt']:
        d6 = str(d6)
        if 'nan' not in d6:
            sum_weibo.append(d6)

    df7 = pd.read_excel('./台湾文本-数据/微博/微博台海局势1-12月/7.xlsx').loc[:,['txt']]
    for d7 in df7['txt']:
        d7 = str(d7)
        if 'nan' not in d7:
            sum_weibo.append(d7)

    df8 = pd.read_excel('./台湾文本-数据/微博/微博台海局势1-12月/8.xlsx').loc[:,['txt']]
    for d8 in df8['txt']:
        d8 = str(d8)
        if 'nan' not in d8:
            sum_weibo.append(d8)

    df9 = pd.read_excel('./台湾文本-数据/微博/微博台海局势1-12月/9.xlsx').loc[:,['txt']]
    for d9 in df9['txt']:
        d9 = str(d9)
        if 'nan' not in d9:
            sum_weibo.append(d9)

    df10 = pd.read_excel('./台湾文本-数据/微博/微博台海局势1-12月/10.xlsx').loc[:,['txt']]
    for d10 in df10['txt']:
        d10 = str(d10)
        if 'nan' not in d10:
            sum_weibo.append(d10)

    df11 = pd.read_excel('./台湾文本-数据/微博/微博台海局势1-12月/11.xlsx').loc[:,['txt']]
    for d11 in df11['txt']:
        d11 = str(d11)
        if 'nan' not in d11:
            sum_weibo.append(d11)

    df12 = pd.read_excel('./台湾文本-数据/微博/微博台海局势1-12月/12.xlsx').loc[:,['txt']]
    for d12 in df12['txt']:
        d12 = str(d12)
        if 'nan' not in d12:
            sum_weibo.append(d12)

    df13 = pd.read_excel('./台湾文本-数据/微博/两岸关系微博.xlsx').loc[:,['content']]
    for d13 in df13['content']:
        d13 = str(d13)
        if 'nan' not in d13:
            sum_weibo.append(d13)

    df14 = pd.read_excel('./台湾文本-数据/微博/微博中国内政.xlsx').loc[:, ['字段1']]
    for d14 in df14['字段1']:
        d14 = str(d14)
        if 'nan' not in d14:
            sum_weibo.append(d14)

    df15 = pd.read_excel('./台湾文本-数据/微博/微博分裂势力.xlsx').loc[:, ['content']]
    for d15 in df15['content']:
        d15 = str(d15)
        if 'nan' not in d15:
            sum_weibo.append(d15)

    df16 = pd.read_excel('./台湾文本-数据/微博/微博台军.xlsx').loc[:, ['字段1']]
    for d16 in df16['字段1']:
        d16 = str(d16)
        if 'nan' not in d16:
            sum_weibo.append(d16)

    df17 = pd.read_excel('./台湾文本-数据/微博/微博台湾政治.xlsx').loc[:, ['txt']]
    for d17 in df17['txt']:
        d17 = str(d17)
        if 'nan' not in d17:
            sum_weibo.append(d17)

    df18 = pd.read_excel('./台湾文本-数据/微博/微博台湾海峡.xlsx').loc[:, ['txt']]
    for d18 in df18['txt']:
        d18 = str(d18)
        if 'nan' not in d18:
            sum_weibo.append(d18)

    df19 = pd.read_excel('./台湾文本-数据/微博/微博台湾牌.xlsx').loc[:, ['txt']]
    for d19 in df19['txt']:
        d19 = str(d19)
        if 'nan' not in d19:
            sum_weibo.append(d19)

    df20 = pd.read_excel('./台湾文本-数据/微博/微博台湾疫情.xlsx').loc[:, ['txt']]
    for d20 in df20['txt']:
        d20 = str(d20)
        if 'nan' not in d20:
            sum_weibo.append(d20)

    df21 = pd.read_excel('./台湾文本-数据/微博/微博台湾经济.xlsx').loc[:, ['content']]
    for d21 in df21['content']:
        d21 = str(d21)
        if 'nan' not in d21:
            sum_weibo.append(d21)

    df22 = pd.read_excel('./台湾文本-数据/微博/微博台独.xlsx').loc[:, ['txt']]
    for d22 in df22['txt']:
        d22 = str(d22)
        if 'nan' not in d22:
            sum_weibo.append(d22)

    df23 = pd.read_excel('./台湾文本-数据/微博/微博和平统一.xlsx').loc[:, ['content']]
    for d23 in df23['content']:
        d23 = str(d23)
        if 'nan' not in d23:
            sum_weibo.append(d23)

    df24 = pd.read_excel('./台湾文本-数据/微博/微博拜登台湾.xlsx').loc[:, ['content']]
    for d24 in df24['content']:
        d24 = str(d24)
        if 'nan' not in d24:
            sum_weibo.append(d24)

    df25 = pd.read_excel('./台湾文本-数据/微博/微博武统.xlsx').loc[:, ['txt']]
    for d25 in df25['txt']:
        d25 = str(d25)
        if 'nan' not in d25:
            sum_weibo.append(d25)

    df26 = pd.read_excel('./台湾文本-数据/微博/微博特朗普台湾.xlsx').loc[:, ['content']]
    for d26 in df26['content']:
        d26 = str(d26)
        if 'nan' not in d26:
            sum_weibo.append(d26)

    df27 = pd.read_excel('./台湾文本-数据/微博/微博美台.xlsx').loc[:, ['字段2']]
    for d27 in df27['字段2']:
        d27 = str(d27)
        if 'nan' not in d27:
            sum_weibo.append(d27)

    df28 = pd.read_excel('./台湾文本-数据/微博/微博蔡英文.xlsx').loc[:, ['字段1']]
    for d28 in df28['字段1']:
        d28 = str(d28)
        if 'nan' not in d28:
            sum_weibo.append(d28)

    df29 = pd.read_excel('./台湾文本-数据/微博/微博领土主权.xlsx').loc[:, ['content']]
    for d29 in df29['content']:
        d29 = str(d29)
        if 'nan' not in d29:
            sum_weibo.append(d29)

    return sum_weibo

def huanqiuw_sum():
    df = pd.read_excel('./台湾文本-数据/环球网/环球网台海.xlsx').loc[:, ['字段1']]
    sum_list = []
    for d in df['字段1']:
        d = str(d)
        if 'nan' not in d:
            sum_list.append(d)
    return sum_list


def zhongguotaiwanwang():
    df1 = pd.read_excel('./台湾文本-数据/中国台湾网/两岸.xlsx').loc[:, ['字段1','字段2']]
    sum_list = []
    for d1 in range(len(df1['字段1'])):
        d_1 = df1['字段1'][d1]
        d_2 = df1['字段2'][d1]
        x = str(d_1)
        y = str(d_2)
        if 'nan' not in x or 'nan' not in y:
            sum_list.append(x)
            sum_list.append(y)

    df2 = pd.read_excel('./台湾文本-数据/中国台湾网/两岸快评.xlsx').loc[:, ['字段1','字段2']]
    for d1 in range(len(df2['字段1'])):
        d_1 = df2['字段1'][d1]
        d_2 = df2['字段2'][d1]
        x = str(d_1)
        y = str(d_2)
        if 'nan' not in x or 'nan' not in y:
            sum_list.append(x)
            sum_list.append(y)

    df3 = pd.read_excel('./台湾文本-数据/中国台湾网/台商.xlsx').loc[:, ['字段1','字段2']]
    for d1 in range(len(df3['字段1'])):
        d_1 = df3['字段1'][d1]
        d_2 = df3['字段2'][d1]
        x = str(d_1)
        y = str(d_2)
        if 'nan' not in x or 'nan' not in y:
            sum_list.append(x)
            sum_list.append(y)

    df4 = pd.read_excel('./台湾文本-数据/中国台湾网/台湾自2020年12月-2021.1.4时事.xlsx').loc[:, ['字段1','字段2']]
    for d1 in range(len(df4['字段1'])):
        d_1 = df4['字段1'][d1]
        d_2 = df4['字段2'][d1]
        x = str(d_1)
        y = str(d_2)
        if 'nan' not in x or 'nan' not in y:
            sum_list.append(x)
            sum_list.append(y)

    df5 = pd.read_excel('./台湾文本-数据/中国台湾网/文化.xlsx').loc[:, ['字段1','字段2']]
    for d1 in range(len(df5['字段1'])):
        d_1 = df5['字段1'][d1]
        d_2 = df5['字段2'][d1]
        x = str(d_1)
        y = str(d_2)
        if 'nan' not in x or 'nan' not in y:
            sum_list.append(x)
            sum_list.append(y)

    df6 = pd.read_excel('./台湾文本-数据/中国台湾网/海峡时评.xlsx').loc[:, ['字段1','字段2']]
    for d1 in range(len(df6['字段1'])):
        d_1 = df6['字段1'][d1]
        d_2 = df6['字段2'][d1]
        x = str(d_1)
        y = str(d_2)
        if 'nan' not in x or 'nan' not in y:
            sum_list.append(x)
            sum_list.append(y)

    df7 = pd.read_excel('./台湾文本-数据/中国台湾网/经贸.xlsx').loc[:, ['字段1','字段2']]
    for d1 in range(len(df7['字段1'])):
        d_1 = df7['字段1'][d1]
        d_2 = df7['字段2'][d1]
        x = str(d_1)
        y = str(d_2)
        if 'nan' not in x or 'nan' not in y:
            sum_list.append(x)
            sum_list.append(y)

    df8 = pd.read_excel('./台湾文本-数据/中国台湾网/网友专栏.xlsx').loc[:, ['字段1','字段2']]
    for d1 in range(len(df8['字段1'])):
        d_1 = df8['字段1'][d1]
        d_2 = df8['字段2'][d1]
        x = str(d_1)
        y = str(d_2)
        if 'nan' not in x or 'nan' not in y:
            sum_list.append(x)
            sum_list.append(y)

    df9 = pd.read_excel('./台湾文本-数据/中国台湾网/网友快言.xlsx').loc[:, ['字段1','字段2']]
    for d1 in range(len(df9['字段1'])):
        d_1 = df9['字段1'][d1]
        d_2 = df9['字段2'][d1]
        x = str(d_1)
        y = str(d_2)
        if 'nan' not in x or 'nan' not in y:
            sum_list.append(x)
            sum_list.append(y)

    df10 = pd.read_excel('./台湾文本-数据/中国台湾网/萧萧话两岸.xlsx').loc[:, ['字段1','字段2']]
    for d1 in range(len(df10['字段1'])):
        d_1 = df10['字段1'][d1]
        d_2 = df10['字段2'][d1]
        x = str(d_1)
        y = str(d_2)
        if 'nan' not in x or 'nan' not in y:
            sum_list.append(x)
            sum_list.append(y)

    df11 = pd.read_excel('./台湾文本-数据/中国台湾网/部委.xlsx').loc[:, ['字段1','字段2']]
    for d1 in range(len(df11['字段1'])):
        d_1 = df11['字段1'][d1]
        d_2 = df11['字段2'][d1]
        x = str(d_1)
        y = str(d_2)
        if 'nan' not in x or 'nan' not in y:
            sum_list.append(x)
            sum_list.append(y)

    return sum_list

def zhihu():
    df = pd.read_excel('./台湾文本-数据/知乎/知乎台海局势的数据.xlsx').loc[:, ['字段1']]
    sum_list = []
    for d in df['字段1']:
        d = str(d)
        if 'nan' not in d:
            sum_list.append(d)
    return sum_list

def ribao_sum():
    sum_list = []
    df = pd.read_excel('./台湾文本-数据/中国日报网/中国日报网两岸关系.xlsx').loc[:, ['字段1']]
    for d in df['字段1']:
        d = str(d)
        if 'nan' not in d:
            sum_list.append(d)

    df2 = pd.read_excel('./台湾文本-数据/中国日报网/中国日报网台海局势.xlsx').loc[:, ['字段1']]
    for d2 in df2['字段1']:
        d2 = str(d2)
        if 'nan' not in d2:
            sum_list.append(d2)

    df3 = pd.read_excel('./台湾文本-数据/中国日报网/中国日报网台湾牌.xlsx').loc[:, ['字段1']]
    for d3 in df3['字段1']:
        d3 = str(d3)
        if 'nan' not in d3:
            sum_list.append(d3)

    df4 = pd.read_excel('./台湾文本-数据/中国日报网/中国日报网和平统一.xlsx').loc[:, ['字段1']]
    for d4 in df4['字段1']:
        d4 = str(d4)
        if 'nan' not in d4:
            sum_list.append(d4)

    df5 = pd.read_excel('./台湾文本-数据/中国日报网/微博民进党.xlsx').loc[:, ['content']]
    for d5 in df5['content']:
        d5 = str(d5)
        if 'nan' not in d5:
            sum_list.append(d5)

    df6 = pd.read_excel('./台湾文本-数据/中国日报网/日报台军.xlsx').loc[:, ['intro2']]
    for d6 in df6['intro2']:
        d6 = str(d6)
        if 'nan' not in d6:
            sum_list.append(d6)

    df7 = pd.read_excel('./台湾文本-数据/中国日报网/日报台湾海峡.xlsx').loc[:, ['intro2']]
    for d7 in df7['intro2']:
        d7 = str(d7)
        if 'nan' not in d7:
            sum_list.append(d7)

    df8 = pd.read_excel('./台湾文本-数据/中国日报网/日报台湾疫情.xlsx').loc[:, ['intro2']]
    for d8 in df8['intro2']:
        d8 = str(d8)
        if 'nan' not in d8:
            sum_list.append(d8)

    df9 = pd.read_excel('./台湾文本-数据/中国日报网/日报台湾经济.xlsx').loc[:, ['intro2']]
    for d9 in df9['intro2']:
        d9 = str(d9)
        if 'nan' not in d9:
            sum_list.append(d9)

    df10 = pd.read_excel('./台湾文本-数据/中国日报网/日报台独.xlsx').loc[:, ['intro2']]
    for d10 in df10['intro2']:
        d10 = str(d10)
        if 'nan' not in d10:
            sum_list.append(d10)

    df11 = pd.read_excel('./台湾文本-数据/中国日报网/日报拜登台湾.xlsx').loc[:, ['intro2']]
    for d11 in df11['intro2']:
        d11 = str(d11)
        if 'nan' not in d11:
            sum_list.append(d11)

    df12 = pd.read_excel('./台湾文本-数据/中国日报网/日报武统.xlsx').loc[:, ['intro2']]
    for d12 in df12['intro2']:
        d12 = str(d12)
        if 'nan' not in d12:
            sum_list.append(d12)

    df13 = pd.read_excel('./台湾文本-数据/中国日报网/日报民进党.xlsx').loc[:, ['intro2']]
    for d13 in df13['intro2']:
        d13 = str(d13)
        if 'nan' not in d13:
            sum_list.append(d13)

    df14 = pd.read_excel('./台湾文本-数据/中国日报网/日报特朗普台湾.xlsx').loc[:, ['intro2']]
    for d14 in df14['intro2']:
        d14 = str(d14)
        if 'nan' not in d14:
            sum_list.append(d14)

    df15 = pd.read_excel('./台湾文本-数据/中国日报网/日报美台.xlsx').loc[:, ['intro2']]
    for d15 in df15['intro2']:
        d15 = str(d15)
        if 'nan' not in d15:
            sum_list.append(d15)

    df16 = pd.read_excel('./台湾文本-数据/中国日报网/日报蔡英文.xlsx').loc[:, ['intro2']]
    for d16 in df16['intro2']:
        d16 = str(d16)
        if 'nan' not in d16:
            sum_list.append(d16)

    return sum_list

def zhongxing_sum():
    sum_list = []
    df = pd.read_excel('./台湾文本-数据/中新网/中新网两岸关系.xlsx').loc[:, ['news_content']]
    for d in df['news_content']:
        d = str(d)
        if 'nan' not in d:
            sum_list.append(d)

    df2 = pd.read_excel('./台湾文本-数据/中新网/中新网台海局势.xlsx').loc[:, ['news_content']]
    for d2 in df2['news_content']:
        d2 = str(d2)
        if 'nan' not in d2:
            sum_list.append(d2)

    df3 = pd.read_excel('./台湾文本-数据/中新网/中新网台军.xlsx').loc[:, ['news_content']]
    for d3 in df3['news_content']:
        d3 = str(d3)
        if 'nan' not in d3:
            sum_list.append(d3)

    df4 = pd.read_excel('./台湾文本-数据/中新网/中新网台湾政治.xlsx').loc[:, ['news_content']]
    for d4 in df4['news_content']:
        d4 = str(d4)
        if 'nan' not in d4:
            sum_list.append(d4)

    df5 = pd.read_excel('./台湾文本-数据/中新网/中新网台湾海峡.xlsx').loc[:, ['news_content']]
    for d5 in df5['news_content']:
        d5 = str(d5)
        if 'nan' not in d5:
            sum_list.append(d5)

    df6 = pd.read_excel('./台湾文本-数据/中新网/中新网台湾牌.xlsx').loc[:, ['news_content']]
    for d6 in df6['news_content']:
        d6 = str(d6)
        if 'nan' not in d6:
            sum_list.append(d6)

    df7 = pd.read_excel('./台湾文本-数据/中新网/中新网台湾疫情.xlsx').loc[:, ['news_content']]
    for d7 in df7['news_content']:
        d7 = str(d7)
        if 'nan' not in d7:
            sum_list.append(d7)

    df8 = pd.read_excel('./台湾文本-数据/中新网/中新网台湾经济.xlsx').loc[:, ['news_content']]
    for d8 in df8['news_content']:
        d8 = str(d8)
        if 'nan' not in d8:
            sum_list.append(d8)

    df9 = pd.read_excel('./台湾文本-数据/中新网/中新网台独.xlsx').loc[:, ['news_content']]
    for d9 in df9['news_content']:
        d9 = str(d9)
        if 'nan' not in d9:
            sum_list.append(d9)

    df10 = pd.read_excel('./台湾文本-数据/中新网/中新网和平统一.xlsx').loc[:, ['news_content']]
    for d10 in df10['news_content']:
        d10 = str(d10)
        if 'nan' not in d10:
            sum_list.append(d10)

    df11 = pd.read_excel('./台湾文本-数据/中新网/中新网武统.xlsx').loc[:, ['news_content']]
    for d11 in df11['news_content']:
        d11 = str(d11)
        if 'nan' not in d11:
            sum_list.append(d11)

    df12 = pd.read_excel('./台湾文本-数据/中新网/中新网民进党.xlsx').loc[:, ['news_content']]
    for d12 in df12['news_content']:
        d12 = str(d12)
        if 'nan' not in d12:
            sum_list.append(d12)

    df13 = pd.read_excel('./台湾文本-数据/中新网/中新网美台.xlsx').loc[:, ['news_content']]
    for d13 in df13['news_content']:
        d13 = str(d13)
        if 'nan' not in d13:
            sum_list.append(d13)

    df14 = pd.read_excel('./台湾文本-数据/中新网/中新网蔡英文.xlsx').loc[:, ['news_content']]
    for d14 in df14['news_content']:
        d14 = str(d14)
        if 'nan' not in d14:
            sum_list.append(d14)

    return sum_list

def jinri_sum():
    sum_list = []
    df = pd.read_excel('./台湾文本-数据/今日头条/今日头条两岸关系.xlsx').loc[:, ['标题']]
    for d in df['标题']:
        d = str(d)
        if 'nan' not in d:
            sum_list.append(d)

    df2 = pd.read_excel('./台湾文本-数据/今日头条/今日头条台军.xlsx').loc[:, ['标题']]
    for d2 in df2['标题']:
        d2 = str(d2)
        if 'nan' not in d2:
            sum_list.append(d2)

    df3 = pd.read_excel('./台湾文本-数据/今日头条/今日头条台海局势.xlsx').loc[:, ['标题']]
    for d3 in df3['标题']:
        d3 = str(d3)
        if 'nan' not in d3:
            sum_list.append(d3)

    df4 = pd.read_excel('./台湾文本-数据/今日头条/今日头条台湾政治.xlsx').loc[:, ['标题']]
    for d4 in df4['标题']:
        d4 = str(d4)
        if 'nan' not in d4:
            sum_list.append(d4)

    df5 = pd.read_excel('./台湾文本-数据/今日头条/今日头条台湾海峡.xlsx').loc[:, ['标题']]
    for d5 in df5['标题']:
        d5 = str(d5)
        if 'nan' not in d5:
            sum_list.append(d5)

    df6 = pd.read_excel('./台湾文本-数据/今日头条/今日头条台湾牌.xlsx').loc[:, ['标题']]
    for d6 in df6['标题']:
        d6 = str(d6)
        if 'nan' not in d6:
            sum_list.append(d6)

    df7 = pd.read_excel('./台湾文本-数据/今日头条/今日头条台湾疫情.xlsx').loc[:, ['标题']]
    for d7 in df7['标题']:
        d7 = str(d7)
        if 'nan' not in d7:
            sum_list.append(d7)

    df8 = pd.read_excel('./台湾文本-数据/今日头条/今日头条台独.xlsx').loc[:, ['标题']]
    for d8 in df8['标题']:
        d8 = str(d8)
        if 'nan' not in d8:
            sum_list.append(d8)

    df9 = pd.read_excel('./台湾文本-数据/今日头条/今日头条和平统一.xlsx').loc[:, ['标题']]
    for d9 in df9['标题']:
        d9 = str(d9)
        if 'nan' not in d9:
            sum_list.append(d9)

    df10 = pd.read_excel('./台湾文本-数据/今日头条/今日头条拜登台湾.xlsx').loc[:, ['标题']]
    for d10 in df10['标题']:
        d10 = str(d10)
        if 'nan' not in d10:
            sum_list.append(d10)

    df11 = pd.read_excel('./台湾文本-数据/今日头条/今日头条武统.xlsx').loc[:, ['标题']]
    for d11 in df11['标题']:
        d11 = str(d11)
        if 'nan' not in d11:
            sum_list.append(d11)

    df12 = pd.read_excel('./台湾文本-数据/今日头条/今日头条民进党.xlsx').loc[:, ['标题']]
    for d12 in df12['标题']:
        d12 = str(d12)
        if 'nan' not in d12:
            sum_list.append(d12)

    df13= pd.read_excel('./台湾文本-数据/今日头条/今日头条特朗普台湾.xlsx').loc[:, ['标题']]
    for d13 in df13['标题']:
        d13 = str(d13)
        if 'nan' not in d13:
            sum_list.append(d13)

    df14 = pd.read_excel('./台湾文本-数据/今日头条/今日头条美台.xlsx').loc[:, ['标题']]
    for d14 in df14['标题']:
        d14 = str(d14)
        if 'nan' not in d14:
            sum_list.append(d14)

    df15 = pd.read_excel('./台湾文本-数据/今日头条/今日头条蔡英文.xlsx').loc[:, ['标题']]
    for d15 in df15['标题']:
        d15 = str(d15)
        if 'nan' not in d15:
            sum_list.append(d15)

    df16 = pd.read_excel('./台湾文本-数据/今日头条/台湾经济.xlsx').loc[:, ['标题']]
    for d16 in df16['标题']:
        d16 = str(d16)
        if 'nan' not in d16:
            sum_list.append(d16)

    return sum_list

def guangming_sum():
    sum_list = []
    df = pd.read_excel('./台湾文本-数据/光明网/光明网两岸关系.xlsx').loc[:, ['标题']]
    for d in df['标题']:
        d = str(d)
        if 'nan' not in d:
            sum_list.append(d)

    df2 = pd.read_excel('./台湾文本-数据/光明网/光明网台军.xlsx').loc[:, ['标题']]
    for d2 in df2['标题']:
        d2 = str(d2)
        if 'nan' not in d2:
            sum_list.append(d2)

    df3 = pd.read_excel('./台湾文本-数据/光明网/光明网台海局势.xlsx').loc[:, ['标题']]
    for d3 in df3['标题']:
        d3 = str(d3)
        if 'nan' not in d3:
            sum_list.append(d3)

    df4 = pd.read_excel('./台湾文本-数据/光明网/光明网台湾政治.xlsx').loc[:, ['标题']]
    for d4 in df4['标题']:
        d4 = str(d4)
        if 'nan' not in d4:
            sum_list.append(d4)

    df5 = pd.read_excel('./台湾文本-数据/光明网/光明网台湾海峡.xlsx').loc[:, ['标题']]
    for d5 in df5['标题']:
        d5 = str(d5)
        if 'nan' not in d5:
            sum_list.append(d5)

    df6 = pd.read_excel('./台湾文本-数据/光明网/光明网台湾牌.xlsx').loc[:, ['标题']]
    for d6 in df6['标题']:
        d6 = str(d6)
        if 'nan' not in d6:
            sum_list.append(d6)

    df7 = pd.read_excel('./台湾文本-数据/光明网/光明网台湾疫情.xlsx').loc[:, ['标题']]
    for d7 in df7['标题']:
        d7 = str(d7)
        if 'nan' not in d7:
            sum_list.append(d7)

    df8 = pd.read_excel('./台湾文本-数据/光明网/光明网台湾经济.xlsx').loc[:, ['标题']]
    for d8 in df8['标题']:
        d8 = str(d8)
        if 'nan' not in d8:
            sum_list.append(d8)

    df9 = pd.read_excel('./台湾文本-数据/光明网/光明网台独.xlsx').loc[:, ['标题']]
    for d9 in df9['标题']:
        d9 = str(d9)
        if 'nan' not in d9:
            sum_list.append(d9)

    df10 = pd.read_excel('./台湾文本-数据/光明网/光明网和平统一.xlsx').loc[:, ['标题']]
    for d10 in df10['标题']:
        d10 = str(d10)
        if 'nan' not in d10:
            sum_list.append(d10)

    df11 = pd.read_excel('./台湾文本-数据/光明网/光明网武统.xlsx').loc[:, ['标题']]
    for d11 in df11['标题']:
        d11 = str(d11)
        if 'nan' not in d11:
            sum_list.append(d11)

    df12 = pd.read_excel('./台湾文本-数据/光明网/光明网民进党.xlsx').loc[:, ['标题']]
    for d12 in df12['标题']:
        d12 = str(d12)
        if 'nan' not in d12:
            sum_list.append(d12)

    df13 = pd.read_excel('./台湾文本-数据/光明网/光明网蔡英文.xlsx').loc[:, ['标题']]
    for d13 in df13['标题']:
        d13 = str(d13)
        if 'nan' not in d13:
            sum_list.append(d13)

    return sum_list

def fenghuan_sum():
    sum_list = []
    df = pd.read_excel('./台湾文本-数据/凤凰网/凤凰台军.xlsx').loc[:, ['标题']]
    for d in df['标题']:
        d = str(d)
        if 'nan' not in d:
            sum_list.append(d)

    df2 = pd.read_excel('./台湾文本-数据/凤凰网/凤凰台湾政治.xlsx').loc[:, ['标题']]
    for d2 in df2['标题']:
        d2 = str(d2)
        if 'nan' not in d2:
            sum_list.append(d2)

    df3 = pd.read_excel('./台湾文本-数据/凤凰网/凤凰台湾海峡.xlsx').loc[:, ['标题']]
    for d3 in df3['标题']:
        d3 = str(d3)
        if 'nan' not in d3:
            sum_list.append(d3)

    df4 = pd.read_excel('./台湾文本-数据/凤凰网/凤凰台湾疫情.xlsx').loc[:, ['标题']]
    for d4 in df4['标题']:
        d4 = str(d4)
        if 'nan' not in d4:
            sum_list.append(d4)

    df5 = pd.read_excel('./台湾文本-数据/凤凰网/凤凰台湾经济.xlsx').loc[:, ['标题']]
    for d5 in df5['标题']:
        d5 = str(d5)
        if 'nan' not in d5:
            sum_list.append(d5)

    df6 = pd.read_excel('./台湾文本-数据/凤凰网/凤凰台独.xlsx').loc[:, ['标题']]
    for d6 in df6['标题']:
        d6 = str(d6)
        if 'nan' not in d6:
            sum_list.append(d6)

    df7 = pd.read_excel('./台湾文本-数据/凤凰网/凤凰拜登台湾.xlsx').loc[:, ['标题']]
    for d7 in df7['标题']:
        d7 = str(d7)
        if 'nan' not in d7:
            sum_list.append(d7)

    df8 = pd.read_excel('./台湾文本-数据/凤凰网/凤凰武统.xlsx').loc[:, ['标题']]
    for d8 in df8['标题']:
        d8 = str(d8)
        if 'nan' not in d8:
            sum_list.append(d8)

    df9 = pd.read_excel('./台湾文本-数据/凤凰网/凤凰民进党.xlsx').loc[:, ['标题']]
    for d9 in df9['标题']:
        d9 = str(d9)
        if 'nan' not in d9:
            sum_list.append(d9)

    df10 = pd.read_excel('./台湾文本-数据/凤凰网/凤凰特朗普台湾.xlsx').loc[:, ['标题']]
    for d10 in df10['标题']:
        d10 = str(d10)
        if 'nan' not in d10:
            sum_list.append(d10)

    df11 = pd.read_excel('./台湾文本-数据/凤凰网/凤凰网两岸关系.xlsx').loc[:, ['标题']]
    for d11 in df11['标题']:
        d11 = str(d11)
        if 'nan' not in d11:
            sum_list.append(d11)

    df12 = pd.read_excel('./台湾文本-数据/凤凰网/凤凰网台海局势.xlsx').loc[:, ['标题1']]
    for d12 in df12['标题1']:
        d12 = str(d12)
        if 'nan' not in d12:
            sum_list.append(d12)

    df13 = pd.read_excel('./台湾文本-数据/凤凰网/凤凰网台湾牌.xlsx').loc[:, ['标题']]
    for d13 in df13['标题']:
        d13 = str(d13)
        if 'nan' not in d13:
            sum_list.append(d13)

    df14 = pd.read_excel('./台湾文本-数据/凤凰网/凤凰网和平统一.xlsx').loc[:, ['标题']]
    for d14 in df14['标题']:
        d14 = str(d14)
        if 'nan' not in d14:
            sum_list.append(d14)

    df15 = pd.read_excel('./台湾文本-数据/凤凰网/凤凰美台.xlsx').loc[:, ['标题']]
    for d15 in df15['标题']:
        d15 = str(d15)
        if 'nan' not in d15:
            sum_list.append(d15)

    df16 = pd.read_excel('./台湾文本-数据/凤凰网/凤凰蔡英文.xlsx').loc[:, ['标题']]
    for d16 in df16['标题']:
        d16 = str(d16)
        if 'nan' not in d16:
            sum_list.append(d16)

    df17 = pd.read_excel('./台湾文本-数据/凤凰网/凤凰领土主权.xlsx').loc[:, ['标题']]
    for d17 in df17['标题']:
        d17 = str(d17)
        if 'nan' not in d17:
            sum_list.append(d17)

    return sum_list

def xinhua_sum():
    sum_list = []
    df = pd.read_excel('./台湾文本-数据/新华网/新华网两岸关系.xlsx').loc[:, ['newstext']]
    for d in df['newstext']:
        d = str(d)
        if 'nan' not in d:
            sum_list.append(d)

    df2 = pd.read_excel('./台湾文本-数据/新华网/新华网台军.xlsx').loc[:, ['newstext']]
    for d2 in df2['newstext']:
        d2 = str(d2)
        if 'nan' not in d2:
            sum_list.append(d2)

    df3 = pd.read_excel('./台湾文本-数据/新华网/新华网台海局势.xlsx').loc[:, ['newstext']]
    for d3 in df3['newstext']:
        d3 = str(d3)
        if 'nan' not in d3:
            sum_list.append(d3)

    df4 = pd.read_excel('./台湾文本-数据/新华网/新华网台湾政治.xlsx').loc[:, ['newstext']]
    for d4 in df4['newstext']:
        d4 = str(d4)
        if 'nan' not in d4:
            sum_list.append(d4)

    df5 = pd.read_excel('./台湾文本-数据/新华网/新华网台湾海峡.xlsx').loc[:, ['newstext']]
    for d5 in df5['newstext']:
        d5 = str(d5)
        if 'nan' not in d5:
            sum_list.append(d5)

    df6 = pd.read_excel('./台湾文本-数据/新华网/新华网台湾牌.xlsx').loc[:, ['newstext']]
    for d6 in df6['newstext']:
        d6 = str(d6)
        if 'nan' not in d6:
            sum_list.append(d6)

    df7 = pd.read_excel('./台湾文本-数据/新华网/新华网台湾疫情.xlsx').loc[:, ['newstext']]
    for d7 in df7['newstext']:
        d7 = str(d7)
        if 'nan' not in d7:
            sum_list.append(d7)

    df8 = pd.read_excel('./台湾文本-数据/新华网/新华网台湾经济.xlsx').loc[:, ['newstext']]
    for d8 in df8['newstext']:
        d8 = str(d8)
        if 'nan' not in d8:
            sum_list.append(d8)

    df9 = pd.read_excel('./台湾文本-数据/新华网/新华网台独.xlsx').loc[:, ['newstext']]
    for d9 in df9['newstext']:
        d9 = str(d9)
        if 'nan' not in d9:
            sum_list.append(d9)

    df10 = pd.read_excel('./台湾文本-数据/新华网/新华网和平统一.xlsx').loc[:, ['newstext']]
    for d10 in df10['newstext']:
        d10 = str(d10)
        if 'nan' not in d10:
            sum_list.append(d10)

    df11 = pd.read_excel('./台湾文本-数据/新华网/新华网武统.xlsx').loc[:, ['newstext']]
    for d11 in df11['newstext']:
        d11 = str(d11)
        if 'nan' not in d11:
            sum_list.append(d11)

    df12 = pd.read_excel('./台湾文本-数据/新华网/新华网民进党.xlsx').loc[:, ['newstext']]
    for d12 in df12['newstext']:
        d12 = str(d12)
        if 'nan' not in d12:
            sum_list.append(d12)

    df13 = pd.read_excel('./台湾文本-数据/新华网/新华网美台.xlsx').loc[:, ['newstext']]
    for d13 in df13['newstext']:
        d13 = str(d13)
        if 'nan' not in d13:
            sum_list.append(d13)

    df14 = pd.read_excel('./台湾文本-数据/新华网/新华网蔡英文.xlsx').loc[:, ['newstext']]
    for d14 in df14['newstext']:
        d14 = str(d14)
        if 'nan' not in d14:
            sum_list.append(d14)

    return sum_list

def emotion_bar():
    # 读入停用词表
    stop_words = []
    with open("./台湾文本-数据/stopwords_cn.txt", 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            stop_words.append(line.strip())
    my_stop_words = ['\\u3000', '(', '，', '、', '“', '”','jpg','src','12','v2','img','zhimg','https','com','IT','22','24','14','15','00','26','2019','18','19','28','17','16','10','2020','11','20','71','90','20','data','12','is','30','-----','------']
    stop_words.extend(my_stop_words)
    word1 = []
    for i in range(0,3000):
        i = str(i)
        word1.append(i)
    stop_words.extend(word1)
    list1 = weibo_sum()
    list2 = zhihu()
    list3 = huanqiuw_sum()
    list4 = zhongguotaiwanwang()
    list5 = ribao_sum()
    list6 = zhongxing_sum()
    list7 = jinri_sum()
    list8 = guangming_sum()
    list9 = fenghuan_sum()
    list10 =xinhua_sum()

    sum_list = []
    sentimentslist = []
    for l1 in list1:
        l1 = str(l1)
        sum_list.append(l1)
    for l2 in list2:
        l2 = str(l2)
        sum_list.append(l2)
    for l3 in list3:
        l3 = str(l3)
        sum_list.append(l3)
    for l4 in list4:
        l4 = str(l4)
        sum_list.append(l4)
    for l5 in list5:
        l5 = str(l5)
        sum_list.append(l5)
    for l6 in list6:
        l6 = str(l6)
        sum_list.append(l6)
    for l7 in list7:
        l7 = str(l7)
        sum_list.append(l7)
    for l8 in list8:
        l8 = str(l8)
        sum_list.append(l8)
    for l9 in list9:
        l9 = str(l9)
        sum_list.append(l9)
    for l10 in list10:
        l10 = str(l10)
        sum_list.append(l10)

    for s in sum_list:
        f = SnowNLP(s)
        print(str(f.sentiments)[0:3])
        sentimentslist.append(str(f.sentiments)[0:3])

    # return sentimentslist

    # data(sentimentslist)


def data():
    # d = {}
    # for l in sentimentslist:
    #     d[l] = d.get(l, 0) + 1
    # ls = list(d.items())
    # ls.sort(key=lambda x: x[0], reverse=False)
    # x_data = []
    # y_data = []
    # for i in ls:
    #     x_data.append(i[0])
    #     y_data.append(i[1])

    x_data = ['0.0','0.1','0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9','1.0']
    y_data = ['1533','573','502','491','520','556','577','788','1252','20564','6393']
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))
        .add_xaxis(x_data)
        .add_yaxis("", y_data, label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts={"text": "台海舆论情感分析", "subtext": "数值越接近1，情感越高"}
        )
        .render("./templates/台海情感分析柱状图.html")
    )


if __name__ == '__main__':
    data()


