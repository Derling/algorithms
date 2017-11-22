# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 22:58:50 2017

@author: Derling

src: https://www.reddit.com/r/dailyprogrammer/comments/76qk58/20171016_challenge_336_easy_cannibal_numbers/

[2017-10-16] Challenge #336 [Easy] Cannibal numbers

"""

def cannibal_number(array, query):
    ''' recursive solution ''' 
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
    ''' iterative solution ''' 
    if not array: # empty array
        return 0
    if len(array) == 1: # one element in array
        return 1 if array[0] >= query else 0
    cannibals = 0
    array = sorted(array)
    for i in range(len(array)):
        if not array: # array is empty because of loop so we should break
            break
        elif array[-1] >= query:
            # highest element meets criteria, remove it and increment count
            cannibals += 1
            array.pop()
        else:
            # highest integer less than query, increment it and remove smallest
            array[-1] = array[-1] + 1
            array.pop(0)
    return cannibals


if __name__ == '__main__':
    int_set = [int(i) for i in input('Enter the sacrifices:\n').split()]
    queries = [int(i) for i in input('Enter the queries:\n').split()]
    results = [[], []]

    for c in queries:
        results[0].append(cannibal_number(int_set.copy(), c))
        results[1].append(cannibal_numbers(int_set.copy(), c))

    if results[0] == results[1]: # functions produce same results
        print('For the quieres of', queries, 'using the integers', int_set,
              ', the results were,', results[0])
    else:
        print('error with functions') 
