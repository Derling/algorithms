'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
'''

def find_needle(haystack, needle):
    try:
        index = haystack.index(needle)
        return index
    except ValueError:
        return -1

if __name__ == '__main__':
    t1 = "hello", "ll"
    t2 = "aaaaa", "bba"
    print(find_needle(*t1))
    print(find_needle(*t2))