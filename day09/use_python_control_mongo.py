from pymongo import MongoClient

try:
    client = MongoClient()
    # 库名
    six = client['six']
    # 表名
    stu = six['stu']


    # one = {"name":"张三", "age":50}
    # two_many = [
    #     {"name":"小三", "age":50},
    #     {"name":"李四", "age":30},
    #     {"name":"王五", "age":20},
    #     {"name":"小刘", "age":15}
    # ]
    # 增 insert insert_one insert_many
    # stu.insert_one(one)
    # stu.insert_many(two_many)

    # 删 remove
    # stu.delete_one({'age': 15})
    # stu.delete_many({'age':50})

    # 改 update update_one updata_many
    # stu.update_one({"name": "李四"}, {"$set":{"name":"小四"}})

    # 查询 find find_one
    # result = stu.find_one({"age":50})
    # print(result)
    results = stu.find({"age":50})
    # for i in results:
    #     print(i)

except Exception as e:
    print(e)
finally:
    #关闭数据库
    client.close()