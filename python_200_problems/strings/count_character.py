# Write a Python program to count the number of characters (character frequency) in a string.
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

def count_character(string):
    count = {}
    for c in string:
        count[c] = count.get(c, 0) + 1
    return count

def solution(string):
    # course solution
    dict = {}
    for n in string:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

if __name__ == '__main__':
    print(count_character('google'))