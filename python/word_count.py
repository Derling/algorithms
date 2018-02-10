# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 20:53:46 2017

Mock Interview question, completed on own time for self improvement.

Also, used python 3.6 features to familiarize myself with type hinting

@author: Derling
"""

punctuation: list = [
    ',',
    '.',
    '!',
    '?',
    ]

def count_words(word_arr: list) -> dict:
    ''' count the occurences of a word in a paragraph '''
    count: dict = {}
    for word in word_arr:
        count[word] = count.get(word, 0) + 1
    return count

def check_punctuation(word: str) -> str:
    ''' check if a word ends with a punctuation and remove it '''
    return word[:-1] if word[-1] in punctuation else word

if __name__ == '__main__':
    arr: list = list(map(check_punctuation,
                         input("Enter a paragraph:").split()))
    print(count_words(arr))
