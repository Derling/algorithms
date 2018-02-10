'''
	[2017-11-21] Challenge #341 [Easy] Repeating Numbers
	src: https://www.reddit.com/r/dailyprogrammer/comments/7eh6k8/20171121_challenge_341_easy_repeating_numbers/
'''

def repeating_numbers(digits):
	numbers = {} # used to keep track of all the times a sequence of number is repeated
	digits = str(digits)
	
	for index, digit in enumerate(digits):
		current = index + 1
	
		while current < len(digits):
			# add the digits that follow the current digit
			digit = digit +  digits[current] 
			# add new digit to hash table or increment key by 1
			numbers[digit] = numbers.get(digit, 0) + 1
			# go to next digit
			current = current + 1

	results = {} # new hash table that will be populated with digits that appear more than once

	for digit, repeats in numbers.items():
		if repeats > 1:
			results[digit] = repeats
	
	return results

if __name__ == '__main__':
	tests = [
		82156821568221,
		11111011110111011,
		98778912332145,
		124489903108444899,
	]
	for num in tests:
		results = repeating_numbers(num)
		if results:
			print(results)
		else:
			print(0)
