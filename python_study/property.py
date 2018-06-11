# -*- coding:utf-8 -*-
#功能：理解@property的用法

#为了对属性进行检查，我们一般需要在类内做限定，如下
class Student(object):
    def get_score(self):
        return self._score
    def set_score(self,value):
        #先判断给定的参数是否符合要求
        if not isinstance(value, int):
            raise  ValueError('Score must be an integer!')
        if value>100 or value<0:
            raise ValueError(u'Score的范围必须在0-100之间！')
        self._score=value

s=Student()
s.set_score(100)
print(s.get_score())
#上面的例子略显复杂，没有直接用属性那么简答
#---------------------------------------------------------------------------------
#把一个getter方法变成属性，只需要加上@property就可以了。此时，@property本身又创建了另一个装饰器@score.setter,
#负责把setter方法变成属性赋值
class Student(object):
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self,value):
        self._birth=value

    #_age是只读属性
    @property
    def age(self):
        return 2017-self._birth

#可以直接调用属性
s=Student()
s.birth=1900
print(s.birth)
print(s.age)
