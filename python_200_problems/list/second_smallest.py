# Write a Python program to find the second smallest number in a list.
# input
# second_smallest([1, 2, -8, -2, 0])
# output
# -2

def second_smallest(array):
    first, second = float('inf'), float('inf')
    for i in array:
        if i < first:
            first, second = i, first
        elif i < second:
            second = i
    return second

def solution(numbers):
    # course solution
    a1, a2 = float('inf'), float('inf')
    for x in numbers:
        if x <= a1:
            a1, a2 = x, a1
        elif x < a2:
            a2 = x
    return a2

print(second_smallest([1, 2, -8, -2, 0]))

if __name__ == '__main__':
    print(second_smallest([1, 2, -8, -2, 0]))