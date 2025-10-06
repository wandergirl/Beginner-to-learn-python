"""
        python操作MySQL:
            1.安装pymysql包 2.导包 3.将Connection Mysql的 用户 密码 port 主机 4.执行sql语句 5.关闭MySQL连接
                    导包: from pymysql import Connection

"""

from pymysql import Connection
conn = Connection(
    host ="localhost",
    port = 3306,
    user="root",
    password = "123456"
)
print(conn.get_server_info())

# 执行非查询语句
cursor = conn.cursor()
conn.select_db("test")
# 执行
cursor.execute("create table test_pymysql(id int);")


conn.close()
