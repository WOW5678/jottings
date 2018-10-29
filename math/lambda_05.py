# -*- coding: utf-8 -*-
"""
 @Time    : 2018/10/29 0029 上午 9:06
 @Author  : Shanshan Wang
 @Version : Python3.5
 @Function: python中的匿名函数与lambda表达式
"""


#[0, 1, 4, 9, 16, 25, 36, 49]
print([i**2 for i in range(8)])
#[0, 2, 4, 6]
print([i for i in range(8) if i%2==0])
a=[[1,2,3],[4,5,6],[7,8,9]]
#[1, 2, 3, 4, 5, 6, 7, 8, 9]
print([j for i in a for j in i])

####匿名函数
from functools import reduce

lambda1=lambda x:x**2
lambda2=lambda x,y:x+y
lambda3=lambda x:x%2==0
#[0, 1, 4, 9, 16, 25, 36, 49]
print(list(map(lambda1,range(8))))
#28
print(reduce(lambda2,range(8)))
#[0, 2, 4, 6]
print(list(filter(lambda3,range(8))))

# 练习：计算5!+4!+3!+2!+1!的和
# # 要求：使用我们刚刚讲的lambda和map reduce filter

la1=lambda x,y:x*y
##120
print(reduce(la1,range(1,6)))
la2=lambda n:reduce(la1,range(1,n+1))
#[1, 2, 6, 24, 120]
print(list(map(la2,range(1,6))))
la3 = lambda a, b: a+b
#153
print(reduce(la3,list(map(la2,range(1,6)))))

'''
矢量化的三元运算符
if 条件：
    代码块
else：
    代码块
条件成立的内容 if 条件 else 条件不成立的内容
'''
s=lambda x,y:x if x>2 else y
print(s(1,4)) #4
print(s(3,5)) #3

# 一种不带参数的lambda表达式
lambda1=lambda :'hello'
print(lambda1()) #hello

#一般情况下：对象的方法与内置函数的区别
#对象没有的方法，并不代表内置函数不能运行
list1=[21,24,42,16]
#对象的方法，比如列表对象的sort()的方法没有返回值，直接修改对象本身
print(list1.sort()) #None
print(list1) #[16, 21, 24, 42]
# 内置函数的方法 有返回值 接收一个对象 返回一个新对象
list1=sorted(list1)
print(list1) #[16, 21, 24, 42]

# 字典排序
dict1={'a':3,'c':1,'b':2}
#字典对象.items()可以转换成一个元组列表
list1=sorted(dict1.items()) #默认情况下是根据key进行排序
#{'c': 1, 'a': 3, 'b': 2}
print({k:v for k,v in dict1.items()})
#如果希望通过字典的值进行排序，需要借助lambda表达式
list2=sorted(dict1.items(),key=lambda x:x[1])
#{'a': 3, 'c': 1, 'b': 2}
print({k:v for k,v in list1})
# 字典排序的另外一种形式：字典列表
list2 = [
    {'name': 'dfy', 'age': 19},
    {'name': 'zhangsan', 'age': 20},
    {'name': 'lisi', 'age': 18}
]

# list2 = sorted(list2, key=lambda x: x['name'])
list2 = sorted(list2, key=lambda x: x['age'])
#[{'age': 18, 'name': 'lisi'}, {'age': 19, 'name': 'dfy'}, {'age': 20, 'name': 'zhangsan'}]
print(list2)