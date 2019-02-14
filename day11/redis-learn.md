### Windows 进入到redis 安装目录下

```cmd
redis-cli.exe -h 127.0.0.1 -p 6379

127.0.0.1:6379>
```
conf文件设置
```conf
默认 bind 127.0.0.1 ::1  
注释掉之后 就允许 所有人访问 或者改成0.0.0.0

tcp-keepalive 300

daemonize no 是否线程守护

database 16 默认16个数据库 0-15
```
- 使用不同的数据库 select 0-15
```cmd
select 0
```
#### string
- 添加 set 添加键
```cmd
set one '1'
set two '2'
set three '3'
 ```
 - 查看键 keys *
 ```cmd
 keys *
```
 - 取键 get
 ```cmd
 get one 
 get two 
 get three 
```
- 清空所有键
```cmd
flushall 
```
- 设置多个键
```cmd
mset one 1 two 2 three 3
```
- 设置一个键在内存中存在的时间
```cmd
setex one 3 "abc"
```
- 字符串追加
```cmd
append one 99
```

#### hash 存对象 属性值
- 单个属性
```editorconfig
hset person name '张三'
hset person age 18
hset person gender false
```


- 多个属性
```editorconfig
hmset person name "李四" age  20  
```
- 查看
```editorconfig
hget person name 
hget person age 
hget person gender 
```
- 查看对象属性
```
hkeys student
hkeys person
```
- 查看对象的值
```
hvals student
hvals person
```
- 删除对象属性
```
hdel student name age
# 添加某些属性
hset student name "老王" age 18 height 180
```
#### list
- 添加值 lpush rpush 
```
lpush one 1
lpush one 2 3 4 5 6
```
- 查看值 lrange xx 0(索引起始位置) -1(索引结束位置) 
```
lrange one 0 -1
```
- 取出并删除值 lpop rpop 
```
lpop one 
```
- 指定位置插入
```
linsert key before 1 'a'
linsert key after 1 'b'
```
- 单独修改值根据索引
```
lset key index 新值
```
- 删除数据
```
lrem key count "值"
count > 0 从头删
      < 0 从尾删
      = 0 符合条件的所有删除
```
#### set
- 
```

```



#### python 操作redis
```python
from redis import  Redis
r = Redis(host='127.0.0.1',port=6379)
r.set({'name': 'Jobs'})
r.get('name')

```