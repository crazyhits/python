#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import listdir

for item in listdir('.'):
    #print item
    print 'name: {}'.format(item)