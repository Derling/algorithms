# Write a Python program to get the smallest number from a list.
# max_num_in_list([1, 2, -8, 0])
# return 2

def find_max(iterable):
    # easiest way to do it
    return max(iterable)

def get_max(array):
    current_max = array[0]
    for i in array:
        if i > current_max:
            current_max = i
    return current_max

def max_num_in_list( list ):
    # course solution
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max

if __name__ == '__main__':
    array = [1, 2, -8, 0]
    print(get_max(array))