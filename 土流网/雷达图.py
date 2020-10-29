import pandas as pd
from pyecharts.charts import Radar
from pyecharts import options as opts
from pyecharts.globals import CurrentConfig,ThemeType

df = pd.read_excel('real_estate_info.xlsx')['规划用途']
datas = df.value_counts()
items = datas.index.tolist()
colors = ['#FF0000', '#FF4500', '#00FA9A', '#FFFFF0', '#FFD700']
#radaritem:雷达图数据项配置
labels = [opts.RadarIndicatorItem(name=items[i],max_=100,color=colors[i])for i in range(len(items))]
value = [int(j) for j in datas.values]
radar = (
    Radar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
    .add_schema(
        schema=labels
    )
    .add(
        series_name='土地规划用途占比(%)',
        data = [[round(x/sum(value) * 100,3)for x in value]],
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5,color='blue') #区域填充颜色
    )
    .set_global_opts()
    .render('radar.html')
)