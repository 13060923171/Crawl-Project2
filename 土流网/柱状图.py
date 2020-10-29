import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Bar
from pyecharts.globals import CurrentConfig,ThemeType

df = pd.read_excel('real_estate_info.xlsx').loc[:,['推出时间', '土地面积', '规划建筑面积']]
date = df['推出时间'].str.split('年',expand = True)[0]
df['年份'] = date
#去掉'平'，数据类型转化为float
df['土地面积'] = df['土地面积'].str[:-1].map(float)
df['规划建筑面积'] = df['规划建筑面积'].str[:-1].map(float)

#分组 求和 单位转换为万m2
land_area = df.groupby('年份').agg({'土地面积':'sum'}) / 10000
planned_area = df.groupby('年份').agg({'规划建筑面积':'sum'}) / 10000

#2016-2019年 爬取的数据 2020的只有两个月的数据 2015年的数据是9月份开始的
years = [int(y) for y in land_area.index[1:-1]]

ydata_1 = [float('{:.2f}'.format(i)) for i in land_area['土地面积'][1:-1]]

ydata_2 = [float('{:.2f}'.format(j)) for j in planned_area['规划建筑面积'][1:-1]]

#绘制柱状图
bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
    .add_xaxis(xaxis_data=years)
    .add_yaxis(
        series_name='土地面积(万m²)',
        yaxis_data=ydata_1,
        label_opts=opts.LabelOpts(is_show=False)
    )
    .add_yaxis(
        series_name='规划建筑面积(万m²)',
        yaxis_data=ydata_2,
        label_opts=opts.LabelOpts(is_show=False)
    )
    .set_global_opts(
        xaxis_opts=opts.AxisLineOpts(name='年份'),
        yaxis_opts=opts.AxisLineOpts(name = '万m²')
    )
    .set_series_opts(markarea_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_='max',name='最大值'),
                                                            opts.MarkPointItem(type_='min',name='最小值')]))
    .render('bar_.html')
)