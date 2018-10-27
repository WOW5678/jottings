# -*- coding: utf-8 -*-
"""
 @Time    : 2018/10/27 0027 上午 11:29
 @Author  : Shanshan Wang
 @Version : Python3.5
 @Function: 迭代器的使用
"""
# 可迭代的对象：如果一个对象可以用for in 的方式遍历其内容 就是一个可迭代的对象 list tuple 字典
# 迭代器：遍历可迭代对象内容的方式
# 常见的迭代器：组合 排列 笛卡尔积  串联迭代器可以被next()函数调用的并不断返回下一个值得对象叫做迭代器：iterator
#凡是可以用作与next()函数的对象都是iterator

import itertools

# 排列 组合 笛卡尔积 串联迭代器
x=range(5)
y=list('abc')
#排列
com1=itertools.combinations(x,3)
#组合
com2=itertools.permutations(x,3)
#笛卡尔积
com3=itertools.product(x,y)
#串联迭代器
com4=itertools.chain(com1,com2,com3)
for i in com4:
    print(i)

#通过iter（）将一个可迭代对象编程迭代器
list01=[1,2,3,4]
##list01不是迭代器所以无法调用  next
#print(next(list01))
#通过iter()将一个可迭代对象编程迭代器
a=iter(list01)
print(a)
print(next(a))
print(next(a))
print(next(a))

#yield 生成器
#生成一个迭代器
#        -》yield的作用是把一个函数变成一个generator
#        -》使用生成器可以达到延迟操作的效果，所谓延迟操作就是指在需要的时候
#        产生结果而不是立即产生就结果，节省资源消耗，和声明一个序列不同的是
#        生成器，在不使用的时候几乎是不占内存的。

def getNum(n):
    i=0
    while i<n:
        yield i
        i+=1
#调用函数
#<generator object getNum at 0x000000000070B2B0>
print(getNum(5))

#把生成器赋值给一个变量a
a=getNum(5)
#使用生成器 通过next()方法
print(next(a)) #0
print(next(a)) #1
print(next(a)) #2

print('*'*8)
def gan():
    i=0
    while i<5:
        temp=yield i
        print('temp:',temp)
        i+=1
a=gan()
print(next(a)) #0
print(next(a)) #1
print(a.send('我是a')) #可以将值发送到上一次yield的地方 也就是发送给了temp


print(next(a)) #2