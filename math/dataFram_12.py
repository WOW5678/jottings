# -*- coding: utf-8 -*-
"""
 @Time    : 2018/11/2 0002 上午 9:27
 @Author  : Shanshan Wang
 @Version : Python3.5
 @Function: pandas的数据结构dataFrame详解
"""
import pandas as pd
import numpy as np

#DataFrame的创建：1、通过二维数组
# DataFrame的创建： 2、字典
# 字典中的value只能是一维数组或者单个的简单数据类型，如果是数组长度必须一致
# 索引对象，不管是Series还是DataFrame对象，都有索引对象
# 他们的自动对齐功能也是通过索引实现的
# DataFrame可以直接通过列索引获取指定列的数据

# 如果需要获取指定行的数据的话，需要通过ix方法来获取对应行索引的行数据
# DataFrame可以切片操作
# 修改值  新增列 新增行  numpy是不能加新行新列的 但是DataFrame可以
# 修改某个具体对象的值，即可以先列后行 也可以先行后列 最好是先列后行可以自动改变对象的数据类型

arr=[['dfy',100],['zs',90],['ls',99]]
#     0    1
#0  dfy  100
#1   zs   90
#2   ls   99
df1=pd.DataFrame(arr)
print(df1)
#RangeIndex(start=0, stop=3, step=1) #指的是行索引
print(df1.index)
#RangeIndex(start=0, stop=2, step=1) 列索引
print(df1.columns)
#0    object
#1     int64
#dtype: object
print(df1.dtypes)
df1=pd.DataFrame(arr,index=['第一行','第二行','第三行'],columns=['name','分数'])
print('df1:',df1)
dict1={
    '语文': [90, 88, 67],
    '数学': [99, 78, 89],
    '外语': [98, 102, 125],
    '物理': 88
}
df2=pd.DataFrame(dict1)
#    外语  数学  物理  语文
# 0   98  99  88  90
# 1  102  78  88  88
# 2  125  89  88  67
print(df2)
df2.index=['dfy','zs','ls']
#       外语  数学  物理  语文
# dfy   98  99  88  90
# zs   102  78  88  88
# ls   125  89  88  67
print(df2)
#一下这两种方式都会报错
#KeyError: 'dfy'
# print(df2['dfy']['外语'])
#90
print(df2['语文']['dfy'])
#90
print(df2.ix['dfy']['语文'])
#      外语  数学
# dfy   98  99
# zs   102  78
print(df2.ix[:2,:2])
print(df2.dtypes)
#将外语这一列都设置为nan
df2['外语']=np.nan
print(df2)
df2['外语']=[0,0,0]
df2.ix['dfy']=[100,100,100,100]
#       外语   数学   物理   语文
# dfy  100  100  100  100
# zs     0   78   88   88
# ls     0   89   88   67
print(df2)
#增加一列 值全为np.nan
df2['XXX']=np.nan
#增加一行，值全为np.nan
df2.ix['YYY']=np.nan
print(df2)
# 外语     float64
# 数学     float64
# 物理     float64
# 语文     float64
# XXX    float64
# dtype: object
#输入每一列的数据类型
print(df2.dtypes)

