#!/usr/bin/env python
'''src : https://www.reddit.com/r/dailyprogrammer/comments/6e08v6/20170529_challenge_317_easy_collatz_tag_system/?st=j4lpnova&sh=e73e3ebe'''
#completed 7/1/17
#simple implementation of an explicit algorithm
def collatzTags(string):
    alphabet={'a':'bc','b':'a','c':'aaa'}
    while len(string)>1:
        string=string[2:]+alphabet[string[0]]
        print(string)

if __name__ == '__main__':
	collatzTags('aaa')