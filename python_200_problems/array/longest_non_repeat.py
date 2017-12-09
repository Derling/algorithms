# ---------------------------------------------------------------
# python best courses https://courses.tanpham.org/
# ---------------------------------------------------------------
# Challenge
# 
# Given a string, find the length of the longest substring
# without repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3.
# ---------------------------------------------------------------

def longest_non_repeat(string):
    max_length = 0 
    
    for i, c in enumerate(string):
        
        sub_str = [] # current sub string
        
        while(i < len(string) and (string[i] not in sub_str)):
            # check if we haven't seen the character before
            sub_str.append(string[i])
            i = i + 1
        
        if len(sub_str) > max_length:
            max_length = len(sub_str)
            
    return max_length

def longest_substring(string):
    i=0
    max_length = 1

    for i,c in enumerate(string):
        
        start_at = i
        sub_str=[]

        # continue increase sub string if did not repeat character         
        while (start_at < len(string)) and (string[start_at] not in sub_str):
            sub_str.append(string[start_at])
            start_at = start_at + 1

        # update the max length   
        if len(sub_str) > max_length:
            max_length = len(sub_str)

        print(sub_str)
        
    return max_length

if __name__ == '__main__':
    tests = ['abcabcbb',
             'bbbbb',
             'pwwkew',
             ]
    for string in tests:
        print(longest_non_repeat(string))