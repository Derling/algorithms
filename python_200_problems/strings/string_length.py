# Write a Python program to calculate the length of a string.

def string_length(string):
    count = 0
    for _ in string:
        count = count + 1
    return count

def solution(string):
    # course solution
    count = 0
    for char in string:
        count += 1
    return count

if __name__ == '__main__':
    print(string_length("hello world"))