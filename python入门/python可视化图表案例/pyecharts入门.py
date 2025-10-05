"""
            pyecharts模块是百度开源的数据可视化
            pyecharts安装： pip install pyecharts   python包不清楚 ”模块与包“ 中有
            pyecharts 入门:
                        from pyecharts.charts import Line # 导包 这是折线图的使用
                        set_global_opts: 全局配置
"""
from numpy.f2py.auxfuncs import isunsigned_short
#折线图
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

# 创建一个折现图对象
line = Line()
# 添加x轴
line.add_xaxis(["早濑·优香","天童·爱丽丝 ","才羽桃"])
# 添加y轴
line.add_yaxis("KG",[200,45,45])
# 配置全局变量
line.set_global_opts(
    title_opts=TitleOpts(title="体重展示(KG)",pos_left="center",pos_bottom="1%"),
    legend_opts = LegendOpts(is_show=True),
    toolbox_opts= ToolboxOpts(is_show=True),
    visualmap_opts = VisualMapOpts(is_show=True)
)
line.render()
