'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

'''


# Definition for singly-linked list.
class ListNode(object):
   def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        type l1: ListNode
        type l2: ListNode
        rtype: ListNode
        """
        dummy = current = ListNode(0)
        carry_over = 0 # carry_over used to track if last sum was greater than 10
        while l1 or l2 or carry_over:
            if l1:
                carry_over += l1.val
                l1 = l1.next
            if l2:
                carry_over += l2.val
                l2 = l2.next
            current.next = ListNode(carry_over % 10)
            current = current.next
            carry_over = carry_over//10
        return dummy.next

def create_list(nums):
    '''
    type nums: int[]
    rtype : ListNode
    '''
    head = dummy = ListNode(0)
    while nums:
        head.next = ListNode(nums.pop())
        head = head.next
    return dummy.next

if __name__ == '__main__':
    list1 = create_list([3, 4, 2])
    list2 = create_list([4, 6, 5])
    solution = Solution().addTwoNumbers(list1, list2)


    list_vals = []
    while solution:
        list_vals.append(str(solution.val))
        solution = solution.next

    # print the values of the sum of the lists ie 7 -> 0 -> 8
    print(' -> '.join(list_vals))

'''
iterate through each linked list while there are still nodes available
add both values togetther to get the value of the next node
value of next node = sum modulus 10
carry_over keeps track of whether or not the value was greater than or equal 10
if carry_over and no nodes are available it still adds a 1 at the end of the linked list
'''