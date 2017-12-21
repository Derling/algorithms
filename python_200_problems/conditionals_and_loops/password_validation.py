# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 14:16:26 2017

@author: DerlingB
"""

# Write a Python program to check the validity of a password (input from users).

# Validation :

# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

# Input
# W3r@100a
# Output
# Valid password

import re

def password_validation(password):
    if len(password) < 6 or len(password) > 16:
        return 'Invalid Password'
    elif (not re.search('[a-z]', password) or 
          not re.search('[A-Z]', password) or
          not re.search('[0-9]', password) or
          not re.search('[$#@]', password) or
          re.search('\s', password)):
        return "Invalid Password"
    return "Valid Password"

def solution():
    # course solution
    p= input("Input your password")
    x = True
    while x:  
        if (len(p)<6 or len(p)>12):
            break
        elif not re.search("[a-z]",p):
            break
        elif not re.search("[0-9]",p):
            break
        elif not re.search("[A-Z]",p):
            break
        elif not re.search("[$#@]",p):
            break
        elif re.search("\s",p):
            break
        else:
            print("Valid Password")
            x=False
            break

    if x:
        print("Not a Valid Password")

if __name__ == '__main__':
    print(password_validation('W3r@100a'))