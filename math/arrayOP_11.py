# -*- coding: utf-8 -*-
"""
 @Time    : 2018/11/2 0002 上午 8:55
 @Author  : Shanshan Wang
 @Version : Python3.5
 @Function: 对数据的操作：一元函数、二元函数、聚合函数、三元函数
"""
import numpy as np
# ndarray的一元函数
# abs fabs 计算整数、浮点数、复数的绝对值，对于非复数，fabs更快
# sqrt 计算各个元素的平方根 相当于arr**0.5 要求arr的每个元素必须非负数
# square 计算各个元素的平方  相当于arr**2
# exp 计算各个元素的指数e的x次方
# log log10 log2 log1p 分别计算自然对数、底数为10、底数为2 以及log(1+x),要求arr中的每个元素必须为正
# sign 计算各个元素的正负号 1为正数 -1为负数 0
# ceil 计算各个元素的ceilling值 即大于等于该值的最小整数
# floor 计算各个元素的floor值，即小于等于该值的最大整数
# rint 各个元素的四舍五入到最接近的整数，保留dtype的类型
# modf 将数组中元素的小数位和整数位以两部分独立数组的形式返回
# isnan NaN(不是一个数字) 布尔类型数组
# isfinite isinf 有穷的(非inf 非NaN)np.NaN  np.inf 无穷的  布尔类型数组
# cos cosh sin sinh tan tanh  普通以及双曲型三角函数
# arccos arccosh arcsin arcsinh arctan arctanh   反三角函数

# ndarray的二元函数
# mod 元素级的取模%
# dot 点积 矩阵积
# greater greater_equal less less_equal equal not_equal 元素级的比较运算，最终返回一个布尔型数组
# logical_and logical_or logical_xor
# power 对数组中的每个元素执行给定次数的指数值

# ndarray的聚合函数
# 聚合函数的对一组值进行操作，返回一个单一值作为结果的函数
# 常见的聚合函数有：平均值、最大值、最小值、方差等等
# arr.min()  arr.max()  arr.mean()  arr.std() arr.sum()
# 方差公式：np.sqrt(np.power(arr-arr.mean(),2).sum()/arr.size)
# 二维数组的情况下，axis=0表示对同列的数据进行聚合
# axis=1 表示对同行的数据进行聚合
# arr.mean(axis=0)

arr=np.array([-2,2,4,-3,100])
#[  2.   2.   4.   3. 100.]
print(np.fabs(arr))
print(arr)
arr1=np.fabs(arr)
#[ 1.41421356  1.41421356  2.          1.73205081 10.        ]
print(np.sqrt(arr1))
#[ 1.41421356  1.41421356  2.          1.73205081 10.        ]
print(arr1**0.5)
#[4.0e+00 4.0e+00 1.6e+01 9.0e+00 1.0e+04]
print(np.square(arr1))
#[4.0e+00 4.0e+00 1.6e+01 9.0e+00 1.0e+04]
print(arr1**2)
print(np.exp(arr1))
#[-1  1  1 -1  1]
print(np.sign(arr))

arr2=np.random.random((2,3))
#[[0.02282454 0.49503035 0.66878514]
# [0.66831873 0.79304352 0.94635194]]
print(arr2)
#(array([[0.02282454, 0.49503035, 0.66878514],
#       [0.66831873, 0.79304352, 0.94635194]]), array([[0., 0., 0.],
#       [0., 0., 0.]]))
## modf 将数组中元素的小数位和整数位以两部分独立数组的形式返回
print(np.modf(arr2))
#nan
print(np.nan)
#inf
print(np.inf)
#[1. 1. 1. 1. 1.]
print(np.sign(arr1))
#[ 4.00e+000  4.00e+000  2.56e+002 -2.70e+001  1.00e+200]
## power 对数组中的每个元素执行给定次数的指数值
#对array数组中每个元素执行arr1对应元素的指数值
print(np.power(arr,arr1))

#a=np.random.randint(2,100,(3,4,5))
a=np.array([[2,3,5,6],[3,4,9,1]])
print(a)
#9 1 33 4.125 2.368411915187052
print(a.max(),a.min(),a.sum(),a.mean(),a.std())
#1.4584077361972543
print(np.sqrt(np.power(a.mean(),2).sum()/a.size))
#[6 9]
print(a.max(axis=1))

#三元函数 np.where==x if condition else y
a=np.array([[3,5],[2,8]])
b=np.array([[1,6],[4,3]])
print(a)
print(b)
c=a>b
#[[ True False]
# [False  True]]
print(c)
#[3 8]
print(a[c])
condition=a>b
#[[3 6]
# [4 8]]
#相当于对应位置选择最大的值
print(np.where(condition,a,b))

print('...........')
print(np.array([[3,6],[4,8]]))
#[[ 2.  3. nan]
# [ 4.  5.  8.]
# [inf nan 33.]]
c=np.array([[2,3,np.nan],[4,5,8],[np.inf,np.nan,33]])
print(c)
condition=np.isnan(c)|np.isinf(c)
#[[ 2.  3.  0.]
# [ 4.  5.  8.]
# [ 0.  0. 33.]]
print(np.where(condition,0,c))

#数据去重
a=np.random.randint(4,9,(4,4))
#[[4 6 7 7]
# [4 4 6 8]
# [8 4 8 7]
# [6 6 4 4]]
print(a)
#[4 6 7 8]
print(np.unique(a))

#
# 引入三元：比如有a b两个数组 我需要将a b对应元素中较大的那个返回出来
# np.where函数是三元表达式x if condition else y的矢量化版本
# 例子：将数组中所有异常数字替换为0 比如将NaN替换为0
# condition = np.isnan(arr) | np.isinf(arr)
# np.where(condition, 0, arr)

# 应用场景：数据去重
# np.unique函数的主要作用是将数组中的元素进行去重操作（也就是只保存不重复的数据）默认会进行排序
# aa = np.random.randint(4, 8, (4, 4))
# print(aa)
# print(np.unique(aa))