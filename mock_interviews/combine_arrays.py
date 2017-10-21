#!/usr/bin/env python3.6

'''
Given two arrays combine the elements of the two arrays such that all
elements of the two arrays are in the new array. 

example:

x = ["dim", "lit", "pop", "extra", "..."]
y = ["min", "lit", "pop", "soap", "plore", "lore"]

the combination would look somehting like this: ["dim", "min", "lit", "lit",..]

output must resemble the above example.

assume both arrays will not always be the same size.

extra challenge: make it so that there are no repeated elements in the combination of the two arrays.

'''

def combine(x, y):
	combination = []
	smallest_len = 0
	if len(x) > len(y):
		smallest_len = len(y)
	else:
		smallest_len = len(x)
	for i in range(smallest_len):
		combination.append(x[i])
		combination.append(y[i])
	if len(x) == smallest_len:
		combination.extend(y[smallest_len: len(y)])
	else:
		combination.extend(x[smallest_len: len(x)])
	return combination

def combine_uniques(x, y):
	combination = []
	smallest_len = 0
	if len(x) > len(y):
		smallest_len = len(y)
	else:
		smallest_len = len(x)
	for i in range(smallest_len):
		if x[i] not in combination:
			combination.append(x[i])
		if y[i] not in combination:
			combination.append(y[i])
	if len(x) == smallest_len:
		for i in range(smallest_len, len(y)):
			if y[i] not in combination:
				combination.append(y[i])
	else:
		for i in range(smallest_len, len(x)):
			if x[i] not in combination:
				combination.append(x[i])
	return combination

if __name__ == '__main__': # script uses python 3.6 syntax 
	y = ["dim", "lit", "pop", "extra", "..."]
	x = ["min", "lit", "pop", "soap", "plore", "lore", "extra", "extra"]
	print(f'normal combination = {combine(x,y)}', end='\n\n')
	print(f'unique elements combination = {combine_uniques(x, y)}')
