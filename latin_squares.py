#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 04:39:38 2017

@author: Derling

r/dailyprogrammer [7-08-21] Challenged #328 [Easy] Latin Squares

"""

def latin_squares(n,arr):
    base_numbers = arr[:n]
    matrix = []
    # create n x n grid using arr from left to right
    for i in range(n):
        matrix.append(arr[i * n : n * (i + 1)])
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            # check how many times a number appears in a row, if its more than
            # once, its not a latin square also if a number appears only on one
            # row then it is not a latin square. 
            if (matrix[i].count(matrix[i][j]) > 1 or 
                    matrix[i] not in base_numbers):
                return False
            # check if the first number of our current row occurs more than
            # once, if it does its not a latin square 
            if matrix[i][0] == matrix[j][0] and j != i: 
                return False                           
    return True
        

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(latin_squares(n,arr))