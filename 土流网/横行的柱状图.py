import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import CurrentConfig,ThemeType
df = pd.read_excel('real_estate_info.xlsx').loc[:,['推出时间', '土地面积', '规划建筑面积']]
df['土地面积'] = df['土地面积'].str[:-1].map(float)
df['规划建筑面积'] = df['规划建筑面积'].str[:-1].map(float)
date = df['推出时间'].str.split('月',expand=True)[0]
date = date.apply(lambda x:x+'月')
df['月份'] = date
# df1 = df[(df['推出时间'].str[:4] == '2020') | (df['推出时间'].str[:4] == '2019')]
df2 = df.groupby('月份').agg({'土地面积':'sum'})/10000
df3 =df.groupby('月份').agg({'规划建筑面积':'sum'})/10000
#把时间写成一个列表
month = df2.index.tolist()
ydata_1 = [float('{:.2f}'.format(i)) for i in df2['土地面积']]

ydata_2 = [float('{:.2f}'.format(j)) for j in df3['规划建筑面积']]

bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
    .add_xaxis(xaxis_data=month)
    .add_yaxis(
        series_name='土地面积(万m²)',
        yaxis_data =ydata_1,
        stack='stack1', #堆叠
        label_opts=opts.LabelOpts(is_show=False)
    )
    .add_yaxis(
        series_name='规划建筑面积(万m²)',
        yaxis_data=ydata_2,
        stack='stack1',
        label_opts=opts.LabelOpts(is_show=False)
    )
    .reversal_axis() #反转 水平条形图
    .set_global_opts(
        xaxis_opts=opts.AxisOpts(name='万m²'),
        yaxis_opts=opts.AxisOpts(name='月份')
    )
    .render('reverse_bar.html')
)