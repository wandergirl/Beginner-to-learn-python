"""
        JSON: 是一种轻量的数据交互格式可以按照指定的格式去组织和封装数据本质上是一个带有特定格式的字符串
              在各个编程语言中流通负责不同的数据传递和交互
        JSON格式: {"name":"admin,"age":18}
                  也可以是[{"name":"admin","age":18},{"sex":"male,"length":"18"}]
"""
import  json
# 准备列表 列表转为JSON
data = [{"name":"早濑优香","age":16},{"name":"天童·爱丽丝","age":4}]
json_str = json.dumps(data,ensure_ascii=False)
print(type(json_str))
print(json_str)
# 准备字典 字典转为JSON
data = {"name":"早濑优香","age":16,"name":"天童·爱丽丝","age":4}
json_str1 = json.dumps(data,ensure_ascii=False)
print(type(json_str1))
print(json_str1)
l = '{"name":"早濑优香","age":16,"name":"天童·爱丽丝","age":4}'
l =json.loads(l)
print(type(l))
print(l)
