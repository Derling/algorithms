''''
HackerRank Challenge
Beautiful days are described as days that divide evenly into an integer. 
The day must first be subtracted by its reverse ie 21 and 12.
Then if the difference of the day evenly divides into k then it is a beautiful day.
Input is one line describing i,j,k each seperated by a space not commas.
The set is the numbers between i and j, inclusive. 
The output is the number of "Beautiful Days".
7/6/17 challenge.
'''

def get_reverse(day):
    '''
    type day: int
    rtype: int
    '''
    return int(str(day)[::-1])

def beautiful_days(lower, upper, divisor):
    '''
    type lower: int
    type upper: int
    type divisor: int
    rtype: int
    '''
    count = 0
    for day in range(lower, upper + 1):
        difference = day - get_reverse(day)
        if difference % divisor == 0:
            count += 1
    return count

if __name__ == '__main__': 
    tests = [
        [20, 30, 2],
        [20, 30, 3],
        [20, 30, 4]
    ]
    for i in tests:
        print(beautiful_days(*i))
