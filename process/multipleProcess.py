# -*- coding:utf-8 -*-
#功能：理解python多进程的实现

import os

print('Process (%s) start...'%os.getpid())
# #fork()函数仅仅在linux，unix,mac上工作
# pid=os.fork()
# if pid==0:
#     print('I am a child process (%s) and my parent is %s' %(os.getpid(),os.getppid()))
# else:
#     print('I (%s) just created a child process (%s)' %(os.getpid(),pid))

print('################################################')
#python的multiprocessing模块就是跨平台版本的多进程模块

from multiprocessing import  Process
import os

#子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)' %(name,os.getpid()))

if __name__ == '__main__':
    print('Parent process %s' %os.getpid())
    #创建子进程P
    p=Process(target=run_proc,args=('test',))
    print('Child process will start.')
    p.start() #开启进程
    #p.join()函数表示要等待p进程运行完毕之后再往下执行  通常用于进程间的同步
    p.join()
    print('Child process end.')