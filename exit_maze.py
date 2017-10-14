# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 16:59:17 2017

@author: Derling


Exit The Maze

given a matrix of 0s and 1s determine if it is possible to reach the last row
starting from the first row

ie

0 0 0 0 0 1 <- start points
1 0 0 0 1 1
1 1 1 0 0 1
0 0 1 1 1 1
0 1 0 0 1 0
0 1 1 1 1 0
0 0 1 0 0 0 <- reach here to exit


in the above example the only accurate way to exit would be to start at the 
entry point, move down three times, move left once, move down twice, move left
three times, then finally move down

write a program that determines whether or not it is possible to exit

input is a 2d array ie [[0, 0, 0, 0, 1], [1, 1, 1, 1, 1,], [0, 0, 0, 0, 0]]
"""

def find_exit(matrix):
    entry_points = matrix[0]
    for point in range(len(entry_points)):
        if entry_points[point]:
            if evaluate_point(matrix, point):
                print('found the way out')
                return True
    return False


def evaluate_point(matrix, index, row=0, last_row=-1, last_index=0):
    if row == len(matrix) - 1: # we are at the last row, we exited
        print('you can exit')
        return True
    
    # if our last action wasn't to go up and we can go down, then lets go down
    if last_row < row and matrix[row + 1][index]:
        print(f'going down from row: {row}')
        return evaluate_point(matrix, index, row + 1, row, index)
    
    # if oour last action wasn't to go down and we can go up, then lets go up
    if row > 0 and matrix[row - 1][index] and last_row > row:
        return evaluate_point(matrix, index, row - 1, row, index)
    

if __name__ == '__main__':
    matrix = [
            [0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 1],
            [1, 1, 1, 0, 1, 0],
            ]
    print(find_exit(matrix))