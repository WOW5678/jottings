# -*- coding:utf-8 -*-
#功能：访问控制
#在属性的名称前加上两个下划线，就变成了一个私有变量
#在属性的名称前加上一个下划线，外部实例时可以访问的，但是要把它视为私有变量
# 以双下划线开头，并且以双下划线结尾的，是特殊变量，可以直接访问
#
class Students(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def print_score(self):
        print('%s:%s' %(self.__name,self.__score))


if __name__ == '__main__':
    student_01=Students('Lucy',59)
    student_02=Students('Lily',29)
    student_01.print_score()
    student_02.print_score()
    #试图从外面直接访问私有变量 会报错
    #print('__name:',student_01.__name)