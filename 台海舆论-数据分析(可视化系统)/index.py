from flask import Flask, render_template
from demo.Emotion_Bar import emotion_bar
from demo.Taiwan_pie import taiwan_pie
from demo.Taiwan_wordCloud import taiwan_wordcloud
from demo.Terrace_Line import terrace_line
from demo.Terrace_pie import terrace_pie
from demo.Time_Line import time_line
from demo.Weibo_Line import weibo_line
from demo.Zhihu_Radius import zhihu_radius

from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.charts import Bar
from pyecharts.charts import Pie
from pyecharts.charts import Polar

from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType
from pyecharts.charts import Line

app = Flask(__name__, static_folder="templates")

#词云图
list1 = taiwan_wordcloud()
with open('./台湾文本-数据/词云分析文本','w+',encoding='utf-8')as f:
    for l in list1:
        f.write(l+'\n')

#折线图1
x1,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10 = terrace_line()

#折线图2
x_data4,y_data4 = time_line()

#条形图
x_data5,y_data5 = weibo_line()

#极坐标-圆
x_data6,y_data6 = zhihu_radius()

@app.route("/")
def show_pyecharts():

    x_data = ['0.0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0']
    y_data = ['1533', '573', '502', '491', '520', '556', '577', '788', '1252', '20564', '6393']

    #情感分析柱状图
    bar = (
        Bar()
        .add_xaxis(x_data)
        .add_yaxis("情感分析", y_data, label_opts=opts.LabelOpts(is_show=False),color='#3498DB')
        .set_global_opts(
            title_opts={"text": "台海舆论情感分析", "subtext": "大于0.5为正面评价，小于0.5为负面评价"}
        )
    )

    #台湾网饼图
    x_data2 = ["文化", "经贸", "媒体专栏", "网友专栏", "两岸专家", "两岸", "台商", "部委", "台海时事", "网友快言", "海峡时评", "两岸快评"]
    y_data2 = [553, 553, 35, 39, 448, 465, 553, 321, 553, 406, 553, 556]

    pie = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
        .add(
            series_name="中国台湾网",
            data_pair=[list(z) for z in zip(x_data2, y_data2)],
            radius=["50%", "70%"],
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        )
        .set_colors(["#E8F8F5", "#D1F2EB", "#A3E4D7", "#76D7C4", "#48C9B0", "#1ABC9C","#17A589", "#148F77", "#117864", "#0E6251F", "#73C6B6", "#45B39D"])
        .set_global_opts(
            legend_opts=opts.LegendOpts(pos_left="legft", orient="vertical"))
        .set_series_opts(
            tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
            ),
        )
    )

    #词云图
    word = (
        WordCloud()
        .add(
            "",
            list1,
            word_size_range=[20, 100],
            shape=SymbolType.DIAMOND,
            textstyle_opts=opts.TextStyleOpts(font_family="cursive"), )
    )

    #折线图1
    y2[0], y2[1],y2[2] = None, None,None
    y4[1] = None
    line = (
        Line()
        .add_xaxis(xaxis_data=x1)
        .add_yaxis(
            series_name="微博",
            symbol="emptyCircle",
            is_symbol_show=True,
            color="#F2D7D5",
            y_axis=y1,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=3)
        )
        .add_yaxis(
            series_name="环球网",
            symbol="emptyCircle",
            is_symbol_show=True,
            color="#C0392B",
            y_axis=y2,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=3)
        )
        .add_yaxis(
            series_name="中国台湾网",
            symbol="emptyCircle",
            is_symbol_show=True,
            color="#641E16",
            y_axis=y3,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=3)
        )
        .add_yaxis(
            series_name="知乎",
            symbol="emptyCircle",
            is_symbol_show=True,
            color="#9B59B6",
            y_axis=y4,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=3)
        )
        .add_yaxis(
            series_name="中国日报网",
            symbol="emptyCircle",
            is_symbol_show=True,
            color="#512E5F",
            y_axis=y5,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=3)
        )
        .add_yaxis(
            series_name="中新网",
            symbol="emptyCircle",
            is_symbol_show=True,
            color="#2980B9",
            y_axis=y6,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=3)
        )
        .add_yaxis(
            series_name="今日头条",
            symbol="emptyCircle",
            is_symbol_show=True,
            color="#154360",
            y_axis=y7,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=3)
        )
        .add_yaxis(
            series_name="光明网",
            symbol="emptyCircle",
            is_symbol_show=True,
            color="#3498DB",
            y_axis=y8,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=3)
        )
        .add_yaxis(
            series_name="凤凰网",
            symbol="emptyCircle",
            is_symbol_show=True,
            color="#1ABC9C",
            y_axis=y9,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=3)
        )
        .add_yaxis(
            series_name="新华网",
            symbol="emptyCircle",
            is_symbol_show=True,
            color="#0E6251",
            y_axis=y10,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=3)
        )
        .set_global_opts(
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False, axisline_opts=opts.AxisLineOpts(
                is_on_zero=False, linestyle_opts=opts.LineStyleOpts(color="#d14a61")
            )),
        )
    )


    #平台占比饼图
    x_data3 = ["微博", "知乎", "中国台湾网", "环球网", "日报网", "中新网", "今日头条", "光明网", "凤凰网", "新华网"]
    y_data3 = [5401, 157, 5035, 3245, 4296, 5574, 1891, 3131, 1052, 1997]
    data_pair = [list(z) for z in zip(x_data3, y_data3)]
    data_pair.sort(key=lambda x: x[1])

    pie2 = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.ROMA))
        .add(
            series_name="访问来源",
            data_pair=data_pair,
            rosetype="radius",
            radius="55%",
            center=["50%", "50%"],
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{d}%"))
    )

    #折线图2
    line2 = (
        Line()
        .add_xaxis(xaxis_data=x_data4)
        .add_yaxis(
            series_name="热度走势",
            y_axis=y_data4,
            color="#FF69B4",
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
            symbol="emptyCircle",
            is_symbol_show=True,
            is_smooth=True,
            label_opts=opts.LabelOpts(is_show=True),
        )
        .set_global_opts(

            tooltip_opts=opts.TooltipOpts(is_show=False),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False,axislabel_opts=opts.LabelOpts(rotate=45)),
        )
    )

    #条形图
    line3 = (
            Bar()
            .add_xaxis(x_data5)
            .add_yaxis("平均值", y_data5, label_opts=opts.LabelOpts(is_show=False),color='#6A5ACD')
            .reversal_axis()
            .extend_axis(
                yaxis=opts.AxisOpts(
                    type_='value',
                    name='转发次数',
                    position='left',
                )
            )
            .set_global_opts(
                title_opts={"text": "评论与转发关系图"},
                xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter='{value}(评论数量)')),
            )
        )

    #圆
    radius = (
            Polar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add_schema(
                radiusaxis_opts=opts.RadiusAxisOpts(data=x_data6, type_="category"),
                angleaxis_opts=opts.AngleAxisOpts(is_clockwise=True, max_=100000),
            )
            .add("点赞数量", y_data6, type_="bar")
            .set_global_opts(title_opts=opts.TitleOpts(title=""))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
        )



    return render_template(
        "index2.html",
        bar_data=bar.dump_options(),word_data=word.dump_options(),
        pie_data=pie.dump_options(),pie2_data=pie2.dump_options(),
        line_data=line.dump_options(),line2_data=line2.dump_options(),
        line3_data=line3.dump_options(),radius_data = radius.dump_options()
    )


if __name__ == '__main__':
    app.run()

