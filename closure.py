#!/usr/bin/env python
# -*- coding: utf-8 -*-

#闭包：内部函数局部作用域可以引用外部函数局部作用域中的变量
def foo():
    a = 1
    def bar():
        b = 2
        c = 3
        return a + b + c
    return bar

#bar是个函数，调用函数foo()    
bar = foo()
#调用bar()
print bar()