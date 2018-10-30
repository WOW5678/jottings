# -*- coding: utf-8 -*-
"""
 @Time    : 2018/10/30 0030 上午 8:57
 @Author  : Shanshan Wang
 @Version : Python3.5
 @Function: python 操作mysql数据库（增删改查）
"""
import pymysql

# python操作mysql数据库的三种方式：1、pymysql  2、mysqldb 3、sqlalchemy
#1.数据库的连接
conn=pymysql.connect(host='localhost',port=3307,user='root',password='root',db='test',charset='utf8')
print('conn')

# 2.创建操作的游标
cursor=conn.cursor()

# 3. 设置字符编码以及自动提交
cursor.execute('set name utf8')
cursor.execute('set autommit=1')
conn.commit()

# 4.编写sql 语句
# sql="insert into tb_user(name,pwd) values('dfy8888','222')"
# sql="delete from tb_user where id={0}".format(2)
# sql="update tb_user set pwd='333' where name='dfy999'"
sql='select * from tb_user'

# 5. 执行sql 并且取得结果集
cursor.execute(sql)

#得到结果的三种方式
result=cursor.fetchall()
result=cursor.fetone()
result=cursor.fetmany()

# 6.关闭游标和连接
cursor.close()
conn.close()
