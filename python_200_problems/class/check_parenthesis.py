# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 17:14:29 2017

@author: DerlingB
"""

# ---------------------------------------------------------------
# python best courses https://courses.tanpham.org/
# ---------------------------------------------------------------
# Write a Python program to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. 
# These brackets must be close in the correct order, 
# for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.


class solution():
    def valid_parentheses(self, string):
        # hash table for determining what the previous character should of been
        legend = {
                '(' : 0,
                ')' : 1,
                '[' : 2,
                ']' : 3,
                '{' : 4,
                '}' : 5,
                }
        
        # if not even length of string, there are not enough pairs
        if len(string) % 2: 
            return False
        
        
        for i in range(len(string)):
            # every odd character should be a closure
            if i % 2:
                # if previous  character was not an opening then 
                # the last opening was not closed ---- return False
                if legend[string[i - 1]] + 1 != legend[string[i]]:
                    return False
        
        return True

class py_solution:
    # course solution
    def is_valid_parenthese(self, str1):
         stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
         for parenthese in str1:
             if parenthese in pchar:
                 stack.append(parenthese)
             elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                 return False
         return len(stack) == 0

if __name__ == '__main__':
    print(solution().valid_parentheses('()[]{}'))