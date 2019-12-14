#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 16:37:36 2019

@author: Daniel
Second part of second class
"""
#Using underscore in for loops means that is jsut an iterator that should not be used as a variable
for _ in range(5):
    print(_)

#%%
    #Lambda function
f = lambda x: x*x
print(f(5))

# Lambda is often used in filtering functions

#%%
# import modulename ---> modulename.func,modulename.var
#  from modulename import * -->everything becomes global (dangerous)
#  from modulename import funcX  
#  import modulename as mn
