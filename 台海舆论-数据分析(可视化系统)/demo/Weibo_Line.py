import pandas as pd
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.charts import Bar


def weibo_sum():

    x_list = []
    y_list = []

    df1 = pd.read_excel('./台湾文本-数据/微博/微博台海局势1-12月/1.xlsx').loc[:,['card-act','card-act1']]
    for d1 in range(len(df1['card-act'])):
        x = df1['card-act'][d1]
        x = x[3:]
        y = df1['card-act1'][d1]
        y = y[3:]
        if x != '' and y != '':
            x_list.append(x)
            y_list.append(y)

    # df2 = pd.read_excel('./台湾文本-数据/微博/微博台海局势1-12月/2.xlsx').loc[:,['card-act','card-act1']]
    # for d2 in range(len(df2['card-act'])):
    #     x2 = df2['card-act'][d2]
    #     x2 = x2[2:]
    #     y2 = df2['card-act1'][d2]
    #     y2 = y2[2:]
    #     print(x2,y2)
    #     # try:
    #     #     if x2 != '' and y2 != '':
    #     #         x_list.append(x2)
    #     #         y_list.append(y2)
    #     # except ValueError:
    #     #     pass

    df3 = pd.read_excel('./台湾文本-数据/微博/微博台海局势1-12月/3.xlsx').loc[:, ['card-act', 'card-act1']]
    for d3 in range(len(df3['card-act'])):
        x3 = df3['card-act'][d3]
        x3 = x3[3:]
        y3 = df3['card-act1'][d3]
        y3 = y3[3:]
        if x3 != '' and y3 != '':
            x_list.append(x3)
            y_list.append(y3)

    df4 = pd.read_excel('./台湾文本-数据/微博/微博台海局势1-12月/4.xlsx').loc[:, ['card-act', 'card-act1']]
    for d4 in range(len(df4['card-act'])):
        x4 = df4['card-act'][d4]
        x4 = x4[3:]
        y4 = df4['card-act1'][d4]
        y4 = y4[3:]
        if x4 != '' and y4 != '':
            x_list.append(x4)
            y_list.append(y4)

    # df5 = pd.read_excel('./台湾文本-数据/微博/微博台海局势1-12月/5.xlsx').loc[:, ['card-act', 'card-act1']]
    # for d5 in range(len(df5['card-act'])):
    #     x5 = df5['card-act'][d5]
    #     x5 = x5[3:]
    #     y5 = df5['card-act1'][d5]
    #     y5 = y5[3:]
    #     if x5 != '' and y5 != '':
    #         x_list.append(x5)
    #         y_list.append(y5)

    df6 = pd.read_excel('./台湾文本-数据/微博/微博台海局势1-12月/6.xlsx').loc[:, ['card-act', 'card-act1']]
    for d6 in range(len(df6['card-act'])):
        x6 = df6['card-act'][d6]
        x6 = x6[3:]
        y6 = df6['card-act1'][d6]
        y6 = y6[3:]
        if x6 != '' and y6 != '':
            x_list.append(x6)
            y_list.append(y6)

    df7 = pd.read_excel('./台湾文本-数据/微博/微博台海局势1-12月/7.xlsx').loc[:, ['card-act', 'card-act1']]
    for d7 in range(len(df7['card-act'])):
        x7 = df7['card-act'][d7]
        x7 = x7[3:]
        y7 = df7['card-act1'][d7]
        y7 = y7[3:]
        if x7 != '' and y7 != '':
            x_list.append(x7)
            y_list.append(y7)

    df8 = pd.read_excel('./台湾文本-数据/微博/微博台海局势1-12月/8.xlsx').loc[:, ['card-act', 'card-act1']]
    for d8 in range(len(df8['card-act'])):
        x8 = df8['card-act'][d8]
        x8 = x8[3:]
        y8 = df8['card-act1'][d8]
        y8 = y8[3:]
        if x8 != '' and y8 != '':
            x_list.append(x8)
            y_list.append(y8)

    df9 = pd.read_excel('./台湾文本-数据/微博/微博台海局势1-12月/9.xlsx').loc[:, ['card-act', 'card-act1']]
    for d9 in range(len(df9['card-act'])):
        x9 = df9['card-act'][d9]
        x9 = x9[3:]
        y9 = df9['card-act1'][d9]
        y9 = y9[3:]
        if x9 != '' and y9 != '':
            x_list.append(x9)
            y_list.append(y9)

    df10 = pd.read_excel('./台湾文本-数据/微博/微博台海局势1-12月/10.xlsx').loc[:, ['card-act', 'card-act1']]
    for d10 in range(len(df10['card-act'])):
        x10 = df10['card-act'][d10]
        x10 = x10[3:]
        y10 = df10['card-act1'][d10]
        y10 = y10[3:]
        if x10 != '' and y10 != '':
            x_list.append(x10)
            y_list.append(y10)

    df11 = pd.read_excel('./台湾文本-数据/微博/微博台海局势1-12月/11.xlsx').loc[:, ['card-act', 'card-act1']]
    for d11 in range(len(df11['card-act'])):
        x11 = df11['card-act'][d11]
        x11 = x11[3:]
        y11 = df11['card-act1'][d11]
        y11 = y11[3:]
        if x11 != '' and y11 != '':
            x_list.append(x11)
            y_list.append(y11)

    df12 = pd.read_excel('./台湾文本-数据/微博/微博台海局势1-12月/12.xlsx').loc[:, ['card-act', 'card-act1']]
    for d12 in range(len(df12['card-act'])):
        x12 = df12['card-act'][d12]
        x12 = x12[3:]
        y12 = df12['card-act1'][d12]
        y12 = y12[3:]
        if x12 != '' and y12 != '':
            x_list.append(x12)
            y_list.append(y12)

    df13 = pd.read_excel('./台湾文本-数据/微博/两岸关系微博.xlsx').loc[:,['card-act', 'card-act1']]
    for d13 in range(len(df13['card-act'])):
        x13 = df13['card-act'][d13]
        x13 = x13[3:]
        y13 = df13['card-act1'][d13]
        y13 = y13[3:]
        if x13 != '' and y13 != '':
            x_list.append(x13)
            y_list.append(y13)

    df14 = pd.read_excel('./台湾文本-数据/微博/微博中国内政.xlsx').loc[:, ['card-act', 'card-act1']]
    for d14 in range(len(df14['card-act'])):
        x14 = df14['card-act'][d14]
        x14 = x14[3:]
        y14 = df14['card-act1'][d14]
        y14 = y14[3:]
        if x14 != '' and y14 != '':
            x_list.append(x14)
            y_list.append(y14)

    df15 = pd.read_excel('./台湾文本-数据/微博/微博分裂势力.xlsx').loc[:, ['card-act', 'card-act1']]
    for d15 in range(len(df15['card-act'])):
        x15 = df15['card-act'][d15]
        x15 = x15[3:]
        y15 = df15['card-act1'][d15]
        y15 = y15[3:]
        if x15 != '' and y15 != '':
            x_list.append(x15)
            y_list.append(y15)

    df16 = pd.read_excel('./台湾文本-数据/微博/微博台军.xlsx').loc[:, ['card-act', 'card-act1']]
    for d16 in range(len(df16['card-act'])):
        x16 = df16['card-act'][d16]
        x16 = x16[3:]
        y16 = df16['card-act1'][d16]
        y16 = y16[3:]
        if x16 != '' and y16 != '':
            x_list.append(x16)
            y_list.append(y16)

    df17 = pd.read_excel('./台湾文本-数据/微博/微博台湾政治.xlsx').loc[:, ['card-act', 'card-act1']]
    for d17 in range(len(df17['card-act'])):
        x17 = df17['card-act'][d17]
        x17 = x17[3:]
        y17 = df17['card-act1'][d17]
        y17 = y17[3:]
        if x17 != '' and y17 != '':
            x_list.append(x17)
            y_list.append(y17)

    df18 = pd.read_excel('./台湾文本-数据/微博/微博台湾海峡.xlsx').loc[:, ['card-act', 'card-act1']]
    for d18 in range(len(df18['card-act'])):
        x18 = df18['card-act'][d18]
        x18 = x18[3:]
        y18 = df18['card-act1'][d18]
        y18 = y18[3:]
        if x18 != '' and y18 != '':
            x_list.append(x18)
            y_list.append(y18)

    df19 = pd.read_excel('./台湾文本-数据/微博/微博台湾牌.xlsx').loc[:, ['card-act', 'card-act1']]
    for d19 in range(len(df19['card-act'])):
        x19 = df19['card-act'][d19]
        x19 = x19[3:]
        y19 = df19['card-act1'][d19]
        y19 = y19[3:]
        if x19 != '' and y19 != '':
            x_list.append(x19)
            y_list.append(y19)

    df20 = pd.read_excel('./台湾文本-数据/微博/微博台湾疫情.xlsx').loc[:, ['card-act', 'card-act1']]
    for d20 in range(len(df20['card-act'])):
        x20 = df20['card-act'][d20]
        x20 = x20[3:]
        y20 = df20['card-act1'][d20]
        y20 = y20[3:]
        if x20 != '' and y20 != '':
            x_list.append(x20)
            y_list.append(y20)

    df21 = pd.read_excel('./台湾文本-数据/微博/微博台湾经济.xlsx').loc[:, ['card-act', 'card-act1']]
    for d21 in range(len(df21['card-act'])):
        x21 = df21['card-act'][d21]
        x21 = x21[3:]
        y21 = df21['card-act1'][d21]
        y21 = y21[3:]
        if x21 != '' and y21 != '':
            x_list.append(x21)
            y_list.append(y21)

    df22 = pd.read_excel('./台湾文本-数据/微博/微博台独.xlsx').loc[:, ['card-act', 'card-act1']]
    for d22 in range(len(df22['card-act'])):
        x22 = df22['card-act'][d22]
        x22 = x22[3:]
        y22 = df22['card-act1'][d22]
        y22 = y22[3:]
        if x22 != '' and y22 != '':
            x_list.append(x22)
            y_list.append(y22)

    df23 = pd.read_excel('./台湾文本-数据/微博/微博和平统一.xlsx').loc[:, ['card-act', 'card-act1']]
    for d23 in range(len(df23['card-act'])):
        x23 = df23['card-act'][d23]
        x23 = x23[3:]
        y23 = df23['card-act1'][d23]
        y23 = y23[3:]
        if x23 != '' and y23 != '':
            x_list.append(x23)
            y_list.append(y23)

    df24 = pd.read_excel('./台湾文本-数据/微博/微博拜登台湾.xlsx').loc[:, ['card-act', 'card-act1']]
    for d24 in range(len(df24['card-act'])):
        x24 = df24['card-act'][d24]
        x24 = x24[3:]
        y24 = df24['card-act1'][d24]
        y24 = y24[3:]
        if x24 != '' and y24 != '':
            x_list.append(x24)
            y_list.append(y24)

    df25 = pd.read_excel('./台湾文本-数据/微博/微博武统.xlsx').loc[:, ['card-act', 'card-act1']]
    for d25 in range(len(df25['card-act'])):
        x25 = df25['card-act'][d25]
        x25 = x25[3:]
        y25 = df25['card-act1'][d25]
        y25 = y25[3:]
        if x25 != '' and y25 != '':
            x_list.append(x25)
            y_list.append(y25)

    df26 = pd.read_excel('./台湾文本-数据/微博/微博特朗普台湾.xlsx').loc[:, ['card-act', 'card-act1']]
    for d26 in range(len(df26['card-act'])):
        x26 = df26['card-act'][d26]
        x26 = x26[3:]
        y26 = df26['card-act1'][d26]
        y26 = y26[3:]
        if x26 != '' and y26 != '':
            x_list.append(x26)
            y_list.append(y26)

    # df27 = pd.read_excel('./台湾文本-数据/微博/微博美台.xlsx').loc[:, ['card-act', 'card-act1']]
    # for d27 in range(len(df27['card-act'])):
    #     x27 = df27['card-act'][d27]
    #     x27 = x27[3:]
    #     y27 = df27['card-act1'][d27]
    #     y27 = y27[3:]
    #     if x27 != '' and y27 != '':
    #         x_list.append(x27)
    #         y_list.append(y27)

    df28 = pd.read_excel('./台湾文本-数据/微博/微博蔡英文.xlsx').loc[:, ['card-act', 'card-act1']]
    for d28 in range(len(df28['card-act'])):
        x28 = df28['card-act'][d28]
        x28 = x28[3:]
        y28 = df28['card-act1'][d28]
        y28 = y28[3:]
        if x28 != '' and y28 != '':
            x_list.append(x28)
            y_list.append(y28)

    df29 = pd.read_excel('./台湾文本-数据/微博/微博领土主权.xlsx').loc[:, ['card-act', 'card-act1']]
    for d29 in range(len(df29['card-act'])):
        x29 = df29['card-act'][d29]
        x29 = x29[3:]
        y29 = df29['card-act1'][d29]
        y29 = y29[3:]
        if x29 != '' and y29 != '':
            x_list.append(x29)
            y_list.append(y29)

    return x_list,y_list


