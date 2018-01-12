
#!/usr/bin/env python3

'''
make a function that takes in a string and returns a shrinked version of the string. 
3 or more consecutive characters get  removed from the string. 
the function must also remove consequitive characters as the result of eliminating the previous characters.
'''

def compress(string):
	if len(string) < 3:
		return string
	i, j = 0, 1
	string = list(string)
	while j < len(string):
		if string[i] != string[j]:
			if j - i >= 2:
				string[i:] = string[j:]
				i = 0
				j = 0
		j += 1
	if string[i] == string[j - 1] and j - i >= 2:
		string[i:] = string[j:]
	return ''.join(string)

if __name__ == '__main__':
	test = [
		'a', # compresses to "a"
		'aa', # compresses to "aa"
		'aaa', # compresses to ""
		'aaaaaaaaaaaaa', # compresses to ""
		'aaab', # compresses to "b"
		'baaabb', # compresses to ""
	]
	for string in test:
		print('"{0}"" compressed is "{1}"'.format(string, compress(string)))