# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 16:15:38 2017

@author: DerlingB
"""

# Consider an array of non-negative integers.
# A second array is formed by shuffling the elements of the first array and deleting a random element. 
# Given these two arrays, find which element is missing in the second array.
# Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.
# Input:
# finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
# Output:
# 5 is the missing number

def missing_element(arr1, arr2):
    for i in arr1:    
        # check if a number exists in other array
        if i not in arr2:
            return i
    return 0

def finder(first_array, second_array):
    # course solution
    return(sum(first_array) - sum(second_array))

if __name__ == '__main__':
    print(missing_element(
            [1,2,3,4,5,6,7], [3,7,2,1,4,6]
            )
    )