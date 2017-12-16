# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 11:26:52 2017

@author: DerlingB
"""

# Write a Python class which has two methods get_String and print_String. 
# get_String accept a string from the user and print_String print the string in upper case.

class String_Class():
    def get_string(self, string):
        self.string = string
    def print_string(self):
        print(self.string.upper())

class IOString():
    # course solution
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input()

    def print_String(self):
        print(self.str1.upper())

if __name__ == '__main__':
    class_ = String_Class()
    class_.get_string('lower case')
    class_.print_string()
