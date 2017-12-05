'''
	Imagine we have an image. we'll represent this image as a simle 2d array,
	where every pixel is a 1 or 0. 

	The image you get is known to have N >= 0 rectangles of 0s on a background of 1s. 
	Write a function that takes an image in an outputs an array of the coordinates for each rectangle.
'''

def get_rectangles(image):
	rectangles = []
	for row in range(len(image)):
		for col in range(len(image[row])):
			if image[row][col] == 0:
				rectangle = [row, col] # add top left corner of rectangle to an array
				while row < len(image) - 1: # look for the height of the rectangle
					if image[row + 1][col] == 0:
						row += 1
					else:
						break
				while col < len(image[row]) - 1: # look for the width of the rectangle
					if image[row][col + 1] == 0:
						col += 1
					else:
						break
				# append bottom right end points
				rectangle.append(row)
				rectangle.append(col)
				rectangles.append(rectangle)
				''' turn the points of the newly found rectangle into 1s so that 
					we do not go through them again as we go down the 2d array '''
				for i in range(rectangle[0], row + 1):
					for j in range(rectangle[1], col + 1):
						image[i][j] = 1
	return rectangles

if __name__ == '__main__':
	test = [
		[1, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 0, 0, 0, 1],
		[1, 0, 1, 0, 0, 0, 1],
		[1, 0, 1, 1, 1, 1, 1],
		[1, 0, 1, 0, 0, 1, 1],
		[1, 1, 1, 0, 0, 1, 1],
		[1, 1, 1, 1, 1, 1, 1]
	] # ouptut = [[2, 3, 3, 5], [3, 1, 5, 1], [5, 3, 6, 4]]
	print(get_rectangles(test))
