# -*- coding:utf-8 -*-
#功能：关于属性绑定的用法

#正常情况下，当我们定义了一个class的实例之后，我们可以给该实例绑定任何的属性和方法，这就是动态语言的灵活性。
class Student(object):
    pass

s=Student()
s.name='Lily'
print(s.name)
#给实例绑定一个方法
from types import MethodType
def set_age(self,age):
    self.age=age
s.set_age=MethodType(set_age,s)
s.set_age(25)
print(s.age)

#但是要注意，给一个实例绑定的方法对另外一个实例是不起作用的
s2=Student()
#AttributeError: 'Student' object has no attribute 'age'
#print(s2.age)

#---------------------给实例绑定方法-------------------------------------------------------
def set_socre(self,score):
    self.score=score
#相当于给每个实例绑定了一个方法
Student.set_score=set_socre

s2.set_score(100)
print(s2.score)
s.set_score(99)
print(s.score)

#限制属性，只允许对student实例添加name和age属性
class Student(object):
    __slots__ = ('name','age')
s=Student()
s.name='Lucy'
s.age=15
#AttributeError: 'Student' object has no attribute 'score'
#s.score=99
#使用__slots__时应该注意，限定的属性仅仅对当前类实例起作用，对继承的子类是不起作用的
class GraduateStudent(Student):
    pass

g=GraduateStudent()
#不报错
g.score=99
print(g.score)

#除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__