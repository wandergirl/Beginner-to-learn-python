
"""
        文件的读取
        在python中，使用open函数可以打开一个已经存在的文件，或者创建一个新文件 语法为：
        open(name,mode,encoding)
        name: 是要打开的目标文件名的字符串（可以包含文件所在的具体路径)。
        mode: 设置打开文件的模式(访问模式)：只读、写入、追加等
        encoding: 编码格式（推荐使用UTF-8）
"""

f = open("C:/Users/AL1S8/Desktop/python文档.txt",'r',encoding= 'utf-8')
print(type(f))
# print(f.read())
# readline一次只能读取一行
print(f.readline())
print(f.readlines())
# close() 关闭文件
f.close()
"""
 文件写入: 1.文件打开 2.文件写入 3.文件刷新
 f = open("xxx.txt","w",encoding="utf-8")
 f.write("文件写入的内容") 文件写入
 f.flush() 内容刷新
 注:文件写入2个特点： 1.当文件不存在时会创建该文件 2.当文件存在时创建该文件会清空前一个文件内容
"""

f = open("D:/python测试.txt","w",encoding = 'utf-8')
f.write("我用python写程序")
f.flush()
f.close()
f1 =open("D:/python测试.txt","w",encoding = "utf-8")
f1.write("学习大数据技术")

f1.close()
f2 = open("D:/python测试.txt","r",encoding = "utf-8")
print(f2.read())
f2.close()


"""
  文件的追加操作： 1.打开文件 2.文件写入 3.内容刷新
  打开文件 通过a模式打开即可 open("xxx.txt","a",encoding="utf-8")
  写入文件 write("xxxxx")
  内容刷新 flush()
  close() 关闭文件     
  注：1.文件的追加会创建文件 2.文件的追加会在存在的文件后面写入内容
"""
# 打开一个存在的文件
f = open("D:/python测试.txt","a",encoding = 'utf-8')
f.write("\n学得本领月薪过万")
f.flush()
f.close()
f = open("D:/python测试.txt","r",encoding = "utf- 8")
print(f.read())
f.close()
# 打开一个不存在的文件
f3 = open("D:/python1.txt","a",encoding = "utf-8") # 报会创建文件
f3.write("早濑优香天下第一\n")
f3.close()
f4 = open("D:/python.txt","r",encoding = "utf-8")
print(f4.read())
