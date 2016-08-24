#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Persion:
    def __init__(self, name):
        self.name = name
    def sayhi(self):
        print 'hello,my name is', self.name

p = Persion('bob')
p.sayhi()
