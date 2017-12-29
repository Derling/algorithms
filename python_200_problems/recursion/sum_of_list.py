# Write a Python program to calculate the sum of a list of numbers. (in recursion fashion)

def sum_of_list(array):
    if len(array) == 1:
        return array[0]
    return array[0] + sum_of_list(array[1:])

def solution(num_List):
    # course solution
    if len(num_List) == 1:
        return num_List[0]
    else:
        return num_List[0] + solution(num_List[1:])



if __name__ == '__main__':
    array = [2, 4, 5, 6, 7]
    print(sum_of_list(array))