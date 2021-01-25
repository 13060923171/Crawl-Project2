import pyecharts.options as opts
from pyecharts.charts import Pie



x_data = ["微博", "知乎", "中国台湾网", "环球网","日报网", "中新网", "今日头条", "光明网","凤凰网", "新华网"]
y_data = [5401, 157, 5035, 3245,4296,5574,1891, 3131,1052,1997]
data_pair = [list(z) for z in zip(x_data, y_data)]
data_pair.sort(key=lambda x: x[1])

def terrace_pie():
    c = (
        Pie(init_opts=opts.InitOpts(bg_color="#2c343c"))
        .add(
            series_name="访问来源",
            data_pair=data_pair,
            rosetype="radius",
            radius="55%",
            center=["50%", "50%"],
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="2020年台海局势各平台占比情况",
                pos_left="center",
                pos_top="20",
                title_textstyle_opts=opts.TextStyleOpts(color="#fff"),
            ),
            legend_opts=opts.LegendOpts(is_show=False),
        )
        .set_series_opts(
            tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
            ),
            label_opts=opts.LabelOpts(color="rgba(255, 255, 255, 0.3)"),
        )
        .render("./templates/2020年台海局势各平台占比情况图.html")
    )

if __name__ == '__main__':
    terrace_pie()