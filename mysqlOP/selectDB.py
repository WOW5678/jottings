# -*- coding:utf-8 -*-
#功能：从数据库中查询数据
import pymysql

#数据库连接对象
conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='123456',db='header_url')
#游标对象
cursor=conn.cursor()
#执行sql语句查询
cursor.execute("select * from malicious_header where flowName ='h_0_VirusShare_0cd45ee53e65ae5f3946203771cea364.apk_77289.pcap_0'")
#获取剩余结果的第一行数据
row_1=cursor.fetchone()
print (row_1)
print (row_1[1])
#获取剩余结果前n行数数据
# row_2=cursor.fetchmany(3)
# #获取剩余结果所有数据
# row_all=cursor.fetchall()

#提交事务
conn.commit()
#关闭游标
cursor.close()
#关闭连接
conn.close()
