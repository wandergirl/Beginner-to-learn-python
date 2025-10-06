"""
        创建河南省疫情地图
"""
import json

from pyecharts.charts import Map
from pyecharts.options import TitleOpts, VisualMapOpts

fn = open("D:\project\PythonData\python入门\python可视化图表案例\疫情.txt","r",encoding = "utf-8")
data = fn.read()
fn.close()
data_dict = json.loads(data)
cities = data_dict["areaTree"][0]["children"][3]["children"]
data_list = []
for city in cities:
    city_name =city["name"]+"市"
    city_confirm = city["total"]["confirm"]
    data_list.append((city_name,city_confirm))
print(data_list)
da = json.dumps(data_list,ensure_ascii=False)

fw = open("D:/疫情1.txt","r",encoding = "utf-8")
da1 =fw.read()
fw.close()
data_list = json.loads(da1)
map = Map()
map.add("河南疫情地图",data_list,"河南")
map.set_global_opts(
    title_opts = TitleOpts(title="河南省疫情地图"),
    visualmap_opts = VisualMapOpts(
        is_show = True,
        is_piecewise =True,
        pieces=[
            {"min": 1, "max": 50, "label": "1-50人", "color": "##CCFFFF"},
            {"min": 51, "max": 80, "label": "51-80人", "color": "#FFFF99"},
            {"min": 81, "max": 100, "label": "1000-4999", "color": "#FF9966"},
            {"min": 101, "max": 120, "label": "5000-9999", "color": "#FF6666"},
            {"min": 120, "max": 150, "label": "10000-99999", "color": "#CC3333"},
            {"min": 151, "max":200,"label": "99999+", "color": "#990033"},
            {"min": 201, "max":220,"label": "99999+", "color": "#990033"},
            {"min": 221, "max":240,"label": "99999+", "color": "#990033"},
            {"min": 260, "max":280,"label": "99999+", "color": "#990033"},
            {"min": 280, "max": 300, "label": "99999+", "color": "#990033"},
            {"min": 241, "max": 260, "label": "99999+", "color": "#990033"},
            {"min": 300, "max": 350, "label": "99999+", "color": "#990033"},

        ]
    )

)
map.render()






