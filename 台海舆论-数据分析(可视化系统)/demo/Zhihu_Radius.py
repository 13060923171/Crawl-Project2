import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Polar
from pyecharts.globals import ThemeType


def zhihu():
    df = pd.read_excel('./台湾文本-数据/知乎/知乎台海局势的数据.xlsx').loc[:, ['ContentItem-action','ContentItem-actions']]
    list_01 = []
    list_02 = []
    list_03 = []
    list_04 = []
    list_05 = []
    list_06 = []
    list_07 = []
    list_08 = []
    list_09 = []
    list_10 = []
    list_11 = []
    list_12 = []

    for d in range(len(df['ContentItem-action'])):
        d1 = df['ContentItem-action'][d]
        d1 = str(d1)
        d1 = d1[0:7]
        d2 = df['ContentItem-actions'][d]
        d2 = str(d2)
        d2 = d2.replace('​赞同 ','').replace('​赞同','')
        d2 = d2.replace('1.4 万','14000').replace('1.8 万','18000').replace('1.5 万','15000').replace('1.3 万','13000').replace('3.4 万','34000')
        if 'nan' not in d1 and 'nan' not in d2:
            if d1 in '2020-01':
                list_01.append(int(d2))
            if d1 in '2020-02':
                list_02.append(int(d2))
            if d1 in '2020-03':
                list_03.append(int(d2))
            if d1 in '2020-04':
                list_04.append(int(d2))
            if d1 in '2020-05':
                list_05.append(int(d2))
            if d1 in '2020-06':
                list_06.append(int(d2))
            if d1 in '2020-07':
                list_07.append(int(d2))
            if d1 in '2020-08':
                list_08.append(int(d2))
            if d1 in '2020-09':
                list_09.append(int(d2))
            if d1 in '2020-10':
                list_10.append(int(d2))
            if d1 in '2020-11':
                list_11.append(d2)
            if d1 in '2020-12':
                list_12.append(d2)

    y_data = []
    y_data.append(sum(list_01))
    y_data.append(sum(list_02))
    y_data.append(sum(list_03))
    y_data.append(sum(list_04))
    y_data.append(sum(list_05))
    y_data.append(sum(list_06))
    y_data.append(sum(list_07))
    y_data.append(sum(list_08))
    y_data.append(sum(list_09))
    y_data.append(sum(list_10))

    for i in list_11:
        i = str(i)
        if i == '':
            list_11.remove('')
    del list_11[-1]
    sum_11 = 0
    for i in list_11:
        i = int(i)
        sum_11 += i

    y_data.append(sum_11)

    del list_12[-1]

    sum_12 = 0
    for i in list_12:
        i = int(i)
        sum_12 += i
    y_data.append(sum_12)

    return y_data

def zhihu_radius():
    y_data = zhihu()
    x_data = ['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月']

    return x_data,y_data
#     c = (
#         Polar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
#         .add_schema(
#             radiusaxis_opts=opts.RadiusAxisOpts(data=x_data, type_="category"),
#             angleaxis_opts=opts.AngleAxisOpts(is_clockwise=True, max_=100000),
#         )
#         .add("点赞数量", y_data, type_="bar")
#         .set_global_opts(title_opts=opts.TitleOpts(title=""))
#         .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
#         .render("./templates/知乎图.html")
#     )
#
# if __name__ == '__main__':
#     zhihu_radius()