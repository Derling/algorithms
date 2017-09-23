# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 17:47:15 2017

@author: Derling
"""

def first_non_repeated(string):
    # 1. find the first non-repeated character in a string
    for s in string:
        if not string.count(s) - 1:
            return s
    return None

def reverse_string(string):
    # 2. reverse a string
    new_string = ''
    for s in range(len(string) - 1, -1, -1):
        new_string += string[s]
    return new_string

def reverse_string_fast(string):
    # 2. reverse a string
    return string[::-1]

def reverse_string_fast_2(string):
    # 2. reverse a string
    return ''.join(reversed(string))

def reverse_string_recursive(string):
    # 2. reverse a string
    if not len(string):
        return ''
    elif len(string) == 1:
        return string
    return string[-1] + reverse_string_recursive(string[0: len(string) - 1])

def anagram(first, second):
    # 3. determine if 2 string are anagrams
    ''' remove white space as they can be used for anagrams '''
    first, second = first.replace(' ', ''), second.replace(' ', '')
    if len(first) != len(second):
        return False
    while first:
        char = first[0]
        print(char)
        if char not in second:
            return False
        first, second = first[1:], second.replace(char, '', 1)
    return True

def anagram_fast(first, second):
    # 3. determine if 2 strings are anagrams
    return sorted(first.replace(' ', '')) == sorted(second.replace(' ', ''))

def anagram_recursive(first, second):
    # 3. determine if 2 strings are anagrams
    first, second = first.replace(' ', ''), second.replace(' ', '')
    def recursion(first, second):
        print(first, second)
        if len(first) and len(second) == 1:
            return True if first == second else False
        elif first[0] in second:
            return recursion(first[1:], second.replace(first[0], '', 1))
        return False
    return recursion(first, second)

def palindrome(word):
    # 4. determine if 2 words are palindrones
    return word.replace(' ', '') == ''.join(reversed(word.replace(' ', '')))

def palindrome_r(word):
    # 4. determine if 2 words are palindrones
    word = word.replace(' ', '')
    def recursive(word):
        if len(word) == 1 and word[0] == word[-1] or not word:
            return True
        elif word[0] == word[-1]:
            return recursive(word[1: len(word) - 1])
        return False
    return recursive(word)

def palindrome_p(word):
    # 4. determine if 2 words are palindrones
    word = word.replace(' ', '')
    for i in range(int(len(word)/2)):
        if not word[i] == word[len(word) - i - 1]:
            return False
    return True

def unique_characters_fast(string):
    # 5. check if a string is composed of unique characters
    return len(set(string)) == len(string)

def unique_characters_short(string):
    # 5. check if a string is composed of unique characters
    from collections import Counter
    counter = Counter(string)
    for v in counter.values():
        if v > 1:
            return False
    return True

def unique_characters_long(string):
    # 5. check if a string is composed of unique characters
    count = {}
    for i in string:
        count[i] = count.get(i, 0) + 1
    for i in count:
        if count[i] > 1:
            return False
    return True

def unique_characters_medium(string):
    # 5. check if a string is composed of unique characters
    for i in string:
        if string.count(i) > 1:
            return False
    return True

def int_or_float(string): # genuinely couldn't think of anything better
    # 6. determine if a string is an int or float
    return float if bool(string.count('.')) else int

def int_or_float_v2(string):
    # 6. determine if a string is an int or float
    return int if float(string).is_integer() else float

def find_all_permutations(string):
     # 8. find all permutations for a string
    import itertools
    return [''.join(p) for p in itertools.permutations(string)]

def permutations(string):
    # 8. find all permutations for a string
    if len(string) == 0:
        return ['']
    prevList = permutations(string[1:len(string)])
    nextList = []
    for i in range(0,len(prevList)):
        for j in range(0,len(string)):
            newString = prevList[i][0:j]+string[0]+prevList[i][j:len(string)-1]
            nextList.append(newString)
    return nextList

if __name__=='__main__':
    pass