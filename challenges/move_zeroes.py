'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
'''
def move_zeroes(nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeroes = 0
        i = 0
        while i < len(nums):
            if not nums[i]:
                zeroes = zeroes + 1
                nums.pop(i)
            else:
                i = i + 1
        nums.extend([0] * zeroes)

if __name__ == '__main__':
    test = [0, 1, 0, 3, 12]
    move_zeroes(test)
    print(test)

'''
remove all the zeroes from the array
then add them to the end of the array
'''