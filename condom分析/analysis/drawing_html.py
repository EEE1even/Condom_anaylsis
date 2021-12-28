# -*- coding: utf-8 -*-
# @Time :    2021/12/8  14:55
# @Author :  Eleven
# @Site :    
# @File :    drawing_html.py
# @Software: PyCharm

import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import *
from pyecharts.components import Table
from pyecharts.globals import ThemeType, SymbolType
from pyecharts.options import ComponentTitleOpts


def map_sales_areas():
    data = pd.read_csv('./data/new_condom_data.csv')
    areas = list(data['地区'])

    area_list = list(data['地区'].unique())
    sales = list(data['付款人数'])
    sum_list = []
    # print(area_list)
    #循环计算各个地区的付款人数总和
    for k in area_list:
        sum = 0
        for i,j in zip(areas,sales):
            if i == k:
                sum += j
        sum_list.append(sum)
    # print(sum_list)
    c = (
        Map(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))
            .add("销售量", [list(z) for z in zip(area_list,sum_list)], "china",is_map_symbol_show=False,
                 label_opts=opts.LabelOpts(is_show=False)
                 )
            .set_global_opts(
            legend_opts=opts.LegendOpts(is_show=False),
            title_opts=opts.TitleOpts('全国地区商家销售量',pos_left='center'),
            visualmap_opts=opts.VisualMapOpts(max_=max(sum_list)),
        )
    #     .render("./html/china_map.html")
    )
    return c

def wordCloud():
    data = pd.read_excel('../jieba_data/condom_message.xlsx')
    #转换成元组
    data = data.apply(lambda x: tuple(x), axis=1).values.tolist()
    w = (
        WordCloud(init_opts=opts.InitOpts(theme=ThemeType.WESTEROS))
            .add(series_name="", data_pair=data,shape='circle',word_size_range=[15,80])
            .set_global_opts(
            title_opts=opts.TitleOpts(title='搜索关键词组',pos_left='center'),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
            # .render("./html/basic_wordcloud.html")
    )
    return w

def time_bar_commodity():
    D_thin = pd.read_excel('../jieba_data/D_thin.xlsx')
    D_air = pd.read_excel('../jieba_data/D_air.xlsx')
    D_lasting = pd.read_excel('../jieba_data/D_lasting.xlsx')
    O_001 = pd.read_excel('../jieba_data/O_001.xlsx')
    O_lasting = pd.read_excel('../jieba_data/O_lasting.xlsx')
    J = pd.read_excel('../jieba_data/J.xlsx')
    Siki = pd.read_excel('../jieba_data/Siki.xlsx')
    commodity = [D_thin,D_air,D_lasting,O_001,O_lasting,J,Siki]
    names = ['杜蕾斯焕金超薄','杜蕾斯空气','杜蕾斯持久','冈本001超薄','冈本持久','杰士邦001持久','私激']

    def get_x(data):
        df = data.head(10)
        x = list(df['词组'])
        return x[::-1]
    def get_y(data):
        df = data.head(10)
        y = list(df['频率'])
        return y[::-1]

    tl = (
        Timeline(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))
        .add_schema(pos_right='10',
                    pos_left='10',
                    is_auto_play=True,
                    play_interval=4444,
                    pos_bottom='10px'
                    )
    )

    for element,name in zip(commodity,names):
        bar = (
            Bar(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))
                .add_xaxis(get_x(element))
                .add_yaxis('次数',get_y(element))
                 #横向柱状图
                .reversal_axis()
                .set_series_opts(label_opts=opts.LabelOpts(position="right",font_size=15,color='white'))
                .set_global_opts(title_opts=opts.TitleOpts('{}避孕套词频前十统计'.format(name),pos_left='center'),
                                 legend_opts=opts.LegendOpts(is_show=False),
                                 xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(is_show=False)),
                                 yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=15,color='white'))
                                 )
        )
        tl.add(bar,'{}'.format(name))
    # tl.render('./html/bar_timeline.html')
    return tl

def price_interval():
    data = pd.read_csv('./data/new_condom_data.csv')
    price = list(data['价格'])
    a = []
    b = []
    c = []
    d = []
    e = []
    f = []
    x = ['价格区间：0~20','价格区间：20~40','价格区间：40~60','价格区间：60~80','价格区间：80~100','价格区间：100以上']
    y = []
    for i in price:
        if 0 < i <= 20:
            a.append(1)
        if 20 < i <= 40:
            b.append(1)
        if 40 < i <= 60:
            c.append(1)
        if 60 < i <= 80:
            d.append(1)
        if 80 < i <= 100:
            e.append(1)
        if i > 100:
            f.append(1)
    for i in (a,b,c,d,e,f):
        y.append(len(i))

    c = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))
            .add(
            "",
            [list(z) for z in zip(x, y)],
            radius=["30%", "75%"],
            center=["50%", "50%"],
            rosetype="area",
            label_opts=opts.LabelOpts(font_size=15,color='white', font_weight='bold')

        )
            .set_global_opts(
            legend_opts=opts.LegendOpts(is_show=False),
            title_opts=opts.TitleOpts(title='价格区间分布',pos_left='center')
        )

        # .render('./html/rose_pie.html')
    )
    return c

