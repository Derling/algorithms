# Write a Python program to get the factorial of a non-negative integer. 

def fractorial(n):
    if n <= 1:
        return 1
    return n * fractorial(n - 1)

def solution(n):
    # course solution
    if n <= 1:
        return 1
    else:
        return n * (solution(n - 1))

if __name__ == '__main__':
    print(fractorial(5))