# -*- coding: utf-8 -*-
"""
 @Time    : 2018/8/12 0012 下午 9:11
 @Author  : Shanshan Wang
 @Version : Python3.5
 function:从EHR中提取出我们需要的数据（主诉，现病史、既往史、诊断），并且写入到csv文件中
"""
import pyodbc
import csv
import re
'''
连接数据库
'''
def connectAccessDB(DBfile):
    connectStr = "Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + DBfile + ";"
    conn = pyodbc.connect(connectStr)
    cursor = conn.cursor()
    return conn,cursor

def extractInformation(cursor):
    patient2zhusu={}
    patient2current={}
    patient2history={}
    patient2diagnoise={}
    patient2reviseDiagnoise={}
    patient2addDiagnoise={}
    patten_0 = re.compile('<%s>.*?</%s>' % ('主诉', '主诉'))
    patten_1 = re.compile('<%s>.*?</%s>' % ('现病史', '现病史'))
    patten_2 = re.compile('<%s>.*?</%s>' % ('既往史', '既往史'))
    patten_3=re.compile('<%s>.*?</%s>' % ('初步诊断', '初步诊断'))
    patten_4=re.compile('<%s>.*?</%s>' % ('修正诊断', '修正诊断'))
    patten_5=re.compile('<%s>.*?</%s>' % ('补充诊断', '补充诊断'))
    SQL = "SELECT 住院号,XML结构化病历 from dbo_电子病历;"
    for row in cursor.execute(SQL):
        if row[0] not in patient2zhusu and row[1]!= None:
            item= patten_0.findall(row[1])[0]
            Item = re.sub('<.*?>', '', item)
            patient2zhusu[row[0]]=Item

            # 现病史
            item = patten_1.findall(row[1])[0]
            Item = re.sub('<.*?>', '', item)
            patient2current[row[0]] = Item
            # 既往史
            item = patten_2.findall(row[1])[0]
            Item = re.sub('<.*?>', '', item)
            patient2history[row[0]] = Item
            #初步诊断
            item = patten_3.findall(row[1])[0]
            Item = re.sub('<.*?>', '', item)
            patient2diagnoise[row[0]] = Item
            # 修正诊断
            item = patten_4.findall(row[1])[0]
            Item = re.sub('<.*?>', '', item)
            patient2reviseDiagnoise[row[0]] = Item
            # 补充诊断
            item = patten_5.findall(row[1])[0]
            Item = re.sub('<.*?>', '', item)
            patient2addDiagnoise[row[0]] = Item
    patientData=[]
    for key in patient2zhusu.keys():
        temp=[key,patient2zhusu[key],patient2current[key],patient2history[key],patient2diagnoise[key],patient2reviseDiagnoise[key],patient2addDiagnoise[key]]
        patientData.append(temp)
    return patientData
''' 
将需要的信息写入csv文件中
'''
def writeCSV(data):
    with open('..\data\patientInformation.csv','w',newline='') as f:
        writer=csv.writer(f)
        writer.writerow(['住院号','主诉','现病史','既往史','初步诊断','修正诊断','增加诊断'])
        writer.writerows(data)

if __name__ == '__main__':
    DBfile = r"..\data\肝病（除医嘱）.accdb"  # 数据库文件
    conn,cursor=connectAccessDB(DBfile )
    patientData=extractInformation(cursor)
    writeCSV(patientData)
    cursor.close()
    conn.close()
