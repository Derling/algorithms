# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 18:08:01 2017

@author: DerlingB
"""

# Write a Python program to convert an integer to a roman numeral.
# Input 1, 4000
# Output I, MMMM

values = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

class Int_Converter():
    def convert_to_roman(self,integer):
        roman = ''
        for n, numeral in values:
            '''
                take each roman numeral value and find how many times
                it would appear in the roman numeral presentation
                by subtracting away the nth place value based on the
                roman numeral
            '''
            while integer >= n:
                roman = roman + numeral
                integer = integer - n
        return roman
    
class py_solution:
    # course solution
    def int_to_Roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            print(num, i)
            for _ in range(num // val[i]):
                roman_num += syb[i]
                print(roman_num, i, num)
                num -= val[i]
            i += 1
        return roman_num


if __name__ == '__main__':
    class_ = Int_Converter()
    inputs = [
            1,
            4000,
            21311,
            982,
            544
        ]
    for i in inputs:
        print(class_.convert_to_roman(i))