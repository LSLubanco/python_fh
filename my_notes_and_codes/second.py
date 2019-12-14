#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 15:21:25 2019

@author: Daniel
Second scientific python class
"""
# %%
#if statement
x = int(input("Please put a number\n"))

if x < 0:
    print("number is negative!")
    if x < -5:
        print("number is smaller than minus five")
elif x ==0:
    print("number is zero")
else:
    print("Number is positive")

print("done!")

# %%
#loops

#range(init,stop_condition,step_size)
for x in range(-5,5,1):
    if(x == -1):
        break
    if x == -4:
        continue
    if x == -2:
        pass #used only for late implementation of code
    print(x)
#for x in range(-5,-50,-2):
#    print(x)

#l = list(range(20))
#print(l)
l2 = ["Sci","Computing", "with","Python"]
 
for l in l2:
    print(l)
dictionary= {0:"a",1:"b",2:"c"}
for k in dictionary:
    print(k, dictionary[k])
for k,d in dictionary.items():
    print(k,d)

# to add loop counter/ keep track of it
print("\n#############################\n")
for a,b in enumerate(range(-3,3)):
    print(a,b)    
# %%
#List Comprehension
    #Vectorization --> Reduce execution time
l = [x for x in range(10)]
print(l)
l = [x**2 for x in range(10)]
print(l)
# %%
#While loop

while(True):
    print(1)
    break

# %%
    
#Functions


def say_hello(text,i=1):
    print(text*i)
print("Out of function")

def add_func(a,b = 5):
    return (a+b,a,b)
def add_func2(a,b = 5):
    return [a+b,a,b]
print(add_func2(5,2))

print(add_func("a","b"))

































