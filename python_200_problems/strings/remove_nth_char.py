# Write a Python program to remove the nth index character from a nonempty string

def remove_nth_char(word, n):
    return ''.join([word[c] for c in range(len(word)) if c != n])

def solution(string, n):
    # course solution
     first_part = string[:n] 
     last_pasrt = string[n+1:]
     return first_part + last_pasrt

if __name__ == '__main__':
    print(remove_nth_char('string', 2))
    print(remove_nth_char('Python', 0))
    print(remove_nth_char('Python', 3))
    print(remove_nth_char('Python', 5))