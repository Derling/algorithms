# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 18:23:45 2017

@author: DerlingB
"""

# Given a sorted integer array without duplicates,
# return the summary of its ranges.
# For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

def summary_of_ranges(array):
    summary = []
    start = 0 # starting index for current range
    current = start
    for i in range(1, len(array)):
        # check if curent number is one more than last number
        if array[current] + 1 == array[i]:
            current = current + 1
        else:
            # if starting and last index are same range is 1
            if start == current:
                summary.append(str(array[current]))
            # last index not same as starting so range is more than 1
            else:
                summary.append(str(array[start]) + '->' + str(array[current]))
                
            start = i # set new range to start at current number index
            current = start # new range, so new current

    # final number doesn't get check in for loop
    if start == current:
        summary.append(str(array[start]))
    else:
        summary.append(str(array[start]) + '->' + str(array[current]))
    return summary

def solution():
    # course solution
    input_array = [0,1,2,4,5,7]
    input_array = [1,2,3,6,9,11,12,13,14,19,20]

    start=0
    result = []

    # i=0
    # while i <= len(input_array)-1:
    #     print(i, input_array[i])
    #     i = i+1


    while start < len(input_array):
    
        # initial end at start position     
        end = start

        # continue to move the end pointer if the gap is 1 with beside number
        # only continue to move if index end+1 is inside array     
        while end+1<len(input_array) and ((input_array[end+1] - input_array[end]) == 1):
            end = end + 1

            # add range to result after calculate     
        if end!=start:
            result.append("{0}-->{1}".format(input_array[start], input_array[end]))
            print(result)
        else:
            result.append("{0}".format(input_array[start]))
            print(result)
        
        # change to next range
        start = end+1

    print(result)

if __name__ == '__main__':
    print(summary_of_ranges([1,2,3,6,9,11,12,13,14,19,20]))
    solution()