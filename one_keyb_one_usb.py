#!/usr/bin/env python
'''HackerRank Challenge
Monica wants to buy exactly one keyboard and one USB drive from her favorite electronics store. 
The store sells  different brands of keyboards and  different brands of USB drives. 
Monica has exactly  dollars to spend, and she wants to spend as much of it as possible 
(i.e., the total cost of her purchase must be maximal).
Given the price lists for the store's keyboards and USB drives, 
find and print the amount money Monica will spend. 
If she doesn't have enough money to buy one keyboard and one USB drive, 
print -1 instead. 
'''

import sys

def getMoneySpent(keyboards, drives, s):
    # Complete this function
    total = 0
    for k in keyboards:        
        for d in drives:
            temp = k + d
            if temp > total and temp <= s:
                total = temp
    return -1 if total == 0 else total

if __name__ == '__main__':
	# s = salary n = number of keyboards m = number of usb devices
	s,n,m = input().strip().split(' ')
	s,n,m = [int(s),int(n),int(m)]
	keyboards = list(map(int, input().strip().split(' ')))
	drives = list(map(int, input().strip().split(' ')))
	#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
	moneySpent = getMoneySpent(keyboards, drives, s)
	print(moneySpent)
