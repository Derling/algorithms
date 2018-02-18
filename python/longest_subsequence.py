# -*- coding: utf-8 -*-
"""
CGiven a string S and a set of words D, find the longest word in D that is a subsequence of S.

Word W is a subsequence of S if some number of characters, possibly zero, can be deleted from S to form W, without reordering the remaining characters.

Note: D can appear in any format (list, hash table, prefix tree, etc.

For example, given the input of S = "abppplee" and D = {"able", "ale", "apple", "bale", "kangaroo"} the correct output would be "apple"

The words "able" and "ale" are both subsequences of S, but they are shorter than "apple".

The word "bale" is not a subsequence of S because even though S has all the right letters, they are not in the right order.

The word "kangaroo" is the longest word in D, but it isn't a subsequence of S.
"""

def longest_subseq(string, words):
    longest_seq = ''
    
    for word in words:
        last_index = -1 # index of last charcter that was found to be in the string
        current_seq = ''
        
        for c in word:
            char_index = string.find(c, last_index + 1) 
            
            # check if current character is in the string
            # last_index + 1 to check after the last character we found in the string
            if char_index != -1 and char_index > last_index:
                last_index = char_index
                current_seq += c
            else:
                current_seq = ''
                break
        if len(current_seq) > len(longest_seq):
            longest_seq = current_seq
    return longest_seq

if __name__ == '__main__':
    string = 'abpplee'
    words = ['able', 'ale', 'apple', 'bale', 'kangaroo']
    print(longest_subseq(string, words))