def business_area_bar():
    data = pd.read_csv('./data/new_condom_data.csv')
    areas = data['地区']
    num_area = areas.value_counts()
    x = list(num_area.index)
    y = list(num_area)
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))
            .add_xaxis(x)
            .add_yaxis("商家个数", y)
            .set_global_opts(
            title_opts=opts.TitleOpts(title='商家分布情况',subtitle='淘宝前50页商品',pos_left='center'),

            legend_opts=opts.LegendOpts(is_show=False),
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=15,color='white')),
            yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=15))
        )
            .set_series_opts(label_opts=opts.LabelOpts(
                                                       color='white'#数据标签的颜色
                                                       ,font_size=12
                                                       # ,formatter #数据标签显示格式
                                                       )##设置数据标签的格式s
            )
            # .render("./html/bar_business.html")
    )
    return c

def Page_show():
    c = (
        Page(layout=Page.DraggablePageLayout)
        .add(
            map_sales_areas(),
            wordCloud(),
            time_bar_commodity(),
            price_interval(),
            business_areaSales()
        )
        .render('./html/page.html')
    )

def business_areaSales():
    data = pd.read_csv('./data/new_condom_data.csv')
    areas = list(data['地区'])
    area_list = list(data['地区'].unique())
    sales = list(data['付款人数'])
    sum_list = []
    # print(area_list)
    #循环计算各个地区的付款人数总和
    for k in area_list:
        sum = 0
        for i,j in zip(areas,sales):
            if i == k:
                sum += j
        sum_list.append(sum)
    areas = data['地区']
    num_area = areas.value_counts()
    x = list(num_area.index)
    y = list(num_area)
    #转换为字典
    commodity_list = dict(zip(x,y))
    sales_list = dict(zip(area_list,sum_list))
    tmp = []
    #求出每个地区的商家平均销售数量
    for key in area_list:
        mean = sales_list[key]/commodity_list[key]
        tmp.append(int(mean))
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))
            .add_xaxis(area_list)
            .add_yaxis("平均销售量", tmp)
            .set_global_opts(
            title_opts=opts.TitleOpts(title='不同地区商家的平均销售数量',subtitle='淘宝前50页商品',pos_left='center'),

            legend_opts=opts.LegendOpts(is_show=False),
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=15,color='white')),
            yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=15))
        )
            .set_series_opts(label_opts=opts.LabelOpts(color='white',is_show=True)##设置数据标签的格式s
        )
        # .render("./html/areaSales_business.html")
    )
    return  c

def table_condom():
    D_thin = pd.read_excel('../jieba_data/D_thin.xlsx')
    D_air = pd.read_excel('../jieba_data/D_air.xlsx')
    D_lasting = pd.read_excel('../jieba_data/D_lasting.xlsx')
    O_001 = pd.read_excel('../jieba_data/O_001.xlsx')
    O_lasting = pd.read_excel('../jieba_data/O_lasting.xlsx')
    J = pd.read_excel('../jieba_data/J.xlsx')
    Siki = pd.read_excel('../jieba_data/Siki.xlsx')
    name_list = [D_thin,D_air,D_lasting,O_001,O_lasting,J,Siki]
    names = ['杜蕾斯焕金超薄','杜蕾斯空气','杜蕾斯持久','冈本001超薄','冈本持久','杰士邦001持久','私激']
    rubbish_num = []
    for name in name_list:
        tmp = 0
        for value,num in zip(name['词组'],name['频率']):
            if value == '不好' or value == '垃圾' or value == '差评':
                tmp += num
        rubbish_num.append(tmp/2000)
    headers = ['产品名称','差评词频占比']
    rows = []
    #添加成二维列表
    for i,j in zip(names,rubbish_num):
        tmp = []
        tmp.append(i)
        tmp.append(j)
        m = list(tmp)
        rows.append(m)
    table = Table()
    table.add(headers, rows)
    table.set_global_opts(
        title_opts=ComponentTitleOpts(title="每件产品追评的差评率", subtitle="频率排名前50的词组")
    )
    # table.render("./html/table.html")
    return table

if __name__ == '__main__':
    Page_show()
    # Page.save_resize_html("./html/page.html", cfg_file="./html/chart_config.json", dest="./html/my_new_charts.html")




