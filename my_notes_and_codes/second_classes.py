#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 16:57:14 2019

@author: Daniel
Section of second class which python classes are discussed as well as exceptions
OOP - Classes
    clustering of functions that are called methods
    with properties that are called variables
"""
class Point:
    '''
    Simple Class to handle 2D coordinates of points
    '''
    def __init__(self,x,y):
        '''
        Create a 2D point (defining its properties)
        '''
        self.x = x
        self.y = y
    
    def translate(self, dx,dy):
        '''
        translate point by dx, dy distances
        '''
        self.x += dx
        self.y += dy
        
    #Defining printing method for our object
    def __str__(self):
        return ("point at x: {}, y: {}".format(self.x,self.y))
    
