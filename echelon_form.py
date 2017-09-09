# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 16:45:56 2017

Linear Algebra challenge
Reducing a linear system to its echelon form represented in a matrix.
Personal Challenge from school.
*** Not complete *** 

@author: Derling
"""

def echelon_form(matrix):
    ''' rhou reduction '''
    echelon = []
    for index, m in enumerate(matrix):
        echelon.append(simplify_top_row(m, index))
        for row in range(index + 1, len(matrix)):
            matrix[row] = simplify_row(matrix[row], m, index)
    return echelon

def simplify_row(current, last, position):
    ''' make everything before the position a 0 '''
    if current[position] < 0:
        return list(map(lambda i: i[1] + (last[i[0]] * current[position]),
                        enumerate(current)))
    return list(map(lambda i: i[1] - (last[i[0]] * current[position]),
                    enumerate(current)))

def simplify_top_row(row, leader):
    ''' reduce nth item in nth row to 1 '''
    return list(map(lambda i: i/row[leader], row))

if __name__ == '__main__':
    n = int(input("enter the number of equations:"))
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    print(echelon_form(matrix))
