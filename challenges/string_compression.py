
#!/usr/bin/env python3

'''
make a function that takes in a string and returns a shrinked version of the string. 
3 or more consecutive characters get  removed from the string. 
the function must also remove consequitive characters as the result of eliminating the previous characters.
'''

def str_compress(string):
	i, j = 0, 1

	def remove_sequence(i, n): # removes a character that starts at index i and appears n times
		while n:
			string.pop(i)
			n -= 1

	while j < len(string):
		if string[i] != string[j]:
			if j - i > 2:
				remove_sequence(i, j - i)
				i = 0
				j = 0
			else:
				i = j
		j += 1

	if string[i] == string[j - 1] and j - i > 2:
		remove_sequence(i, j - i)

	return ''.join(string)

def compress(string):
	if len(string) < 3:
		return string
	return str_compress(list(string))

if __name__ == '__main__':
	test = [
		'a', # compresses to "a"
		'aa', # compresses to "aa"
		'aaa', # compresses to ""
		'aaaaaaaaaaaaa', # compresses to ""
		'aaab', # compresses to "b"
		'baaabb', # compresses to ""
		'abccdddmmfffm' # compresses to "abcc"
	]
	for string in test:
		print(f'\"{string}\" compresses to \"{compress(string)}\"')