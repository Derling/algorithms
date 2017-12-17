# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 13:38:15 2017

@author: DerlingB
"""

# ---------------------------------------------------------------
# python best courses https://courses.tanpham.org/
# ---------------------------------------------------------------
# Write a Python program that accepts a string and calculate the number of digits and letters
# Sample Data : "Python 3.2"
# Expected Output :
# Letters 6 
# Digits 2

def count_digit_letter(string):
    letters = digits = 0
    for char in string:
        if char.isalpha():
            letters = letters + 1
        elif char.isdigit():
            digits = digits + 1
    return letters, digits

def solution():
    # course solution
    s = input("Input a string")
    d=l=0
    for c in s:
        if c.isdigit():
            d=d+1
        elif c.isalpha():
            l=l+1
        else:
            pass
    print("Letters", l)
    print("Digits", d)

if __name__ == '__main__':
    string = "Python 3.2"
    letters, digits = count_digit_letter(string)
    print('Letters: {0}\nDigits: {1}'.format(letters, digits))