# -*- coding: utf-8 -*-

'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

'''

def t(array):
    p = []
    for i in range(len(array)):
        product = 1
        for j in range(len(array)):
            if i != j:
                product = product * array[j]
        p.append(product)
    return p

def get_ex_products(array):
    ex_products = []
    product = mult_nums(array)
    
    for index in range(len(array)):
        # divide the ith element from product to exclude it from the product
        ex_products.append(product//array[index])
    
    return ex_products

def mult_nums(nums):
    product = 1
    for num in nums:
        product = product * num
    return product

if __name__ == '__main__':
    tests = [
        [1, 2, 3, 4, 5],        # [120, 60, 40, 30 , 24]
        [3, 2, 1],              # [2, 3, 6]
        [2, 4, 6, 8, 10],       # [1920, 960, 640, 480, 384]
        [2, 4, 6, 8, 10, 12],   # [23040, 11520, 7690, 5760, 4608, 3840]
    ]
    for test in tests:
        print(t(test))