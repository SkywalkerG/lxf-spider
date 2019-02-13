import json

# json 里面必须是双引号 所以外面拿单引号包裹
# 1. 字符串 dumps loads
# 字符串 --> dict list
# data = '{"name": "张三", "age": 18}'
data = '[{"name": "张三", "age": 18},{"name": "李四", "age": 28}]'

json_data = json.loads(data)
print(json_data, type(json_data))

# json_dict/list to str
json_data_to_string = json.dumps(json_data)
print(json_data_to_string, type(json_data_to_string))

# 2. 文件对象 dump load 和 dict list 转换
# 把列表或者字典存为json文件简写
json.dump(json_data, open('a.json', 'w'))

# 读取json文件为dict或者list
fp = open('a.json', 'r')
print(json.load(fp)) 