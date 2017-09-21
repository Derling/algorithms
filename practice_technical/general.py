# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 07:47:26 2017

@author: Derling
"""

def frequent_integers(integers): # procedual 
    # 1.Find the most frequent integer in an array
    count = {} # instantiate a dict, also known as a hashmap
    for i in integers:
        # get return the value for the key, if not in the dict set value to 0
        count[i] = count.get(i, 0) + 1 # increment the value for the int by 1
    most = (0, 0)
    for k, v in count.items():
        if v > most[1]:
            most = (k, v)
    return most

def functional_frequent_integers(integers):# functional
    # 1.Find the most frequent integer in an array
    from collections import Counter
    c = Counter(integers)
    most = max(c.values())
    return (list(c.keys())[list(c.values()).index(most)], most)
        

def sum_of_10_pairs(integers):# procedual
    # 2.Find pairs in an integer array whose sum is equal to 10
    pairs = []
    for i in integers:
        if 10 - i in integers:
            pairs.append((i, 10 - i))
    return pairs

def sum_of_10_pairs_2(integers):# functional
    return set((i, 10 - i) for i in integers if 10 -i in integers)

def rotated_arrays_1(first, second): # functional
    # 3. given 2 arrays find out if one is the rotated version of the other
    return True if sorted(first) == sorted(second) else False

def fibonacci_recursive(n):
    # 4. Fibonacci sequence
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n -1) + fibonacci_recursive(n- 2)

def fibonacci(n):
    # 4. Fibonacci sequence
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a

def rotated_arrays_2(first, second): # procedual
    # 3. given 2 arrays find out if one is the rotated version of the other'
    if len(first) != len(second): # not the same number of elements
        return False
    for i in first:
        if i in second: # if the integer is in the second array do nothing
            continue
        else: # if the integer is not in the second array return false
            return False
    return True # if all numbers are in both arrays, return true

def element_only_once(array):
    # 5. Find the only element in an array that only occurs once
    only_once = [i for i in array if array.count(i) == 1]
    return only_once[0] if len(array) == 1 else None

def common_elements(first, second):# functional
    # 6. Find the common elements in two arrays
    return frozenset(set(first).intersection(second))

def common_elements_v2(first, second): # alternative functional
    # 6. Find the common elements in two arrays
    return [i for i in first if i in second]

def common_elements_in_arrays(first, second): # procedual
    # 6. Find the common elements in two arrays
    common  = []
    for i in first:
        if i in second:
            common.append(i)
    return common

def bin_search(array, n):# procedual
    # 7. implement binary search of a sorted array of integers
    # 8. binary search on an unsorted array
    array = sorted(array)
    left  = 0
    right = len(array) - 1
    while left <= right:
        middle = int(left + (right - 1)/2)
        print(left, right, middle)
        if array[middle] == n:
            return middle
        elif array[middle] < n:
            left = middle + 1
        else:
            right = middle - 1
    return -1

def bin_search_recursive(array, left, right, n): # recursive
    # 7. implement binary search of a sorted array of integers
    # 8. binary search on an unsorted array
    array = sorted(array)
    if left <= right:
        mid = int(left + (right - 1)/ 2)
        if array[mid] == n:
            return mid
        elif array[mid] > n:
            return bin_search_recursive(array, left, mid -1, n)
        else:
            return bin_search_recursive(array, mid+1, right, n)
    else:
        return -1

def prime_numbers(n):
    # 9. find the first x prime numbers
    primes = []
    for num in range(2, n):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
    return primes

def squareroot(number): # only works on perfect squares
    # 12. implement a squareroot function
    if number == 1:
        return 1
    elif number < 0:
        return -1
    for i in range(2,number):
        if number/(i**2) == 1:
            return i
        elif number/(i**2) != i and \
            int(number/(i**2)) * i**2 == number:
                return parse_squareroot((i, squareroot(int(number/(i**2)))))
    return -1

def parse_squareroot(args):
    # 12 helper method
    result = 1
    for index, value in enumerate(args):
        if type(value) is tuple:
            for n in args[index]:
                result *= n
        else:
            result *= value
    return result

def exponent(number, power):
    # 12 implement an exponent function
    if power == 0:
        return 1
    n = [number] * power
    result = 1
    for i in n:
        result *= i
    return result

def multiplication_without_x(op1, op2):
    # 14 write a multiply function without using *
    numbers = []
    for i in range(op2):
        numbers.append(op1)
    total = 0
    for i in numbers:
        total += i
    return total

def multiplication_without_x_v2(op1,op2):
    # 14 functional version
    return sum([op1 for i in range(op2)])

def multiplication_without_x_v3(op1,op2):
    # 14 also functional popped into my head
    import itertools
    return list(itertools.accumulate([op1 for i in range(op2)]))[-1]

if __name__ == '__main__':
    print(multiplication_without_x(3, 123))
    print(multiplication_without_x_v2(3, 123))
    print(multiplication_without_x_v3(3, 123))