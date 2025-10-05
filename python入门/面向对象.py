"""
            1。设计一个类:
                        class 类的名称: 使用class关键字进行声明一个类 类有属性 方法
                        类的属性: 使用class关键字定义的类中定义的变量
                        方法: 在使用class关键字定义中定义的方法 定义方法(def 方法名(self,形参1，形参2，形参3.........形参N):
                                                          self关键字是必须填写的。它用来表示自身的意思 在方法内部，
                                                          想要访问类的成员变量，必须使用self，尽管在参数列表中,但是传参的时候可以忽略它
            2.创建一个对象：
                         对象 =  类名称();
            3.对象赋值
            4.获取对象中记录的属性
"""
# 定义一个类 类中有属性（变量) 方法(函数)
class Student:
    name = None
    gender =None
    nationality =None
    age =None
    def myfunc(self,name):
        print(f"{name}天下第一")
stu_1 = Student()
stu_1.age = 16
stu_1.gender = "女"
stu_1.nationality = "千禧年科技学院"
stu_1.myfunc("早濑优香")
print(stu_1.name)
print(stu_1.gender)
print(stu_1.nationality)
print(stu_1.age)