'''
[2017-11-13] Challenge #340 [Easy] First Recurring Character
src = https://www.reddit.com/r/dailyprogrammer/comments/7cnqtw/20171113_challenge_340_easy_first_recurring/

Write a program that outputs the first recurring character in a string.

											* * * Bonus(Completed) * * * 
Return the index (0 or 1 based, but please specify) where the original character is found in the string.
'''

def first_recurring_char(string):
	# challenge completed, using zero based indexing
	chars = {}
	for index, c in enumerate(string):
		if c in chars: # we've seen this char so return the index and the char
			return (chars[c], c)
		else: # first time seeing this char, add it to map
			chars[c] = index
	return None

if __name__ == '__main__':
	challenge_input = [
		'IKEUNFUVFV',
		'PXLJOUDJVZGQHLBHGXIW',
		'*l1J?)yn%R[}9~1"=k7]9;0[$',
	]
	for index, string in enumerate(challenge_input):
		print('challenge', index + 1, 'results:',first_recurring_char(string))
