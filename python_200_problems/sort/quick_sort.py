# Write a Python program to sort a list of elements using the quick sort algorithm.
# Note : According to Wikipedia "Quicksort is a comparison sort, meaning that it can 
# sort items of any type for which a "less-than" relation (formally, a total order) is defined. 
# In efficient implementations it is not a stable sort, meaning that the relative order of equal 
# sort items is not preserved. Quicksort can operate in-place on an array, requiring small additional
# amounts of memory to perform the sorting."

def quick_sort(array, low, high):
    # helper method
    def partition(arr, low, high):
        for i in range(low, high):
            if array[i] <= array[high]:
                array[low], array[i] = array[i], array[low]
                low = low + 1
        array[low], array[high] = array[high], array[low]
        return low
    if low < high:
        pivot = partition(array, low, high)
        quick_sort(array, low, pivot - 1)
        quick_sort(array, pivot + 1, high)
    return array

''' 

# course solution
def quickSort(data_list):
   quickSortHlp(data_list,0,len(data_list)-1)

def quickSortHlp(data_list,first,last):
   if first < last:

       splitpoint = partition(data_list,first,last)

       quickSortHlp(data_list,first,splitpoint-1)
       quickSortHlp(data_list,splitpoint+1,last)


def partition(data_list,first,last):
   pivotvalue = data_list[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and data_list[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while data_list[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = data_list[leftmark]
           data_list[leftmark] = data_list[rightmark]
           data_list[rightmark] = temp

   temp = data_list[first]
   data_list[first] = data_list[rightmark]
   data_list[rightmark] = temp


   return rightmark

'''

if __name__ == '__main__':
    array = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print('The sorted array is {}'.format(quick_sort(array, 0, len(array) - 1)))