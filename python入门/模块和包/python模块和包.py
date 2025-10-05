"""
        模块：是一个Python文件，以.py结尾。
             模块能定义函数，类和变量，模块里也能包含可执行的代码
             模块就是一个Python文件，里面有类、函数、变量等，可以直接拿来用
        模块的导入：
                from [模块名] import [模块 | 类 | 变量 | 函数 ] [as 别名]
                常用的组合形式：
                import 模块名
                from 模块名 import 类、变量、方法等
                from 模块名 import *
                import 模块名 as 别名
        =====================================================================================================
        python包：物理层面上python包就是一个文件夹该文件夹包含读个模块文件包含了一个__init__.py文件
                 逻辑层面上python包的本质仍然是模块
        导入python包：import 包名.模块
                    from 包名.模块 import 功能
        __all__变量：当模块/python文件被__all__修饰时在from xxx.xxxx import * 导包时 被__all__修饰的部分才能被导出使用
        安装第三方包： 同时按下win键和R键弹出的运行框中输如cmd回车 在命令提示符中输入 pip install xxxx  来安装第三方包

        本文件就是 "python模块和包"里面的和MyModule.py是互通的
"""


# 导入时间模块
import time
time.sleep(1)  # 使用sleep 函数
# 从time模块导入sleep函数
from time import sleep
print(sleep(1))
# 从time模块引入所有功能
from time import *
sleep(1)  # 可以直接使用功能
# 使用as特定功能加上别名
from time import sleep as sl #as 给sleep起了一个sl的别名
sl(1)
"""
        自定义模块: 新建一个python文件 import到当前文件中即可
        当导入模块时：导入的模块会运行所导入的模块
        __main__变量:当导入模块时模块内置的变量__name__ 就会变成__main__ 
        __all__变量：当导入模块时使用import * __all__ 变量修饰谁谁就能导进来
"""
import MyModule
MyModule.my_function(1, 3)
from MyModule import *
my_function(1,3)
# my_function1(1,9) # 该功能没有被__all__修饰不能被导入   将注释解除则会将没有被__all__修饰的BUG暴露出来

#从python入门包中导入模块和包在导入MyModule模块
from python入门.模块和包.MyModule import *
my_function(1,6)
