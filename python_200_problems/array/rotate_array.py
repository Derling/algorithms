# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 17:37:32 2017

@author: DerlingB
"""

# Rotate an array of n elements to the right by k steps.
# For example, with n = 7 and k = 3,
# the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
# Note:
# Try to come up as many solutions as you can,
# there are at least 3 different ways to solve this problem.

def rotate_array(array, steps = 1):
    ''' 
        take the last x(steps) numbers and store them in a temp varible
        move the first elements, not including the last x(steps) elements
        x(steps) forward, finally replace the first x(steps) elements with
        the last x(steps) elements
    '''
    last_slice = array[len(array) - steps:]
    array[steps:] = array[0: len(array) - steps]
    array[0: steps] = last_slice
    return array
    
def solution():
    # course solution
    org = [1,2,3,4,5,6,7]
    result = org[:]
    steps = 3

    for idx,num in enumerate(org):
        if idx+steps < len(org):
            result[idx+steps] = org[idx]
        else:
            result[idx+steps-len(org)] = org[idx]

    print(result)

if __name__ == '__main__':
    print(rotate_array([1,2,3,4,5,6,7], 3))