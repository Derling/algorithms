# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 22:58:50 2017

@author: Derling

src: https://www.reddit.com/r/dailyprogrammer/comments/76qk58/20171016_challenge_336_easy_cannibal_numbers/

[2017-10-16] Challenge #336 [Easy] Cannibal numbers

"""

def cannibal_number(array, query):
    ''' 
        recursive solution 
    type array: int[]
    type query: int
    rtype: int
    ''' 
    def recursion(array, query):
        if not array: # empty array
            return 0
        elif len(array) == 1: # one element in array
            return 1 if array[0] >= query else 0
        else: # check highest integer in array
            if array[-1] >= query:
                # found a strong enough cannibal, remove it and do recursion
                return 1 + cannibal_number(array[:-1], query)
            else:
                # cannibal too weak, make it eat the smallest integer
                array[-1] = array[-1] + 1
                array.pop(0)
                return 0 + cannibal_number(array, query)

    return recursion(sorted(array), query)

def cannibal_numbers(array, query): 
    ''' 
        iterative solution 
    type array: int[]
    type query: int
    rtype: int
    ''' 
    if not array: # empty array
        return 0
    if len(array) == 1: # one element in array
        return 1 if array[0] >= query else 0
    cannibals = 0
    array = sorted(array)
    while array:
        if array[-1] >= query:
            # highest element meets criteria, remove it and increment count
            cannibals += 1
            array.pop()
        else:
            # highest integer less than query, increase value and remove smallest
            array[-1] = array[-1] + 1
            array.pop(0)
    return cannibals


if __name__ == '__main__':
    int_set = [21, 9, 5, 8, 10, 1, 3]
    queries = 10, 15
    
    for i in queries:
        print(cannibal_number(int_set.copy(), i))

'''
both solutions require the array to be sorted
this makes the algorithm work really nicely
if the strongest integers are in the back
all they have to do is feast on the weaker ones
if the array is sorted the weaker ones are at the beginning of the array
*** not optimized for space *** 
'''
