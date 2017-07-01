#src=https://www.reddit.com/r/dailyprogrammer/comments/69y21t/20170508_challenge_314_easy_concatenated_integers/?st=j4lrpdmz&sh=f46d2d86
#Concatenated Integers challenge
#decided to do it recursively
#personal notes:much harder than I thought it was going to be. Challenge unfairly labeled "Easy".

def concatenateRecursively(integers):
	return smallestNumber(integers.split()),largestNumber(integers.split())
def largestNumber(data):
	largest = ""
	while(data):
		next = max(data)
		largest += str(next)
		data.remove(next)
	return largest
def smallestNumber(data):
	smallest = ""
	while(data):
		next = min(data)
		smallest += str(next)
		data.remove(next)
	return smallest
if __name__ == '__main__':
	print('{0[0]},{0[1]}'.format(concatenateRecursively('79 82 34 83 69')))
	print('{0[0]},{0[1]}'.format(concatenateRecursively('420 34 19 71 341')))
	print('{0[0]},{0[1]}'.format(concatenateRecursively('17 32 91 7 46')))