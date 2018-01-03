# Write a Python program to sort a list of elements using the bubble sort algorithm.
# Note : According to Wikipedia "Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that
# repeatedly steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the 
# wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted. 
# The algorithm, which is a comparison sort, is named for the way smaller elements "bubble" to the top of the list. 
# Although the algorithm is simple, it is too slow and impractical for most problems even when compared to insertion sort. 
# It can be practical if the input is usually in sort order but may occasionally have some out-of-order elements nearly 
# in position.

def bubble_sort(array):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(array)):
            if array[i] < array[i - 1]:
                temp = array[i]
                array[i] = array[i - 1]
                array[i - 1] = temp
                swapped = True
    return array

def solution(nlist):
    # course solution
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp

if __name__ == '__main__':
    array1 = [98, 22, -33, 9, 0, 22, 11, 5]
    print(bubble_sort(array1))
    array2 = [14, 46, 43, 27, 57, 41, 45, 21, 70]
    print(bubble_sort(array2))