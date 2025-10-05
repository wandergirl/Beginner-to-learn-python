"""
        这个是为"python模块和包.py"创建的模块/文件
"""
__all__ = ['my_function']
def my_function(a,b):
     print(a+b)
my_function(1,2)
if __name__ == __import__:  # test调用会使__name_变量变成__main__但是from导入的时候不会使__name__变成__ main__
    my_function(1,2)
my_function(1,2)
def my_function1(a,b):
    print(a+b)