'''
HackerRank Challenge
Beautiful days are described as days that divide evenly into an integer. 
The day must first be subtracted by its reverse ie 21 and 12.
Then if the difference of the day evenly divides into k then it is a beautiful day.
Input is one line describing i,j,k each seperated by a space not commas.
The set is the numbers between i and j, inclusive. 
The output is the number of "Beautiful Days".
7/6/17 challenge.
'''

def main():
    i,j,k = getInput()
    beautiful_days = getDays(i,j,k)
    print(beautiful_days)
def getInput():
    return map(int,input().split())
def getDays(i,j,k):
    count = 0
    for day in range(i,j+1):    
        if abs(day-getReverse(day))%k == 0:
            count += 1
    return count
def getReverse(integer):
    return int(str(integer)[::-1])
if __name__ == '__main__': 
    main()