# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 12:05:53 2017

@author: DerlingB
"""

# Write a Python program to find the three elements that sum to zero from a set (array) of n real numbers.
# Input
# [-25, -10, -7, -3, 2, 4, 8, 10]
# Output
# [[-10, 2, 8], [-7, -3, 10]] 

class Sum_Zero():
    def get_sum_zero(self, array):
        result = []
        for i in range(len(array)):
            for j in range(i + 1, len(array)):
                # check if the opposite number of the sum of the two current
                # integers is in the array, if so we have a match
                if (array[i] + array[j]) * -1 in array:
                    # sorted because we may run into this combination again
                    combination = sorted([
                            array[i], 
                            array[j],
                            (array[i] + array[j]) * -1
                            ])
                    # check to see whether we have already seen the combination
                    if combination not in result:
                        result.append(combination)
        return result

class py_solution:
    # course solution
    def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result

if __name__ == '__main__':
    class_ = Sum_Zero()
    print(class_.get_sum_zero([-25, -10, -7, -3, 2, 4, 8, 10]))