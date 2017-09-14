# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 13:51:23 2017

[2017-09-13]Challenge # 331 [Intermediate] Sum of digits of x raised to n 

@author: Derling
"""

def sum_of_digits(base, power):
    ''' return the sum of the digits of x to the power of n'''
    count = 0
    for digit in map(int, str(pow(base, power))):
        count+= digit 
    return count

if __name__ == '__main__':
    x, n = map(int, input('Enter the number followed by the power:\n').split())
    print(sum_of_digits(x, n))