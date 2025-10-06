"""
            全国疫情可视化地图开发

"""
import json

from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts, TitleOpts
from pyecharts.types import VisualMap

# 读取数据文件
f = open("D:\project\PythonData\python入门\python可视化图表案例\疫情.txt","r",encoding = 'utf-8')
data = f.read();  # 将读取到的数据赋值给data
# 关闭文件
f.close()
# 字符串josn 转换为 python的字典
data_dict = json.loads(data)
# 从字典中取出省份的数据
province = data_dict["areaTree"][0]["children"]
# 组装每个省份和确诊人数为元组，并各个省的数据封装入列表内
data_list = []
for item in province :
    province_name = item["name"]
    province_confirm = item["total"]["confirm"]
    data_list.append([province_name,province_confirm])

print(data_list)

data_list.append(["济源市",5])
map = Map()
map.add("各省份确诊人数",data_list,"china")
map.set_global_opts(
    title_opts = TitleOpts(title = "全国疫情地图"),
    visualmap_opts = VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99, "label": "1-99人", "color": "##CCFFFF"},
            {"min":100, "max": 499, "label": "100-499人", "color": "#FFFF99"},
            {"min":500, "max": 1000, "label": "1000-4999", "color": "#FF9966"},
            {"min":2000, "max": 5000, "label": "5000-9999", "color": "#FF6666"},
            {"min":5001, "max": 99999, "label": "10000-99999", "color": "#CC3333"},
            {"min":100000, "label": "99999+", "color": "#990033"}
        ]
    ),
)


map.render()

