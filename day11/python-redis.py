from redis import AuthenticationError

import redis

# 1. 链接数据库
# redis.Redis()
client = redis.StrictRedis(host="127.0.0.1",port=6379)

# 2. 设置key
key = "pyone"

# string 增删改查
# 增
result = client.set(key, "1")
print(result)
# 删
result = client.delete(key)
# 改
result = client.set(key, '2')
# 查询
result = client.get(key)
result = client.keys()

'''
分布式 
master 写入 1 
slave  读取 10 

1.当前电脑终端
window ipconfig 当前电脑的ip地址192.168.20.20
ubuntu ifconfig
查看ip地址

redis.config bind:192.168.20.20
重启服务
2. salve 
- 复制redis.conf  命名为 salve.conf
- 修改 bing:192.168.20.20
       slaveof 192.168.20.20 6379
       port 6378
  重启redis-server salve.conf
3. 查看关系 redis-cli h 192.168.20.20 info Relication
4. redis-cli -h 192.168.20.20 -p 6379
5. redis-cli -h 192.168.20.20 -p 6378
6. 在master 写入数据
7. 在salve 读取
'''
