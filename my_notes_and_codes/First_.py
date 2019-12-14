#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 12:42:23 2019

@author: Daniel

First class
"""
s = 'hello world'
s[-3:len(s)+1]
# We are not allowed to change a singular item of the string
# s[0] = 'J'  is illegal
# however we can change the whole string
#s = 'new string' is legal

print(s)

#   List
# A list may have mixed data types
# A list is index accessed
# a list is muttable
# it is very flexible however the performance quality is not the highest
# compared to other available data types in python
l = [5,'a',2,9.0,[5,2,3]]
l[2] = 23 

#   tuple 
# immutable values
t = (5,4,3,2)
# packing and unpacking tuples
(a,b,c,d) = t
print(a,b,c,d)
t1 = (a+1,b+1,c+1,d+1)
print(t1)

#   Dictionary
d = {'key1':'value1','key2':'value2'}
d['key1']

# Homework go from beginning until control flow