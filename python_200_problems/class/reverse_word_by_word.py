# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 11:40:10 2017

@author: DerlingB
"""

# Write a Python class to reverse a string word by word.
# Input "hello world"
# Output "world hello"

class Reverse_Words():
    def reverse(self, string):
        # seperate each word
        words = string.split()

        # join all the words together starting from the back of the words array
        return ' '.join([words[i - 1] for i in range(len(words), 0, -1)])
    '''
    def reverse(self, string):
        # easier to read version of above code
        # less pythonic :(
        words = string.split()
        results = ' '
        for i in range(len(words), 0, -1):
            results = results + words[i - 1]
        return results
    '''

class py_solution:
    # course solution
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))


if __name__ == '__main__':
    class_ = Reverse_Words()
    print(class_.reverse('hello world'))