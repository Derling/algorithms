#!/usr/bin/env python3
#[2017-09-11] Challenge#331 [Easy] The Adding Calculator

def adding_calculator(int1, int2, operand):
	if operand == '+':
		return int1 + int2
	elif operand == '-':
		return int1 + -int2
	elif operand == '^':
		return power_addition(int1, int2)
	elif operand == '*':
		return multiplication_addition(int1, int2)
	elif operand == '/':
		return divide_addition(int1, int2)

def multiplication_addition(int1, int2):
	total = 0
	for n in range(int2):
		total += int1
	return total 

def power_addition(integer, power):
	total = 0
	for n in range(power):
		total += multiplication_addition(integer, integer)
	return total

def divide_addition(divident, divisor):
	total = 0
	current = 0 
	while current < divident:
		current += divisor
		total += 1
	return total if current%divisor == 0 else 'Non-integral answer'

if __name__ == '__main__':
	int1, int2, operand = input('Enter the two integers followed'
					   ' by the operand\n').split()
	print(adding_calculator(int(int1), int(int2), operand))