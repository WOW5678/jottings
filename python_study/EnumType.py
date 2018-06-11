# -*- coding:utf-8 -*-
#功能：理解python的枚举类型的使用
from enum import Enum
Month=Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#枚举Month的成员
#value的属性 是自动赋值给成员的Int变量，默认是从1开始计数
for name,member in Month.__members__.items():
    print(name,'==>',member,',',member.value)

#如果需要精确地控制枚举类型，可以从Enum派生出定义类
from enum import unique

#@nique装饰器可以帮助我们检测保证没有重复值
@unique
class Weekday(Enum):
    Sun=0
    Mon=1
    Tue=2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

#对枚举类型的访问
print(Weekday.Sun)   #Weekday.Sun
print(Weekday.Sun.value) #0
print(Weekday(0)) #Weekday.Sun,注意这是根据value查找枚举类型的名称，必须用（）而不能用[]
print(Weekday['Sun']) #Weekday.Sun

#也可以遍历输出
for name,member in Weekday.__members__.items():
    print(name,'=>',member,'=>',member.value)