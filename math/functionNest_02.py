# -*- coding: utf-8 -*-
"""
 @Time    : 2018/10/27 0027 上午 10:59
 @Author  : Shanshan Wang
 @Version : Python3.5
 @Function: 函数的嵌套 以及递归的使用
"""
def fun1():
    def fun2():
        print('Hello world')
    return fun2
#执行时
#fun1()表示的就是fun2这个函数对象，再加上（）表示执行
fun1()()

# 函数嵌套的三层用法
def fun1():
    print('我是fun1的函数体语句')
    def fun2():
        print('我是fun2的函数体语句')

        def fun3():
            print('Hello world')
        return fun3
    return fun2
#a表示的是func2这个对象
a=fun1()
# b表示的是func3这个对象
b=a()
#执行func3函数，打印hello world
b()

#fun1中返回 fun2的方法名
# fun1()就是调用函数 返回fun2的函数入口给变量a
# a()就是调用函数fun2 返回fun3的函数入口给变量b
# 最后调用b()

######递归函数
def main(n):
    print('进入第%d层梦境'%n)
    if n==3:
        print('到达潜意识区，开始醒来')
    else:
        main(n+1)
    print('从第%d层梦境醒来'%n)
main(1)

####用递归函数，计算阶乘问题
def jiecheng(n):
    if n==1:
        return 1
    else:
        return n*jiecheng(n-1)
print(jiecheng(5))