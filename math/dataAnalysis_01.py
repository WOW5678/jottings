# -*- coding: utf-8 -*-
"""
 @Time    : 2018/10/27 0027 上午 10:47
 @Author  : Shanshan Wang
 @Version : Python3.5
 @Function: numpy,pandas,scipy的初尝试
"""
import numpy as np
#[0 1 2 3 4 5 6 7 8 9]
print(np.arange(10))

for i in range(10):
    print(i)

a=np.arange(10)
#[ 0  1  4  9 16 25 36 49 64 81]
print(a**2)

###
###scipy的使用
###
from scipy import linalg
a=np.array([[1,2],[30,4]])
print(a)
#二阶方阵行列式
#注意：推荐用scipy.linalg代替numpy.linalg
#-56.0
print(linalg.det(a))

###
###Pandas的使用,数据结构：Series和DataFrame
###
import pandas as pd

s=pd.Series([2,4,5,np.nan,8,9])
print(s)

#DatetimeIndex(['2017-12-01', '2017-12-02', '2017-12-03', '2017-12-04',
#               '2017-12-05', '2017-12-06', '2017-12-07'],
#              dtype='datetime64[ns]', freq='D')
dates=pd.date_range('20171201',periods=7)
print(dates)

df=pd.DataFrame(np.random.randn(7,4),index=dates,columns=list('ABCD'))
print(df)
#转置
print(df.T)
# 按B这一列进行排序，其他列受影响
print(df.sort_values(by='B'))
print(df.head(2))
print(df.tail(1))
print(df.describe())