# Write a Python program to sort a list of elements using the insertion sort algorithm.
# Note: According to Wikipedia "Insertion sort is a simple sorting algorithm that builds 
# the final sorted array (or list) one item at a time. It is much less efficient on large
# lists than more advanced algorithms such as quicksort, heapsort, or merge sort."

def insertion_sort(array):
    for i in range(1, len(array)):
        current_value = array[i]
        index = i
        while index > 0 and array[index - 1] > current_value:
            temp = array[index - 1]
            array[index - 1] = current_value
            array[index] = temp
            index = index - 1
    return array

def solution(nlist):
    # course solution
    for index in range(1,len(nlist)):

     currentvalue = nlist[index]
     position = index

     while position>0 and nlist[position-1]>currentvalue:
         nlist[position]=nlist[position-1]
         position = position-1

     nlist[position]=currentvalue

if __name__ == '__main__':
    a = [14, 46, 43, 27, 57, 41, 45, 21, 70]
    print(insertion_sort(a))