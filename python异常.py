"""
        异常:软件可能会出现的BUG即程序运行过程中的错误
        异常的捕获: 1.捕获可能出现的异常:
                   try:
                   # 可能出现的代码
                   except:
                   # 如果出现异常的代码
                  2.捕获指定异常：
                    try:
                        #可能出现异常的一行代码
                    except NameError as e: # NameError 是可能出现的NameError异常类型即变量名没有赋值
                        # 如果出现异常的代码
                  3.捕获多个异常：
                      try：
                         #可能出现异常的代码
                      except (NameError,ZeroDivisionError) as e: #NameError ZeroDivision 分别是会出现异常的类型
                         # 如果出现异常的代码
                  4.捕获所有异常:
                       try:
                        #可能出现异常的一行代码
                    except Exception as e: # NameError 是可能出现的所有异常类型
                        # 如果出现异常的代码
"""
# 基本捕获异常的语法
try:
    f = open("c:/aoteman","r",encding="utf-8")

except:
    print("出现异常，将以w模式打开")
    f = open("D:/早濑优香.txt","w",encoding = 'utf-8')
    f.write("早濑优香天下第一");
    try:
        print(f.read())
    except:
        f = open("D:/早濑优香.txt","r",encoding = 'utf-8')
        print(f.read())
    f.close()
# 捕获指定异常
try:
    name = "早濑邮箱"
    print(name)
except NameError as e:
    print("出现了变量未定义的异常")
    print(e)
# 捕获多个异常
try:
    1 / 0
except (ZeroDivisionError,NameError) as e:
    print(e)
# 捕获所有的异常
try:
    1/0
except Exception as e:
    print(e)
"""
     异常的finally:表示有没有异常都要执行的代码，例如关闭文件。
     
"""
try:
    f = open("D:/早濑优香.txt","r",encoding = 'utf-8')
except Exception as e:
    f = open("D:/早濑优香.txt","w",encoding = 'utf-8')
else:
    print("没有异常")
finally: # 无论是否出现异常 finally里面的代码块都会执行
    print(f.read())