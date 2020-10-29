import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.globals import CurrentConfig,ThemeType

#读取数据
df = pd.read_excel('real_estate_info.xlsx').loc[:,['出让形式','成交状态']]
#统计
df1 = df['出让形式'].value_counts()
df2 = df['成交状态'].value_counts()
#构造data_pair
data_pair_1 = [(i, int(j)) for i, j in zip(df1.index, df1.values)]
data_pair_2 = [(i, int(j)) for i, j in zip(df2.index, df2.values)]
#绘制饼图
c = (
    Pie(init_opts=opts.InitOpts(theme="成交方式占比图",width="1100px",height='500px'))
    .add(
        "土地出让形式",
        data_pair_1,
        center=['25%','50%'],
        label_opts=opts.LabelOpts(is_show=True)
    )
    .set_colors(['red','blue','green'])
    .add(
        "土地成交状态",
        data_pair_2,
        center=['70%','50%'],
        label_opts=opts.LabelOpts(is_show=True),
    )

    .set_global_opts(title_opts=opts.TitleOpts(title="土地出让形式&土地成交状态占比"),legend_opts=opts.LegendOpts(is_show=False))
    .set_series_opts(tooltip_opts=opts.TooltipOpts(trigger='item',formatter="{a} <br/>{b}: {c} ({d}%)"))
    .render("pie_.html")
)