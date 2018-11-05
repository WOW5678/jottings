# -*- coding: utf-8 -*-
"""
 @Time    : 2018/11/5 0005 上午 8:43
 @Author  : Shanshan Wang
 @Version : Python3.5
 @Function: pandas的层次缩影和取值的新方法
"""
import pandas as pd


# pandas:层次索引
# 在某一个方向拥有多个（两个及两个以上）索引级别
# 通过层次化索引，pandas能够以较低维度形式处理高纬度的数据
# 通过层次化索引，可以按照层次统计数据
# 层次索引包括Series层次索引和DataFrame层次索引

# 数据透视表 用到层次索引
# ix是比较老的方法 新方式是使用iloc  loc
# iloc 对下标值进行操作 Series与DataFrame都可以操作
# loc 对索引值进行操作 Series与DataFrame都可以操作

# 将数据进行归一 合并  数据有重复  类似合并单元格
# 设置多个行索引 层次化索引
# 根据层次化索引取值 此时可以理解为三维的

# pandas：按照层次索引进行统计数据
# print(df2.sum(level='year'))
# print(df2.mean(level='fruit'))
# 下面的level写了2个相当于是 并且的关系
# print(df2.min(level=['year', 'fruit']))

print(pd.__version__) #0.23.3
s1=pd.Series(data=[99, 87, 76, 67, 99],
             index=[['2017', '2017', '2018', '2018', '2018'], ['dfy', 'lisi', 'dfy', 'lisi', 'zs']])
#数据透视表 用到层次索引
# 2017  dfy     99
#       lisi    87
# 2018  dfy     76
#       lisi    67
#       zs      99
# dtype: int64
print(s1)
#87
print(s1.iloc[1])
#87
print(s1.loc['2017','lisi'])

df1=pd.DataFrame({
'year': [2016, 2016, 2017, 2017, 2018],
    'fruit': ['apple', 'banana', 'apple', 'banana', 'apple'],
    'production': [2345, 3242, 5667, 2576, 2134],
    'profits': [23.22, 76.89, 90.99, 78.22, 98.76],
})
#     fruit  production  profits  year
# 0   apple        2345    23.22  2016
# 1  banana        3242    76.89  2016
# 2   apple        5667    90.99  2017
# 3  banana        2576    78.22  2017
# 4   apple        2134    98.76  2018
print(df1)
print('.....................')
df2=df1.set_index(['year','fruit'])
#              production  profits
# year fruit
# 2016 apple         2345    23.22
#      banana        3242    76.89
# 2017 apple         5667    90.99
#      banana        2576    78.22
# 2018 apple         2134    98.76
print(df2)
#df1.index=['a', 'b', 'a', 'c', 'd']
# MultiIndex(levels=[[2016, 2017, 2018], ['apple', 'banana']],
#            labels=[[0, 0, 1, 1, 2], [0, 1, 0, 1, 0]],
#            names=['year', 'fruit'])
print(df2.index)
print('----------------')
#       production  profits
# year
# 2016        5587   100.11
# 2017        8243   169.21
# 2018        2134    98.76
print(df2.sum(level='year'))
#         production  profits
# fruit
# apple         3382   70.990
# banana        2909   77.555
print(df2.mean(level='fruit'))
#              production  profits
# year fruit
# 2016 apple         2345    23.22
#      banana        3242    76.89
# 2017 apple         5667    90.99
#      banana        2576    78.22
# 2018 apple         2134    98.76
print(df2.sum(level=['year','fruit']))

#取值的新方法
print(df1['profits'][2])
print(df1.ix[2]['profits'])

print('------------------')
#iloc对下标值进行操作
print(df1.iloc[2,2]) #90.99
#loc对索引值进行操作
print(df1.loc[2,'profits']) #90.99
