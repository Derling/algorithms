'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
'''

def is_palindrome(s):
        """
        :type s: str
        :rtype: bool
        """
        if not len(s):
            return True
        stripped_s = ''.join(str(s).lower().split())
        s = [i for i in stripped_s if str(i).isalnum()]
        return s[::-1] == s

if __name__ == '__main__':
    str1 = 'race car'
    str2 = 'race a car'
    str3 = 'A man, a plan, a canal: Panama'
    print(is_palindrome(str1)) # True
    print(is_palindrome(str2)) # False
    print(is_palindrome(str3)) # True

'''
isolate the alpha numeric characters from the string into an array
then check if the array is equivalent to the reversed version of itself
'''