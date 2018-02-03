#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
python类中没有私有变量和方法。所以你想在类中创建一个实例变量或私有方法，你必须遵守规则：
1.一个下划线_表示私有变量和方法。
2.两个下划线__表示的变量和方法，它们的名字会被修改。
'''
class Foo(object):
    def __init__(self):
        self.public = 'public'
        self._private = 'public'
        self.__secret = 'secret'
        
foo = Foo()
print foo.public
print foo._private
print foo._Foo__secret
