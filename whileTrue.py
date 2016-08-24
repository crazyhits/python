#!/usr/bin/env python
# -*- coding: utf-8 -*-

number = 18
running = True

while running:
    guess = int(raw_input('Enter your intager: '))
    if guess == number:
        print 'you are right!'
        running = False
    elif guess > number:
        print 'too large!'
    else:
        print 'too little!'
else:
    print 'end!'
print 'done'
