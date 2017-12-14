# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 17:41:12 2017

@author: DerlingB
"""

# Write a Python class named Circle constructed by a radius and two methods which
# will compute the area and the perimeter of a circle.

from math import pi


class Circle():
    def __init__(self, radius= 0):
        self.radius = radius
    def area(self):
        return pi * pow(self.radius, 2)
    def perimeter(self):
        return 2 * pi * self.radius

class solution():
    # course solution
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14


if __name__ == '__main__':
    NewCircle = Circle(8)
    print(NewCircle.area())
    print(NewCircle.perimeter())