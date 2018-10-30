# -*- coding: utf-8 -*-
"""
 @Time    : 2008/3/1 0001 上午 9:28
 @Author  : Shanshan Wang
 @Version : Python3.5
 @Function: time模块的使用方法
"""
from datetime import datetime
import time

print(datetime.now())
print(time.time())
# 时间戳 1970 1 1 0 0到现在为止的秒数
# time_tuple 时间元祖  struct_time
print(time.localtime())
#2008/03/01 09:33:20
print(time.strftime('%Y/%m/%d %H:%M:%S',time.localtime()))

time_tuple=time.strptime('2017-12-12 14:23:56','%Y-%m-%d %H:%M:%S')
#1513059836.0
print(time.mktime(time_tuple))

################################################
'''
sleep 推迟调用线程的运行，secs指秒数
'''
for i in range(1,3):
    print('让子弹飞一会')
    time.sleep(2)
    print('子弹在飞')
    time.sleep(2)
    print('子弹到了')

########################################
now=time.time()
#减去三天的秒数
three_ago=now-60*60*24*3
#将时间戳转换成时间元组
time_tuple=time.localtime(three_ago)
# 将时间戳转换成时间字符串
#2008-02-27 09:38:40
print(time.strftime('%Y-%m-%d %H:%M:%S',time_tuple))
