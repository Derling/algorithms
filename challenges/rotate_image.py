#!/usr/bin/env python3
'''
given an n by n matrix representing an image 
create a function that rotates it 90 degrees

example:
image = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]
rotated = [
	[7, 4, 1],
	[8, 5, 2],
	[9, 6, 3]
]
'''


def rotate_image(image):
	rotated_image = []
	for i in range(len(image)):
		row = []
		for j in range(len(image) - 1, -1, -1):
			row.append(image[j][i])
		rotated_image.append(row)
	return rotated_image

if __name__ == '__main__':
	test = [
		[1, 2, 3],
		[4, 5, 6],
		[7, 8, 9],
	]
	print(rotate_image(test))