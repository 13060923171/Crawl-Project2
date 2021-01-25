import pyecharts.options as opts
from pyecharts.charts import Pie
from pyecharts.globals import ThemeType

x_data = ["文化", "经贸", "媒体专栏", "网友专栏", "两岸专家","两岸","台商","部委","台海时事","网友快言","海峡时评","两岸快评"]

y_data = [553,553,35,39,448,465,553,321,553,406,553,556]


def taiwan_pie():
    c = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.VINTAGE))
        .add(
            series_name="中国台湾网",
            data_pair=[list(z) for z in zip(x_data, y_data)],
            radius=["50%", "70%"],
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="台湾网各项比重",pos_left='35%',pos_top='5%'),
            legend_opts=opts.LegendOpts(pos_left="legft", orient="vertical"))
        .set_series_opts(

            tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
            ),
        )
        .render("./templates/台湾网占比图.html")
    )

if __name__ == '__main__':
    taiwan_pie()