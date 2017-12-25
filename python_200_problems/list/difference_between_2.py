# Write a Python program to get the difference between the two lists
# Input 
# list1 = [1, 2, 3, 4]
# list2 = [1, 2]
# Output
# [3,4]

def difference_between_2_lists(array1, array2):
    diff1 = [i for i in array1 if i not in array2]
    diff2 = [i for i in array2 if i not in array1]
    return diff1 + diff2

def solution():
    # course solution
    list1 = [1, 2, 3, 4]
    list2 = [1, 2]
    print(list(set(list1) - set(list2)))

if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    list2 = [1, 2]
    print(difference_between_2_lists(list1, list2))