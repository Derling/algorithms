# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 14:08:56 2017

@author: DerlingB
"""

#  Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700

def find_numbers(divisble, multiple, lower_bound, upper_bound):
    for i in range(lower_bound, upper_bound):
        if i % 7 == 0 and i % 5 == 0:
            yield i

def solution():
    # course solution
    nl=[]
    for x in range(1500, 2700):
        if (x%7==0) and (x%5==0):
            nl.append(str(x))
    print (','.join(nl))

if __name__ == '__main__':
    for i in find_numbers(7, 5, 1500, 2700):
        print(i)    