"""
        python操作MySQL:
            1.安装pymysql包 2.导包 3.将Connection Mysql的 用户 密码 port 主机 初始化 4.执行sql语句 5.关闭MySQL连接
                    导包: from pymysql import Connection
                    Connection Mysql的 用户 密码 port 主机 初始化:    实例化 Connection对象并将数据库的信息初始化,
                                                                       创建游标对象cursor Connection对象.cursor
                    执行sql语句: 使用Connection对象选择数据库 conn.select_db("目标数据库")
                                使用游标对象cursor执行数据库语句
                    关闭MySQL连接关闭数据库连接 :Connection对象.close()
            注：pymysql库在执行对数据库有修改操作的行为时，是需要通过链接对象commit成员方法来进行确认只有确认的修改才能生效
                自动提交：在Connection对象实例化时将自动提交语句写上即可

"""

from pymysql import Connection
conn = Connection(
    host ="localhost", #本机名
    port = 3306, #端口
    user="root", # 账户
    password = "123456",# 密码
)
print(conn.get_server_info())

# 执行非查询语句
cursor = conn.cursor #创建游标对象
conn.select_db("test") # 选择数据库
# 使用游标对象执行mysql语句
cursor.execute("create table test_pymysql1(id int)") #执行创建表的语句

#cursor.execute("insert into test_pymysql values(1)")
conn.close()
