# -*- coding: utf-8 -*-
"""
 @Time    : 2018/11/5 0005 上午 9:05
 @Author  : Shanshan Wang
 @Version : Python3.5
 @Function: matplotlib画图小试：直线、条状图、饼图
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

# 带e的科学计数法
# 4.773e-101是科学记数的写法，就是4.773X10^-101的意思，即4.773乘以10的-101次方
# f表示float 1表示小数点后一位小数

#labeldistance，文本的位置离远点有多远，1.1指1.1倍半径的位置
#autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
#shadow，饼是否有阴影
#startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
#pctdistance，百分比的text离圆心的距离

# 设置x，y轴刻度一致，这样饼图才能是圆的
#plt.axis('equal')

# 显示图例
#plt.legend()

#生成数据
dataout=np.arange(24).reshape((4,6))
print(dataout)
# 保存数据
np.savetxt('data.txt',dataout,fmt='%.2f')

#读取数据
data=np.loadtxt('data.txt')
# [[ 0.  1.  2.  3.  4.  5.]
#  [ 6.  7.  8.  9. 10. 11.]
#  [12. 13. 14. 15. 16. 17.]
#  [18. 19. 20. 21. 22. 23.]] float64
print(data,data.dtype)

y=np.random.randint(1,11,5)
#[ 4  1  6 10  3]
print(y)
x=np.arange(len(y))
#[0 1 2 3 4]
print(x)

print('=====================')
plt.figure(figsize=(6,8))
#[6.4, 4.8]
print(rcParams['figure.figsize'])
#plt.plot(x,y,color='r') #折线图
#plt.bar(x,y,color='g') #柱状图
plt.pie(y,explode=[0,0.2,0,0,0]) #饼状图
plt.show()

print('==============================')
plt.figure(figsize=(6,8))
labels=['part one', 'part two', 'part three']
data=[60,30,10]
colors=['red','yellow','blue']
# 每一部分的突出间隔
explode=[0,0.05,0]
plt.pie(data,explode=explode,labels=labels,colors=colors,
        labeldistance=0.7,startangle=90,autopct='%.2f%%',pctdistance=0.5,shadow=False)
plt.axis('equal')
plt.legend()
plt.show()
