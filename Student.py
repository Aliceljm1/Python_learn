#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'ljm'


#定义一个基类
class IPerson(object):
    def run(self):
        print("person is runing")

#覆盖toString方法
    def __str__(self):
        return 'IPerson object (name: %s)' % self.name

#实现迭代方法，实现下标访问：__getitem__，实现下标赋值__setitem__
    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    #没有找到属性的时候尝试访问__getattr__方法，此时我们可以做一个默认的映射
    
    #当我们没有设置age属性的时候，如果用户访问了就返回一个函数，这个函数的返回值是25. 调用形式，obj.age()
    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr) #抛出异常

#callable 来判定某个量是对象还是函数

def testRun(IPerson):
    IPerson.run()

callable(testRun)

#定义子类集成Person
class Student(IPerson):
    """description of class"""
    #限制属性，不允许扩展
    __slots__ = ('name', '__id')
    def __init__(self, name,id,age=12,_birth='2010'):
        self.name=name
        self.__id=id
        #不能直接访问__id,

    def getId(self):
        return self.__id
   
    #覆盖父类的方法
    def run(self):
        print("Student is runing")
    #覆盖特定函数，len（obj）
    
    def __le__(self, **kwargs):
        return super().__le__(**kwargs)
    
    #装饰器定义一个属性类似getter方法
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth


 #timer的对象可以直接调用testRun方法，无需继承IPerson，
class Timer(object):
    def run(self):
        print('Start...')
        print(isinstance(self,IPerson))
        print(dir(self))#获取一个对象所有的属性和方法

    
stu=Student('ljm',27)
#类似反射，获取设置属性
hasattr(stu,"name")
setattr(stu,"name","testljm")

#给对象一个实例属性
stu.temp_a="asfasdf"





#枚举

from enum import Enum
#定义
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

m1=Month.Feb

#循环
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

#准确定义某一个枚举类

from enum import Enum,unique

@unique #@unique装饰器可以帮助我们检查保证没有重复值。
class WeekDay(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1=WeekDay.Sun


