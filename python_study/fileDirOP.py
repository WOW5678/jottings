# -*- coding:utf-8 -*-
#功能：使用Python操作文件和目录
import os
print(os.name) #操作系统的类型，如果是nt就是windowns系统 如果是posix就是Linux,unix或者mac os x

#查看操作系统中的环境变量
print(os.environ)
print('#########################')
#获取耨个环境变量的值
print(os.environ.get('PATH'))
print('##########################')
#操作文件和目录

#查看当前目录的绝对路径
print(os.path.abspath('.'))