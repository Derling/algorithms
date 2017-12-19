# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 13:52:38 2017

@author: DerlingB
"""

# Count the number of even and odd numbers from a series of numbers
# Input 
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
# Output
# Number of even numbers : 4                                                                                    
# Number of odd numbers : 5 

def count_evens_odds(numbers):
    evens = odds = 0
    for n in numbers:
        if n % 2 == 0:
            evens = evens + 1
        else:
            odds = odds + 1
    return evens, odds

def solution():
    # course solution
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
    count_odd = 0
    count_even = 0
    for x in numbers:
        if not x % 2:
    	     count_even+=1
        else:
    	     count_odd+=1
                
    print("Number of even numbers :",count_even)
    print("Number of odd numbers :",count_odd)

if __name__ == '__main__':
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    evens, odds = count_evens_odds(numbers)
    print('Number of even numbers : {0}\n'
          'Number of odd numbers : {1}'.format(evens, odds))