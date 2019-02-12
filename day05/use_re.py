import re

one = 'abc123'
pattern = re.compile('\d+')
# match 从头匹配，匹配一次
# result = pattern.match(one)

# search 从任意位置匹配， 匹配一次
# result = pattern.search(one)
# findall 查找符合的正则 内容
# result = pattern.findall(one)

# sub   替换字符串
# result = pattern.sub('#', one)


# split  拆分
pattern = re.compile('c')
result = pattern.split(one)


print(result)

# 匹配汉字
# [\u4e00-\u9fa5]