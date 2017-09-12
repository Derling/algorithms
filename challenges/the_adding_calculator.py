#[2017-09-11] Challenge#331 [Easy] The Adding Calculator

def adding_calculator(int1, int2, operand):
	if operand == '+':
		return int1 + int2
	else if operand == '-':
		return int1 + -int2
	else if operand == '^':
		return power_addition(int1, int2)
	else if operand == '*':
		return multiplication_addition(int1, int2)

def multiplication_addition(int1, int2):
	total = 0
	for n in range(int2):
		total += int1
	return total 

def power_addition(int1, int2):
	return 

if __name__ == '__main__':
	int1, int2, operand = input('Enter the two integers followed'
					   ' by the operand').split()
	print(adding_calculator(int(int1), int(int2), operand))