def weibo_line():
    y_data = []
    x_data =['0-50','50-100','100-150','150-200','200-250','250-300','300-350','350-400','400-450','450及以上']
    x_list,y_list = weibo_sum()
    y_50 = []
    y_100 = []
    y_150 = []
    y_200 = []
    y_250 = []
    y_300 = []
    y_350 = []
    y_400 = []
    y_450 = []
    y_500 = []
    for i in range(len(x_list)):
        x = x_list[i]
        y = y_list[i]
        if int(x) <= 50:
            y_50.append(y)
        if 50 < int(x) <= 100:
            y_100.append(y)
        if 50 < int(x) <= 100:
            y_100.append(y)

        if 100 < int(x) <= 150:
            y_150.append(y)
        if 150 < int(x) <= 200:
            y_200.append(y)
        if 200 < int(x) <= 250:
            y_250.append(y)
        if 250 < int(x) <= 300:
            y_300.append(y)
        if 300 < int(x) <= 350:
            y_350.append(y)
        if 350 < int(x) <= 400:
            y_400.append(y)
        if 400 < int(x) <= 450:
            y_450.append(y)
        if int(x) > 450:
            y_500.append(y)

    sum1 = 0
    for i in y_50:
        i = int(i)
        sum1 += i
    avg1 = sum1/len(y_50)
    y_data.append(int(avg1))

    sum2 = 0
    for i in y_100:
        i = int(i)
        sum2 += i
    avg2 = sum2 / len(y_100)
    y_data.append(int(avg2))

    sum3 = 0
    for i in y_150:
        i = int(i)
        sum3 += i
    avg3 = sum3 / len(y_150)
    y_data.append(int(avg3))

    sum4 = 0
    for i in y_200:
        i = int(i)
        sum4 += i
    avg4 = sum4 / len(y_200)
    y_data.append(int(avg4))

    sum5 = 0
    for i in y_250:
        i = int(i)
        sum5 += i
    avg5 = sum5 / len(y_250)
    y_data.append(int(avg5))

    sum6 = 0
    for i in y_300:
        i = int(i)
        sum6 += i
    avg6 = sum6 / len(y_300)
    y_data.append(int(avg6))

    sum7 = 0
    for i in y_350:
        i = int(i)
        sum7 += i
    avg7 = sum7 / len(y_350)
    y_data.append(int(avg7))

    sum8 = 0
    for i in y_400:
        i = int(i)
        sum8 += i
    avg8 = sum8 / len(y_400)
    y_data.append(int(avg8))

    sum9 = 0
    for i in y_450:
        i = int(i)
        sum9 += i
    avg9 = sum9 / len(y_450)
    y_data.append(int(avg9))

    sum10 = 0
    for i in y_500:
        i = int(i)
        sum10 += i
    avg10 = sum10 / len(y_500)
    y_data.append(int(avg10))

    return x_data,y_data

#     c = (
#         Bar(init_opts=opts.InitOpts(width="1300px", height="600px", theme=ThemeType.MACARONS))
#         .add_xaxis(x_data)
#         .add_yaxis("平均值", y_data, label_opts=opts.LabelOpts(is_show=False))
#         .reversal_axis()
#         .set_global_opts(
#             title_opts={"text": "评论与转发关系图"},
#             xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter='{value}(评论数量)')),
#             yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter="{value}(转发数量)")),
#         )
#         .render("./templates/今日条形图.html")
#     )
#
# if __name__ == '__main__':
#     weibo_line()