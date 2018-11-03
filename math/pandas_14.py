# -*- coding: utf-8 -*-
"""
 @Time    : 2018/11/3 0003 上午 9:44
 @Author  : Shanshan Wang
 @Version : Python3.5
 @Function: pandas的基本功能与常用的数学统计方法
"""
import pandas as pd
import numpy  as np

# pandas的基本功能
# 1、数据文件读取 文本数据读取
# 2、索引、选取和数据过滤
# 3、算术运算和数据对齐
# 4、函数的应用和映射
# 5、重置索引

# 通过pandas提供的read_XXX相关的函数可以读取文件中的数据，并形成DataFrame
# 常用的数据读取方法为read_csv 主要可以读取文本类型的数据
# help(pd.read_csv)
# help(pd.read_excel)
# csv的数据的表格形式的 并且是最简单的表格 直接看看图片

# pandas：数据过滤获取
# 通过DataFrame的相关方式可以获取对应的列或者数据形成一个新的DataFrame，方便后续进行统计计算
# pandas中缺省值NaN处理方法：1 isnull  2 notnull  3 dropna  4 fillna
# df.dropna()  默认丢弃只要包含nan数据的行 axis=1则是丢弃列 how='any'默认 如果设置how='all'则表示全部为nan才丢弃

# df.fillna()  填充缺失值

# pandas常用的数学统计方法
# count 计算非NA值的数量
# describe 针对Series或DataFrame列计算统计
# min/max/sum 计算最小值 最大值  总和
# argmin argmax 计算能够获取到最小值和最大值的索引位置（整数）
# idxmin idxmax 计算能够获取到最小值和最大值的索引值
# quantile   计算样本的分位数（0到1）
# mean   值的平均数
# median  值的中位数
# mad 根据平均值计算平均绝对距离差
# var 样本数值的方差
# std 样本值的标准差
# cumsum 样本值的累计和
# cummin  cummax  样本的累计最小值 最大值
# cumprod  样本值的累计积
# pct_change  计算百分数变化
# print(df2.describe())
# print(df2.quantile())


# 相关系数   具体看图片
# print(df2.corr())
# 协方差
# print(df2.cov())

# pandas:唯一值、值频率计算以及成员资格
# unique方法用于获取Series或DataFrame某列中的唯一值数组（去重数据后的数组)
# value_counts方法用于计算一个Series或DataFrame某列中各值的出现频率
# isin方法用于判断矢量化集合的成员资格，是否在里面，可用于选取Series中或DataFrame列中数据的子集
#pd.read_csv()
#pd.read_excel()
#pd.read_json()

#dataFrame数据的切片
#pandas当中处理NaN缺省值的方法：1.isnull 2.notnull
#3.dropna()4.fillna()

dict1={
    '语文': [90, 88, 67],
    '数学': [99, 78, 89],
    '外语': [98, 102, 125],
    '物理': 88
}
df2=pd.DataFrame(dict1)
df2['数学'][1]=np.nan
#     外语    数学  物理  语文
# 0   98  99.0  88  90
# 1  102   NaN  88  88
# 2  125  89.0  88  67
print(df2)
#删除含有空值得列
#     外语  物理  语文
# 0   98  88  90
# 1  102  88  88
# 2  125  88  67
print(df2.dropna(axis=1))

df3=pd.DataFrame(np.random.random((7,3)))
df3.ix[:4,1]=np.nan
df3.ix[:2,2]=np.nan
# 0  0.265456       NaN       NaN
# 1  0.821593       NaN       NaN
# 2  0.926739       NaN       NaN
# 3  0.723732       NaN  0.243985
# 4  0.167271       NaN  0.289523
# 5  0.201474  0.515232  0.053081
# 6  0.501449  0.705777  0.485086
print(df3)
print(df3.fillna(1))
#           0         1         2
# 0  0.193041  0.500000 -1.000000
# 1  0.436411  0.500000 -1.000000
# 2  0.327941  0.500000 -1.000000
# 3  0.222833  0.500000  0.103680
# 4  0.476285  0.500000  0.561985
# 5  0.338230  0.563929  0.920338
# 6  0.289510  0.528569  0.820140
print(df3.fillna({1:0.5,2:-1}))

print(df2.describe())
print(df2.median())
#方差
print(df2.var())
#标准差
print(df2.std())
#相关系数
print(df2.corr())
#协方差
print(df2.cov())


s1=pd.Series(['a', 'b', 'c', 'b', 'a'])
#['a' 'b' 'c']
print(s1.unique())
#2
print(s1.value_counts()['a'])
# 0     True
# 1     True
# 2    False
# 3     True
# 4     True
# dtype: bool
print(s1.isin(['a','b']))
print('------------------------------')
df4=pd.DataFrame(np.random.randint(10,16,(3,3)),columns=['dfy', 'zs', 'ls'])
#    dfy  zs  ls
# 0   15  11  13
# 1   12  10  11
# 2   15  12  12
print(df4)
#[15 11 13]
print(df4.ix[0].unique())
#[15 12]
print(df4['dfy'].unique())
# 15    2
# 12    1
print(df4['dfy'].value_counts())
# 15    1
# 13    1
# 11    1
print(df4.ix[0].value_counts())
# 0    False
# 1    False
# 2    False
print(df4['dfy'].isin([11]))


# 读写csv文件
df1 = pd.DataFrame(np.arange(24).reshape((8, 3)))
df1.columns = ['dfy', 'san', 'lisi']
print(df1)
df1.to_csv('df1.csv', index=False)

df2 = pd.read_csv('df1.csv')
print(df2)