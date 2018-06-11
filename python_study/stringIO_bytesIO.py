# -*- coding:utf-8 -*-
#功能：了解python的StringIO和BytesIO
from io import  StringIO
f=StringIO()
f.write('Hello')
#使用getvalue方法获得写入后的str
print(f.getvalue())
print('####################################')
#要读取StringIo,可以用一个str初始化stringio,然后像读文件一样读取
f=StringIO('Hello\nHi!\nGoodbye\n')
while True:
    s=f.readline()
    if s=='':
        break
    print(s.strip())
print("######################################")
from io import  BytesIO
f=BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())
print('#######################################')
f=BytesIO()
#写入的不是str，而是经过了Utf-8编码之后的Bytes
f.write('中国'.encode('utf-8'))
print(f.getvalue())
