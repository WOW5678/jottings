# -*- coding:utf-8 -*-
'''
Create time: 2018/10/31 9:09
@Author: 大丫头
function: ndarray数组的使用
'''
''''
# NumPy模块是Python的一种开源的数值计算扩展，是一个用python实现的科学计算包，主要包括：
# 1、一个具有矢量算术运算和复杂广播能力的快速且节省空间的多维数组，称为ndarray
# ndarray  N-dimensional array object
# 2、用于对整组数据进行快速运算的标准数学函数 ufunc
# 3、实用的线性代数、傅里叶变换和随机数生成函数
# 4、Numpy和稀疏矩阵的运算包Scipy配合使用更加方便


# NumPy的核心数据结构：ndarray   N维数组
# 元素的数据类型由dtype(data-type)对象来指定，每个ndarray只有一种dtype类型
# ndarray的大小固定 创建好后数组大小是不会发生改变的

# 创建ndarray数组对象的方法：
# 1、array函数：接收一个普通的python序列(字符串 元祖 列表)，并将其转换为ndarray
# 2、zeros函数：创建指定长度或形状的全0数组
# 3、ones函数：创建指定长度或形状的全1数组
# 4、empty函数：创建一个没有任何具体值的数组（准确的说是创建一些未初始化的ndarray多维数组）
# 5、arange()函数：python的range()
# 6、linspace函数 等差数列  endpoint是否包含终值 默认包含终值
# 7、logspace函数 等比数列
# 8、使用随机数填充数组 numpy.random中的random()函数

# ndarray属性
# dtype ：数组元素数据类型的对象
# shape:一个数组的各个维度大小的元祖 即数组的形状
# size：数组总个数，即shape中各个数的相乘
# ndim：一个数组的维度数量

'''
import numpy as np
print(np.__version__) #1.14.1

a=np.array([[2,3,4],[5,6,7]],dtype=np.float)
print(a)
print(a.dtype) #float64

b=np.zeros((3,4,2),dtype=np.int)
print(b)

c=np.ones((2,3))
print(c)

d=np.empty((3,3))
print(d)
#d的值
#[[ 1.47770328e-311  1.47784123e-311  1.47770328e-311]
#[ 1.47784125e-311  1.47770328e-311  1.47784123e-311]
#[ 1.47770328e-311  1.47784125e-311 -1.30091598e-258]]

print(np.arange(1,10,2)) #[1 3 5 7 9]
print(np.array(range(1,10,2))) #[1 3 5 7 9]

#[1.   3.25 5.5  7.75]
e=np.linspace(1,10,4,endpoint=False)
print(e)
#[ 1.          2.28571429  3.57142857  4.85714286  6.14285714  7.42857143
# 8.71428571 10.        ] linspace默认是包括endpoint的
print(np.linspace(1,10,8))

f=np.logspace(1,8,4,endpoint=False)
#[1.00000000e+01 5.62341325e+02 3.16227766e+04 1.77827941e+06]
print(f)
print(np.logspace(1,8,5))

#[0,1)
g=np.random.random((2,3,4))
print(g)
#属性： float64 (2, 3, 4) 24 3
print('属性：',g.dtype,g.shape,g.size,g.ndim)

# randint指定上下界，产生的是随机的整数
print(np.random.randint(10,20,(2,3,4)))

#[[0.44678193 0.06587503]
#[0.06471601 0.47288475]
# [0.27234047 0.8338035 ]]
print(np.random.rand(3,2))

#[[ 1.07092431  0.57467159]
# [ 0.2411354  -0.49064896]
# [-0.69840483 -1.11399248]]
#生成的数据符合正太分布
print(np.random.randn(3,2))