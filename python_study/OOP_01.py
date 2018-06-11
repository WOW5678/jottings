# -*- coding:utf-8 -*-
#功能：实现一个简单的面向对象的例子
class Students(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def print_score(self):
        print('%s:%s' %(self.name,self.score))


if __name__ == '__main__':
    student_01=Students('Lucy',59)
    student_02=Students('Lily',29)
    student_01.print_score()
    student_02.print_score()