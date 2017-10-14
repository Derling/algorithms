# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 18:01:18 2017

@author: Derling

given a matrix, used to represent a maze, consisting of n by n points which 
containin 0s and 1s. find a way out of the maze by reaching the last vector in
the matrix

ie

0 0 0 0 0 1 <- entry points
0 1 1 1 0 1
0 0 0 1 1 1
0 0 1 1 0 1
0 0 1 0 0 0 <- exit points

input is a 2d array for above example it would be something like:
matrix = [
        [0, 0, 0, 0, 0, 1],
        [0, 1, 1, 0, 0, 1],
        [0, 0, 0, 1, 1, 1],
        [0, 0, 1, 1, 0, 1],
        [0, 0, 1, 0, 0, 0]
    ]

entry points are not given or none at start of program.

return true if it possible to reach the last row, return false if not possible
"""

def evaluate_maze(matrix):
    entry_points = matrix[0]
    for point in range(len(entry_points)):
        if entry_points[point]:
            if evaluate_point(matrix, point):
                return True
    return False

results = []

def evaluate_point(matrix, index, row=0, last_row=-1,last_index=0):
    # base case, we made it to the end of the maze
    if row == len(matrix) - 1:
        return True
    
    if last_row <= row and matrix[row + 1][index]:
        print('going down')
        results.append(evaluate_point(matrix, index, row + 1, row, index))
        
    if row != 0 and last_row >= row and matrix[row - 1][index]:
        print('going up')
        results.append(evaluate_point(matrix, index, row - 1, row, index))
    
    if index != len(matrix[row]) - 1 and last_index != index + 1 and \
        matrix[row][index + 1]:
        print('moving right')
        results.append(evaluate_point(matrix, index + 1, row, row, index))
        
    if index != 0 and last_index != index - 1 and \
        matrix[row][index -1:]:
        print('moving left')
        results.append(evaluate_point(matrix, index - 1, row, row, index))
    return any(results)
