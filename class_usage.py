#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Animal(object):
    run = True
class Dog(Animal):
    fly = False
    def __init__(self, age):
        self.age = age
    def sound(self):
        return "wang wang~"

#实例化一个对象dog
dog = Dog(1)
#查看dog对象的属性
print dog.__dict__
print dog.age
print dog.run
print dog.fly
#访问dog对象的sound方法
print dog.sound()
