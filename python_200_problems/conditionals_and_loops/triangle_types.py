# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 14:27:51 2017

@author: DerlingB
"""

# Write a Python program to check a triangle is equilateral, isosceles or scalene.
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.

def triangle_types(sides):
    if len(sides) != 3:
        return None
    if sides[0] == sides[1] == sides[2]:
        return 'Equilateral Triangle'
    elif sides[0] != sides[1] != sides[2]:
        return 'Scalene Triangle'
    else:
        return "Isoceles Triangle"

if __name__== '__main__':
    # example input 1 2 3 or 3 3 3 or 2 2 4
    sides = input('Enter the sides of the triangle: ').split()
    print(triangle_types(sides))