# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 17:47:15 2017

@author: Derling
"""

def first_non_repeated(string):
    # 1. find the first non-repeated character in a string
    for s in string:
        if not string.count(s) - 1:
            return s
    return None

def reverse_string(string):
    # 2. reverse a string
    new_string = ''
    for s in range(len(string) - 1, -1, -1):
        new_string += string[s]
    return new_string

def reverse_string_fast(string):
    # 2. reverse a string
    return string[::-1]

def reverse_string_fast_2(string):
    # 2. reverse a string
    return ''.join(reversed(string))

def reverse_string_recursive(string):
    # 2. reverse a string
    if not len(string):
        return ''
    elif len(string) == 1:
        return string
    return string[-1] + reverse_string_recursive(string[0: len(string) - 1])
if __name__=='__main__':
    print(first_non_repeated('aabbccdeeffgg'))
    print(reverse_string_fast_2('aabbccdeeffgg'))
    print(reverse_string_recursive('aabbccdeeffgg'))