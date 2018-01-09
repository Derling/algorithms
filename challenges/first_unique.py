'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
'''

from collections import OrderedDict

class Solution(object):
    def first_uniq_char(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = OrderedDict()
        for i, v in enumerate(s):
            last_data = d.get(v, [i, 0])
            last_data[1] = last_data[1] + 1
            d[v] = last_data
        for k, v in d.items():
            if v[1] == 1:
                return v[0]
        return -1

if __name__ == '__main__':
    s = "leetcode"
    x = Solution()
    print(x.first_uniq_char(s))
    s = "loveleetcode"
    print(x.first_uniq_char(s))

'''
OrderedDict keeps track of the order in which the keys and values were entered

Values for the keys(characters) are arrays of size 2 which keep the
character index and the number of times they appear in the string.
'''