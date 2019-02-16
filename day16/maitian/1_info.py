import pandas as pd

# 读取文件
df = pd.read_json('maitian.json')
# print(df)
# print(dir(df))
# 列名
print(df.columns)
print('********'*3)
# 使用pandas的describe方法,打印基本信息
print(df.describe())
print('********'*3)
# 按照列名 统计个数 都是一样的
print(
    df['location'].value_counts()
)

