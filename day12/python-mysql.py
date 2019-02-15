import pymysql

try:
    # 1.连接数据库 连接对象conncetion
    conn = pymysql.Connect(
        host= "localhost",
        port=3306,
        db="animal",
        user="root",
        passwd="root123",
        charset="utf8"
    )

    # 建库建表 插入数据
    # 2.创建游标对象 cursor
    cursor = conn.cursor()

    # 添加一条数据 科目表 -- GO语言
    # insert_sub = 'insert into subject values(0,"GO 语言")'
    # result = cursor.execute(insert_sub)
    # 修改
    # update_sub = 'update subject set title="区域块链接" where title="GO 语言"'
    # result = cursor.execute(update_sub)
    # 删除
    # delete_sub = 'delete from subject where id=3'
    # result = cursor.execute(delete_sub)
    # 查询
    query_sub = 'selet * from subject'
    cursor.execute(query_sub)
    # fetchone fetchall
    result = cursor.fetchall()
    print(result)
    # 提交事务
    conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
except Exception as e:
    print(e)
