# -*- coding:utf-8 -*-
'''
Create time: 2018/10/31 9:28
@Author: 大丫头
'''
import numpy as np

a=np.array([2900,3,4])
print(a,a.dtype) #int32

b=a.astype(np.complex128)
#complex128 int32
print(b.dtype,a.dtype)

c=np.array(['python','java','rn'],dtype='U14')
#['python' 'java' 'rn'] <U14
print(c,c.dtype)

d=np.random.random((2,3,5))
# (2, 3, 5)
print(d.shape)
d.shape=(3,10)
# (3,10)
print(d,d.shape)

e=d.reshape((3,2,5))
#(3, 2, 5) (3, 10)
print(e.shape,d.shape)

###############################################
#数组的运算  数组之间 数组与标量之间
a1=[2,3,5]
b1=['222','dty',99]
#[2, 3, 5, '222', 'dty', 99]
#两个列表相加 就是列表的添加
print(a1+b1)

a=np.array([2,3,5])
b=np.array(['4','5','2'],dtype=int)
#[ 8 15 10]
print(a*b)
#[16 25  4]
print(b**2)

c=np.array([[1,2,3],[4,5,6]])
d=np.array([[2,3,4],[4,5,8]])
d.shape=(3,2)
print(c.shape)
print(d.shape)
#矩阵乘法
#[[25 35]
# [58 80]]
print(np.dot(c,d))
#[[25 35]
#[58 80]]
print(c.dot(d))
