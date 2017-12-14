# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 17:50:01 2017

@author: DerlingB
"""

# Write a Python class to convert a roman numeral to an integer

# Sample input
# 'MMMCMLXXXVI'
# 'MMMM'
# 'C'

# Sample output
# 3986                                                                                                          
# 4000                                                                                                          
# 100

values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }

class Numeral_Converter():
    def convert_to_int(self, roman_numeral):
        # hash table for the values of the individual roman numerals
        total = 0
        
        for index, numeral in enumerate(roman_numeral):
            # check if the current numeral is less than the numeral
            # that follows it, if so subtract the current numerals value
            if (index < len(roman_numeral) - 1 and 
                values[numeral] < values[roman_numeral[index + 1]]):
                total = total - values[numeral]
            else:
                total = total + values[numeral]

        return total

class py_solution:
    # course solution
    def roman_to_int(self, s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val


if __name__ == '__main__':
    inputs = ['MMMCMLXXXVI',
              'MMMM',
              'C',
              'CD',
              'D']
    class_ = Numeral_Converter()
    for i in inputs:
        print(class_.convert_to_int(i))