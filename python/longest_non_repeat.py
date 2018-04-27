# -*- coding: utf-8 -*-

def longest_non_repeat(string):
    longest_sub = index = 0
    current_sub = {}
    while index < len(string):
        char = string[index]
        if not current_sub.get(char, None):
            current_sub[char] = index
        else:
            if len(current_sub) > longest_sub:
                longest_sub = len(current_sub)
            index = current_sub[char]
            current_sub = {}
        index += 1
    if current_sub and len(current_sub) > longest_sub:
        longest_sub = len(current_sub)
    return longest_sub

if __name__ == '__main__':
    tests = ['abcabcbb',
             'bbbbb',
             'pwwkew',
             ]
    for string in tests:
        print(longest_non_repeat(string))