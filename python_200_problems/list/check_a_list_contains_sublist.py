# Write a Python program to check whether a list contains a sublist.
# Input
# a = [2,4,3,5,7]
# b = [4,3]
# c = [3,7]
# print(is_Sublist(a, b))
# print(is_Sublist(a, c))
# Output


def check_sublist(array, subarray):
    if len(subarray) > len(array):
        return False
    if subarray == []:
        return True
    start_count = array.count(subarray[0])
    start_index = 0
    while start_count:
        start_index = array.index(subarray[0], start_index)
        subarray_len = 0
        for s, i in enumerate(range(start_index, start_index + len(subarray))):
            if i == len(array):
                break
            else:
                if subarray[s] == array[i]:
                    subarray_len = subarray_len + 1
                else:
                    break
        if subarray_len == len(subarray):
            return True
        start_index = start_index + 1
        start_count = start_count - 1
    return False

def is_Sublist(l, s):
    # course solution
	sub_set = False
	if s == []:
		sub_set = True
	elif s == l:
		sub_set = True
	elif len(s) > len(l):
		sub_set = False

	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = 1
				while (n < len(s)) and (l[i+n] == s[n]):
					n += 1
				
				if n == len(s):
					sub_set = True

	return sub_set

if __name__ == '__main__':
    a = [2, 4, 3, 5, 7]
    b = [4, 3]
    c = [3, 7]
    print(check_sublist(a, b))
    print(check_sublist(a, c))