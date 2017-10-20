# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 22:58:50 2017

@author: Derling

src: https://www.reddit.com/r/dailyprogrammer/comments/76qk58/20171016_challenge_336_easy_cannibal_numbers/

[2017-10-16] Challenge #336 [Easy] Cannibal numbers

"""

def get_cannibals(int_set, query): # O(n) speed
    count = 0
    highest = max(int_set)
    while highest >= query:
        count += 1
        int_set.remove(highest)
        highest = max(int_set)
    while len(int_set) > 1:
        int_set.remove(min(int_set))
        int_set[int_set.index(max(int_set))] = max(int_set) + 1
        if max(int_set) == query:
            count += 1
            int_set.remove(max(int_set))
    return count

def cannibals(int_set, query): # O(log n)
    int_set = sorted(int_set)
    count = 0
    while len(int_set) > 1:
        if int_set[-1] >= query:
            int_set.pop()
            count += 1
        else:
            int_set[-1] = int_set[-1] + 1
            int_set.pop(0)
    return count if int_set[0] != query else count + 1

if __name__ == '__main__':
    int_set = list(map(int, input('Enter the sacrifices:\n').split()))
    queries = list(map(int, input('Enter the queries:\n').split()))
    results = []
    test = []
    for c in queries:
        results.append(get_cannibals(int_set.copy(), c))
        test.append(cannibals(int_set.copy(), c))
    print(results, test)