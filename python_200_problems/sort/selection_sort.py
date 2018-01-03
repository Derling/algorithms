# Write a Python program to sort a list of elements using the selection sort algorithm.
# Note : The selection sort improves on the bubble sort by making only one exchange for every pass through the list.

def selection_sort(array):
    last_switch = len(array) - 1
    while last_switch:
        current_largest = array[0]
        index = 0
        for i, v in enumerate(array[:last_switch + 1]):
            if v > current_largest:
                current_largest = v
                index = i
        array[last_switch], array[index] = current_largest, array[last_switch]
        last_switch = last_switch - 1
        print(array)
    return array


def solution(nlist):
    # course solution
    for fillslot in range(len(nlist)-1,0,-1):
        maxpos=0
        for location in range(1,fillslot+1):
            if nlist[location]>nlist[maxpos]:
                maxpos = location
        temp = nlist[fillslot]
        nlist[fillslot] = nlist[maxpos]
        nlist[maxpos] = temp

if __name__ == '__main__':
    array = [29, 72, 98, 20, 87, 66, 52, 51, 36]
    print(selection_sort(array))