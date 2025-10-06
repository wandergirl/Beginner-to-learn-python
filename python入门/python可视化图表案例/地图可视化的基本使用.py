from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts, TitleOpts

map = Map()
data = [
    ("北京市",9999),
    ("上海市",999),
    ("广东省",999)
]
map.add("中国黑人分布地图",data,"china")
map.set_global_opts(
    visualmap_opts = VisualMapOpts(
        is_show=True,
        is_piecewise = True,
        pieces = [
            {"min":1,"max":999,"label":"1-999","color":"black"},
            {"min":999,"max":9999,"label":"999-9999","color":"red"}
                                   ]
                                   ),
title_opts = TitleOpts("中国黑人分布地图",pos_left="center",pos_bottom="1%"),

)
map.render()

