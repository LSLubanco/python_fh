#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 17:27:04 2019

@author: Daniel
second class exceptions
"""
while True:
    try:
        x = int(input("Enter a number: "))
        break
    except ValueError:
        print("Enter a valid number!")
    
print("You have entered the number {}".format(x))

#y=0
try:
    y = int(input("Enter a number: "))
except ValueError:
    print("Enter a valid number!")
finally:
    print("you have entered {}".format(y))