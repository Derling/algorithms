# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 11:37:07 2017

@author: DerlingB
"""

# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.

class Rectangle():
    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width
    def area(self):
        return self.width * self.length

class Solution():
    # course solution
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width
    
if __name__ == '__main__':
    class_ = Rectangle(12, 10)
    print(class_.area())