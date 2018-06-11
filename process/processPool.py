# -*- coding:utf-8 -*-
#功能：如果要启用大量的子进程，可以用进程池的方式批量创建子进程
from multiprocessing import  Pool
import os,time,random

def long_time_task(name):
    print('Run task %s (%s)...'%(name,os.getpid()))
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print('Task %s run %0.2f seconds.' %(name,(end-start)))

if __name__ == '__main__':
    print('Parent process %s' %os.getpid())
    #创建包含4个子进程的进程池
    p=Pool(4) #最多同时执行4个进程
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

    print('####################################')
    #子进程
    #演示在python 代码中运行命令'nslookup www.python.org'
    import subprocess
    print('$ nslookup www.python.org')
    r=subprocess.call(['nslookup','www.python.org'])
    print('Exit code:',r)

    print('######################################')
    #如果子进程还需要输入，则可以通过communicate()方法输入
    print('$ nslookup')
    p=subprocess.Popen(['nplookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out,error=p.communicate(b'set q=mx\npython.org\nexit\n')
    print(out.decode('utf-8'))
    print('Exit code:',p.returncode)
