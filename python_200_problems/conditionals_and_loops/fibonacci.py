# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 14:02:14 2017

@author: DerlingB
"""

# Write a Python program to get the Fibonacci series between 0 to 50

def fibonacci(n):
    previous, current = 0, 1
    while current < n:
        yield current
        previous, current = current, previous + current

'''
def fibonacci_recursive(previous, current, n):
    if current < n:
        print(current)
        fibonacci_recursive(current, previous + current, n)
'''
def solution():
    x,y=0,1

    while y<50:
        print(y)
        x,y = y,x+y

if __name__ == '__main__':
    for n in fibonacci(50):
        print(n)