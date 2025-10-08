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


"""
        异常的传递性:当函数func01中发生异常时，并且没有捕获处理这个异常的时候，
        异常会传递到函数func02,当异常func02也没有捕获到这个异常时mian函数会捕获这个异常
        注:简单来说异常传递性就是这个函数没有找到这个BUG，那么当另一个函数调用这个函数时这个BUG会带着这个函数一起调用
"""
# 定义一个出现异常的方法
def func1():
    print("func1 开始执行")
    num = 1/0
    print("func2 结束执行")
# 定义一个无异常的方法，调用func1方法
def func2():
    print("func1 开始执行")
    func1()
    print("func2 结束执行")
# 定义一个方法调用上面的方法
def main():
    func2() #单独执行这句话会出现很多异常
    try:        # 把上面的func2()注释后再执行try模块会正常运行
        func2()
    except Exception as e:
        print(e)
main()