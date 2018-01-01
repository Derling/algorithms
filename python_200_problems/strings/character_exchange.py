#  Write a Python program to change a given string to a new string where the first and last chars have been exchange

def character_exchange(string):
    chars = [c for c in string]
    chars[0], chars[-1] = chars[-1], chars[0]
    return ''.join(chars)

def solution(string):
    # course solution
    return string[-1:] + string[1:-1] + string[:1]

if __name__ == '__main__':
    s = 'string'
    print(character_exchange(s))