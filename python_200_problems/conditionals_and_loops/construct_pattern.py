# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 13:32:18 2017

@author: DerlingB
"""

# ---------------------------------------------------------------
# python best courses https://courses.tanpham.org/
# ---------------------------------------------------------------
#  Write a Python program to construct the following pattern, using a nested for loop.
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

def construct_pattern(n):
    # generator
    for i in range(n):
        yield str('* ' * i)
    for i in range(n, 0, -1):
        yield str('* ' * i)

def solution():
    n=5;
    for i in range(n):
        for j in range(i):
            print ('* ', end="")
        print('')

    for i in range(n,0,-1):
        for j in range(i):
            print('* ', end="")
        print('')

if __name__ == '__main__':
    for pattern in construct_pattern(5):
        print(pattern)