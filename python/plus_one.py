# Given a non-negative number represented as an array of digits,
# plus one to the number.

# The digits are stored such that the most significant
# digit is at the head of the list.

def plus_one(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] = digits[i] + 1
            return digits
        digits[i] = 0
    digits.insert(0, 1)
    return digits

if __name__ == '__main__':
    n = input('Enter a number:')
    digits = [int(i) for i in n]
    print(plus_one(digits))

'''
start from end of array and add 1
if that number is 9 then we make that element 0 and add 1 to the next element
finally if it cycles through all the digits in the array instert a 1 at the 0th
index making it the new significant digit
'''