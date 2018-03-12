def str_to_bin(string):
	conversions = []
	for char in string:
		ascii_number = ord(char)
		conversions.append(bin(ascii_number)[2:])
	return ' '.join(conversions)

if __name__ == '__main__':
	print(str_to_bin('geeks'))
	print(str_to_bin('GFG'))
	print(str_to_bin('python'))
	