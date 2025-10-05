"""
            1。设计一个类:
                        class 类的名称: 使用class关键字进行声明一个类 类有属性 方法
                        类的属性: 使用class关键字定义的类中定义的变量
                        方法: 在使用class关键字定义中定义的方法 定义方法(def 方法名(self,形参1，形参2，形参3.........形参N):
                                                          self关键字是必须填写的。它用来表示自身的意思 在方法内部，
                                                          想要访问类的成员变量，必须使用self，尽管在参数列表中,但是传参的时候可以忽略它
            2.创建一个对象：
                         对象 =  类名称();  类只是一种程序内的"设计图纸"，需要基于图纸生产实体(对象)
                                                                ,才能工作这种套路，称之为面向对象
            3.对象赋值
                         1.对象名.属性/变量 = xxx
                         2.构造方法: 实例化对象时会自动调用构造方法同时类对象的传参会传递给构造方法因此可以用构造方法给成员变量赋值
                                        def __init__(self，成员变量1，成员变量2,成员变量) :
                                            def.成员变量1 =成员变量1
                                            def.成员变量2 =成员变量2
                                            def.成员变量3 =成员变量3
            4.常用的类内置方法(魔术方法):
                            __str__字符串方法：当对象需要被转换为字符串时，会输出内存地址
                            __lt__小于符号比较方法:两个对象直接比较是不可以的，但是可以用It方法 完成小于号和大于号两种比较
                            __le__小于等于比较符号方法:__le__可用于<=,>=两种比较运算符上
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
"""
        演示类和对象的关系，即面对对象的编程套路
        1.创建对象并实例化
        2.使用构造方法实例化对象
        3.常用的类内置方法(魔术方法)
"""
# 创建对象并实例化
class Clock:
    id = None  # 序列化
    price = None # 价格
    def ring(self):
        import winsound
        winsound.Beep(2000,3000)

clock1 = Clock()  # 构建出了clock1对象并将clock1的id 和price赋值 最后调用ring()方法
clock1.id = "0721"
clock1.price = "0721"
print(f"clock1的id为{clock1.id},clock1的价格为{clock1.price}")

# 使用构造方法实例化对象
class Student:
    name =None
    age =None
    School = None
    # 在Student类中声明构造函数
    def __init__(self,name,age,School):
        self.name =name
        self.age =age
        self.School = School
        print(f"学生姓名{name}\n年龄:{age}\n学校:{School}\n")
    # __str__魔术方法
    def __str__(self):   #将实例化的对象转换为字符串 return的必须为字符串类型
        return f"{self.name},{self.age},{self.School}" # 返回的是什么,对象转换成的字符串就是什么
    # __lt__魔术方法
    def __lt__ (self,other):
        return self.age <other.age
    # __le__ 魔术方法
    def __le__(self,other):
        return self.age <=other.age
    # __eq__魔术方法
    def __eq__(self,other):
        return self.age == other.age
# 构造方法
YUUKA =Student("早濑优香",16,"千禧年科技学院") #在实例化对象的同时将对象的属性赋上值
# 常用的类内置方法(魔术方法)
AL1S = Student("天童爱丽丝",5,"千禧年科技学院")
print(str(YUUKA))  #输出结果为 早濑优香 16 千禧年科技学院
print(str(AL1S))  #输出结果为 天童爱丽丝 5 千禧年科技学院
print(YUUKA <AL1S) #比较的是AL1S和YUUKA的age属性，此时AL1S<YUUKa 所以返回的是False
print(AL1S <= YUUKA)  #比较的是AL1S和YUUKA的age属性，此时AL1S<YUUKa 所以返回的是True
print(YUUKA == AL1S) ##比较的是AL1S和YUUKA的age属性，此时AL1S<YUUKa 所以返回的是False