# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 19:40:29 2017

@author: DerlingB
"""

# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
# You may assume that each input would have exactly one solution

# Example:
#     Given nums = [2, 7, 11, 15], target = 26,
#     Because nums[2] + nums[3] = 11 + 15 = 26,
#     return [2, 3].

def sum_indices(array, target):
    for i in array:
        # look for the difference of current number and target number in array
        if target - array[i] in array:
            return [i, array.index(target - array[i])]
    return None

def main(array, target):
    ''' Hash table solution, much more efficient '''
    
    # hash table which will keep track of numbers we have seen and their index
    seen_numbers = {}
    for index, number in enumerate(array):
        # determine the number that matches our current number in the loop
        missing = target - number

        # check if we have seen the number before
        if seen_numbers.get(missing, -1) + 1: 
            return [seen_numbers.get(missing), index]
        else:
            seen_numbers[number] = index
    return []

def solution():
    # course solution , no real solution given, filled in by me
    # before i wrote code, it was just the nested for loop
    # Solution 1
    # Try all 

    input_array = [2, 7, 11, 15]
    target = 26
    result = []
    
    for i, num in enumerate(input_array):
        for j in range(i+1, len(input_array)):
            if target - num == input_array[j]:
                result = [i, j]
                break
        if result:
            break
    print(result)

if __name__ == '__main__':
    print(sum_indices([2, 7, 11, 15], 26))
    print(main([2, 7, 11, 15], 26))