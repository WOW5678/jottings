# -*- coding:utf-8 -*-
#功能：实现mysql数据库的链接

import pymysql

#创建链接
conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='123456',db='header_url')
#创建游标
cursor=conn.cursor()

#执行sql 并返回受影响的行数
#effect_row=cursor.execute('select * from Header')
#执行sql并返回受影响的行数
#effect_row=cursor.execute("update Header set pass= '123' where nid=%s",(11,))
#执行sql 返回受影响的行数 执行多次
A=['h_0_VirusShare_00276ed337e75825aa3a706290c61de0.apk_81093.pcap_0','h_0_VirusShare_0143549ec65ed5060857ec38f7e76468.apk_26392.pcap_5']
B=[' GET getTask.php task updateOpening s HTTP 1.1 Host depositmobi.com Connection Keep-Alive User-Agent Apache-HttpClient UNAVAILABLE java 1.4','GET adv tuichu.html HTTP 1.1 User-Agent Dalvik 1.6.0 Linux U Android 4.3.1 Android SDK built for x86 Build JB_MR2 Host www.plapk.com Connection Keep-Alive Accept-Encoding gzip']
data=zip(A,B)
effect_row=cursor.executemany("insert into Header(flowName,header)VALUES(%s,%s)",[row for row in data])
#提交事务，不然无法保存新建或者修改的数据
conn.commit()
#关闭游标
cursor.close()
#关闭链接
conn.close()
