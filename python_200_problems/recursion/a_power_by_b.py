# Write a Python program to calculate the value of 'a' to the power 'b'.

def a_power_by_b(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    return a * a_power_by_b(a, b -1)

def power(a,b):
	if b==0:
		return 1
	elif a==0:
		return 0
	elif b==1:
		return a
	else:
		return a*power(a,b-1)

if __name__ == '__main__':
    print(a_power_by_b(3, 4))