#!/usr/bin/env python
'''
HackerRank Challenge I found useful
Differnces of diagonals in a n x n matrix
completed 7/3/17
'''


def diagonalDiff(integers):
	#variable for top left to bottom right sums
	lsum = 0
	#variable for top right to bottom left sums
	rsum = 0
	for i in range(len(integers)):
		lsum += integers[i][i]
		rsum += integers[i][len(integers)-i-1]
	return abs(lsum - rsum)
if __name__ == '__main__':
	#input for n x n matrix
	n = int(input())
	matrix = []
	print('Please enter the elements in the matrix as string using (\' \') :')
	for i in range(n):
		temp = [int(temp) for temp in input().split(' ')]
		matrix.append(temp)
	print('Diagonal Differences: ' , diagonalDiff(matrix))
