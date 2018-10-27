# -*- coding: utf-8 -*-
"""
 @Time    : 2018/10/27 0027 上午 11:11
 @Author  : Shanshan Wang
 @Version : Python3.5
 @Function: 装饰器的使用
"""
# 装饰器本质上是一个Python函数 它可以让其他函数在不需要做任何代码变动的前提下增加额外功能
# 装饰器的返回值也是一个函数对象
# 它经常用于有切面需求的场景 比如：插入日志 性能测试  权限判断等
# 有了装饰器 我们就可以抽离出大量与函数功能本身无关的雷同代码并继续重用
# 总之 装饰器的作用就是为已经存在的对象添加额外的功能

def addTips(fun):
    def wrap(*args,**kwargs):
        print('这是操作之前')
        result=fun(*args,**kwargs)
        print('操作结束了')
        return result
    return wrap

@addTips
def add(x,y):
    return x+y
print(add(2,3))

####装饰器中也可以传入参数
def addTips2(i):
    def wrap1(fun):
        def wrap(*args,**kwargs):
            print('这是操作之前')
            result=0
            if i>10:
                result=fun(*args,**kwargs)
            else:
                print('对不起，没有执行fun的权限')
            print('操作结束了')
            return result
        return wrap
    return wrap1

@addTips2(10)
def add(x,y):
    return x+y

#这是操作之前
#对不起，没有执行fun的权限
#操作结束了
#0
print(add(2,3))




