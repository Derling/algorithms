"""
There are people sitting in a circular fashion,
print every third member while removing them,
the next counter starts immediately after the member is removed.
Print till all the members are exhausted.
For example:
Input: consider 123456789 members sitting in a circular fashion,
Output: 369485271
"""

def circular_counter(array, steps=1):
    # generator function that gets the ith element and removes it from 
    # the array and circles back around until there are no elements
    steps = steps- 1 # list index start at 0
    index = 0
    length = len(array)
    while array:
        index = (steps + index) % length
        yield array.pop(index)
        length = length - 1

if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in circular_counter(array, 3):
        print(i, end='')