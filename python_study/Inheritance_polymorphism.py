# -*- coding:utf-8 -*-
#功能：理解python的继承和多态

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    #在子类中重写父类的方法
    def run(self):
        print('Dog is running...')
    #在子类中添加自己独特的方法
    def eat(self):
        print('Eating meat...')
class Cat(Animal):
    pass

animal=Animal()
animal.run()
#因为Dog和 cat都是Animal的子类，都拥有Animal的所有方法
dog=Dog()
#当调用run方法时会优先选择执行自己重写的方法
dog.run()
cat=Cat()
cat.run()

#判断一个变量是否属于某个类型
print(isinstance(dog,Dog))  #true
print(isinstance(dog,Animal)) #true 子类对象一定是父类的类型 但是反过来 父类的对象就一定不是子类的类型
print(isinstance(animal,Dog))  #false
print(isinstance(cat,Cat))    #true


#--------------------------------------动态语言的鸭子类型--------------------------------------
class Timer(object):
    def run(self):
        print('Start....')

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(dog)
run_twice(cat)
#只需要传入的对象具有run方法就可以执行
run_twice(Timer())

#-----------------------------一个例子理解以上所有内容--------------------------------------------------
class Provice(object):
    def __init__(self,provicename):
        self.provicename=provicename
    def ps(self):
        print('I am in %s'%self.provicename)
#子类
class City(Provice):
    def __init__(self,provicename,cityname):
        self.cityname=cityname
        Provice.__init__(self,provicename)
    def psl(self):
        print('I am in %s-%s'%(self.provicename,self.cityname))

#定义一个独立的类
class Timer(object):
    def ps(self):
        print(u'我不属于Provice类及其子类，但是我有ps方法');
    def psl(self):
        print(u'我不属于Provice类及其子类，但是我有psl方法')

#定义一个函数
def f(x):
    x.ps()
    x.psl()

#调用部分
f(City(u'上海',u'浦东'))
f(Timer())