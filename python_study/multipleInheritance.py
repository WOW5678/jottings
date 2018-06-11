# -*- coding:utf-8 -*-
#功能：理解多重继承

#动物类
class Aninmal(object):
    pass
#哺乳动物类
class Mammal(Aninmal):
    pass
#鸟类
class Bird(Aninmal):
    pass

#各种动物 狗类
class Dog(Mammal):
    pass
#蝙蝠类
class Bat(Mammal):
    pass
#鹦鹉类
class Parrot(Bird):
    pass
#鸵鸟类
class Ostrich(Bird):
    pass

#现在，要给动物加上Runnale()和Flyable的功能，只需要定义Runnable和Flyable的类
class Runnable(object):
    def run(self):
        print('Running....')
class Flyable(object):
    def fly(self):
        print('Flying....')
#对于需要Runnable功能的动物，只需要多继承一个Runnable
class Dog(Mammal,Runnable):
    pass


