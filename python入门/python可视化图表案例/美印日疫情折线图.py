"""
        目标：生成美国、印度、日本三个国家的疫情折线图
        任务:1.处理数据将这三个国家的文本文档的数据处理成JSON格式
             2.把这三个国家的JSON数据转换为字典类型
             3，把这些数据中所需要的数据整理出来
             4.利用数据生成x轴和y轴 生成折线图
"""

# 处理三国数据

import json  # 导入JSON模块
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, ToolboxOpts, LegendOpts, VisualMapOpts

f_us = open("D:\project\PythonData\python入门\python可视化图表案例\美国.txt","r",encoding="utf-8")
us_data = f_us.read()  #使用 r 模式打开文件并读取文件
f_jp = open("D:\project\PythonData\python入门\python可视化图表案例\日本.txt","r",encoding="utf-8")
jp_data = f_jp.read()  #使用 r 模式打开文件并读取文件
f_in = open("D:\project\PythonData\python入门\python可视化图表案例\印度.txt","r",encoding="utf-8")
in_data = f_in.read()  #使用 r 模式打开文件并读取文件
us_data =us_data.replace("jsonp_1629344292311_69436(","") # 将读取到的数据赋值给us_data,将开头不符合规范的数据替换为空
jp_data =jp_data.replace("jsonp_1629350871167_29498(","") # 将读取到的数据赋值给jp_data,将开头不符合规范的数据替换为空
in_data =in_data.replace("jsonp_1629350745930_63180(","") # 将读取到的数据赋值给in_data,将开头不符合规范的数据替换为空
us_data = us_data[:-2] #把美国JSON中最后两个不符合规范的字符删去
jp_data = jp_data[:-2] #把日本JSON中最后两个不符合规范的字符删去
in_data = in_data[:-2] #把印度JSON中最后两个不符合规范的字符删去
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)
# 获取trend key
us_trend_data = us_dict["data"][0]["trend"]
# 获取日期数据用于x轴取2020年(到314下标)
us_x_data = us_trend_data["updateDate"][:314]
# 获取日期数据用于x轴取2020年(到314下标)
us_y_data = us_trend_data["list"][0]["data"][:314]
jp_trend_data = jp_dict["data"][0]["trend"]
# 获取日期数据用于x轴取2020年(到314下标)
jp_x_data = jp_trend_data["updateDate"][:314]
# 获取日期数据用于x轴取2020年(到314下标)
jp_y_data = jp_trend_data["list"][0]["data"][:314]
# 获取trend key
in_trend_data = in_dict["data"][0]["trend"]
# 获取日期数据用于x轴取2020年(到314下标)
in_x_data = in_trend_data["updateDate"][:314]
# 获取日期数据用于x轴取2020年(到314下标)
in_y_data = in_trend_data["list"][0]["data"][:314]
# 生成图表
line = Line()
line.add_xaxis(us_x_data)
line.add_yaxis("美国确诊人数", us_y_data)
line.add_xaxis(jp_x_data)
line.add_yaxis("日本确诊人数", jp_y_data)
line.add_xaxis(us_x_data)
line.add_yaxis("印度确诊人数", in_y_data)
# 设置全局选项
line.set_global_opts(
    title_opts=TitleOpts(title="2020年美日印三国确诊人数对比折线图",pos_left="center",pos_bottom="1%"),
    legend_opts = LegendOpts(is_show=True),
    toolbox_opts= ToolboxOpts(is_show=True),
    visualmap_opts = VisualMapOpts(is_show=True)

)
line.render()
f_us.close()
f_in.close()
f_jp.close()
