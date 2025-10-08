"""
            封装：将类中的成员(方法与变量)设置为私有,禁止外界访问
                    功能：访问限制 类对象无法访问 类中的其他成员可以访问
                    定义：定义私有成员无论是变量还是方法都均以__开头
            继承:继承分为单继承和多继承
                   class 类名(父类名): #单继承的语法
                   class  类名(父类名1,父类名2,父类名3...) #多继承的语法
                                                    多继承的优先权:如果父类中有同名的方法或属性，先继承的优先级高于后继承
            复习父类成员：子类继承父类的成员属性和成员方法后，如果对其"不满意",那么可以进行复写 在子类中重新定义同名的函数即可
                        super.父类的成员   调用super可以调用父类中的成员
            类型注解: 帮助第三方工具对代码进行类型推断,协助做代码提示
                    帮助开发者自身对变量进行类型注释 支持 变量的类型注解 函数(方法) 形参列表和返回值的类型注解
                    变量 : 类型 #注解的方式  该变量是xxx类型
            多态:  同样的行为，传入不同的对象，得到不同的状态 多态常作用在继承关系上
                    函数(函数)形参声明接受父类对象 实际传入父类的子类对象进行工作
            抽象类: 更多情况下多态是发生在抽象类中的，抽象类是含有抽象方法的类，抽象方法是方法体是空实现的(pass)称之为抽象方法
                        抽象类就好比定义一个标准
                  定义  class A :
                            def cool_wind(self):
                                pass
                        包含了抽象方法的类必须实现
"""
#  实现封装 定义一个类将其中一个方法私有化并通过另一个方法来访问
class Phone:
    id = None
    IMEI =None
    def __lscpu(self):  # 将lscpu设置为私有方法
        print("我的cpu架构是arm-64 7a")
    def showmyself(self):  # 通过访问__lscpu()方法来调用私有方法，同时也是IPhone子类所没有的方法
        self.__lscpu()
IPhone =Phone()
IPhone.showmyself()
# 定义calling类用来实现python的多继承
class calling :
    def call(self):
        print("打电话功能")
class watching_video :
    def watching(self):
        print("看视频功能")
# 定义一个类来实现python类的单继承
class IPhone(Phone):
    def show(self):   # 这个方法是父类所没有的方法
        print("我是新款手机")
phone = IPhone()
phone.showmyself()

# 定义一个类来实现类的多继承和多态
class HUAWEI(Phone,watching_video,calling):
    def call(self):
        print("开启5G进行高质量通话")
    def watching(self):
        print("观看8k高清视频")
    def showmyself(self):
        print("采用最新的3nm工艺的cpu")
        # 定义XIAOMI类来实现类的多态
class XIAOMI(Phone,watching_video,calling):
    def call(self):
        print("使用卫星通话")

    def watching(self):
        print("开启省流量模式观看8k高清视频")

    def showmyself(self):
        print("升级最新的系统")
# 实例化对象实现多继承 通过多继承来使用父类的方法
HPhone =HUAWEI()    # 这些方法使用了方法的复习，将继承的父类中的的成员重写
HPhone.showmyself()
HPhone.watching()
HPhone.call()
# 基础类型注解
Name : str
Age : int
Height : int
# 容器类型注解
my_list : list[int] = [1,2,3]
my_tuple : tuple[int] = (1,2,3)
my_dict : dict[str, int] = {"1":1,"2":2,"3":3}

# 多态使用子类对象来调用函数
     # 聊一会儿天，调用call函数
def talk(Calling : calling) :
    Calling.call()

hPhone = HUAWEI()   #创建了HUAWEI的对象hphone HUAWEI继承了 Phone watching_video calling 类 子类实例化对象的时候会调用calling 方法  会执行父类中的calling方法
talk(hPhone)
mphone = XIAOMI() ##创建了XIAOMI的对象mphone XIAOMI继承了 Phone watching_video calling 类 子类实例化对象的时候会调用calling 方法  会执行父类中的calling方法
talk(mphone)


"""
使用抽象类来实现多态
"""
class AC :
    def cool_wind(self):
        pass
    def hot_wind(self):
        pass
    def swing_l_r(self):
        pass
class Midea_AC (AC):
    def cool_wind(self):
        print("美的空调制冷")
    def hot_wind(self):
        print("美的空调制热")
    def swing_l_r(self):
        print("美的空调上下摆风")
def need(ac : AC):
    ac.cool_wind()
    ac.hot_wind()
    ac.swing_l_r()
Midea =Midea_AC()
need(Midea)