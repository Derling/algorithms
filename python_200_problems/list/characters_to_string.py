# ---------------------------------------------------------------
# python best courses https://courses.tanpham.org/
# ---------------------------------------------------------------
# Convert a list of characters into a string
# Input ['a', 'b', 'c', 'd']
# Output abcd

def characters_to_str(chars):
    return ''.join(chars)

def solution():
    # course solution
    s = ['a', 'b', 'c', 'd']
    str1 = ''.join(s)
    print(str1)

if __name__ == '__main__':
    test = ['a', 'b', 'c', 'd']
    print(characters_to_str(test))