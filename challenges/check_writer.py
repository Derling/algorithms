#!/usr/bin/env python3

'''
2017-09-06] Challenge #330 [Intermediate] Check Writer

src = https://www.reddit.com/r/dailyprogrammer/comments/6yep7x/20170906_challenge_330_intermediate_check_writer/

Given a dollar amount between 0.00 and 999,999.00, create a program that 
will provide a worded representation of a dollar amount on a check.

'''

numbers = { # map for numerical values
	0: '',
	1: 'one',
	2: 'two',
	3: 'three',
	4: 'four',
	5: 'five',
	6: 'six',
	7: 'seven',
	8: 'eight',
	9: 'nine',
	10: 'ten',
	11: 'eleven',
	12: 'twelve',
	13: 'thirteen',
	14: 'fourteen',
	15: 'fifteen',
	16: 'sixteen',
	17: 'seventeen',
	18: 'eighteen',
	19: 'nineteen',
	20: 'twenty',
	30: 'thirty',
	40: 'fourty',
	50: 'fifty',
	60: 'sixty',
	70: 'seventy',
	80: 'eighty',
	90: 'ninety',
}

def write_check(dollars, cents):
	check = ''
	thousands, hundreds = 0, 0
	if len(dollars) >= 3: # case where there are at least 100 dollars
		thousands = str(int(dollars)// 1000) # get the thousands places
		hundreds = str(int(dollars[len(dollars) - 3: len(dollars)])) # hundreds
		if len(thousands) == 3: # at least 100 thousand 
			check += numbers[int(thousands[0])] + ' hundred '
			if int(thousands[1:]) > 19: # ten and ones thousand places
				check += numbers[int(thousands[1:])//10 * 10] + ' ' \
					+ numbers[int(thousands[2])] + ' thousand, '
			else:
				check += numbers[int(thousands[1:])] + ' thousand, '

		elif len(thousands) == 2: # at least 10 thousand
			if int(thousands) > 19:
				check += numbers[int(thousands)//10 * 10] + ' ' \
					+ numbers[int(thousands[1])] + ' thousand, '
			else:
				check += numbers[int(thousands)] + ' thousand, '

		elif thousands != '0': # at least one thousand
			check += numbers[int(thousands)] + ' , and '

		check += numbers[int(hundreds) // 100] + ' hundred '
		if int(hundreds[1:]) > 19: # determine tens and ones places
			check += numbers[int(hundreds[1:])//10 * 10] + ' ' \
					+ numbers[int(hundreds[2])] + ' dollars and '
		else:
			check += numbers[int(hundreds[1:])] + ' dollars and '

	else: # range of dollars = 0 - 99
		if len(dollars) == 2:
			if int(dollars) > 19:
				check += numbers[int(dollars)//10 * 10] + ' ' \
					+ numbers[int(dollars[0])] + ' dollars and '
			else:
				check += numbers[int(dollars)] + ' dollars and '

		else:
			check += numbers[int(dollars[0])] + ' dollars and '

	if cents != '0':
		if int(cents) > 19:
			check += numbers[int(cents)//10 * 10] + ' ' \
				+ numbers[int(cents[1])] + ' cents.'
		else:
			check += numbers[int(cents)] + ' cents.'
	else:
		check += ' zero cents.'

	return check

if __name__ == '__main__':
	tests = [
		'333.88',
		'742388.15',
		'919616.12',
		'12.11',
		'2.0',
		'365920.97'
	]
	results = []

	for money in tests:
		dollars, cents = money.split('.')
		results.append(write_check(dollars, cents))

	for  i in range(len(tests)):
		print(
			'For the test', 
			tests[i], 
			'the results were', 
			results[i].capitalize(),
			end = '\n\n'
			)