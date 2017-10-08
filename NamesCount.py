#!/usr/bin/env python
# -*- coding: utf-8 -*-

def names_count():
    count = {}
    with open('names.txt') as f:
        for i in f.readlines():
            i = i.strip()
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
            
        for k, v in sorted(count.items(), key=lambda x: x[1], reverse=True):
            print k, v
            
if __name__ == '__main__':
    names_count()