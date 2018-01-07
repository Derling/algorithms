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
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = current = ListNode(0)
        carry_over = 0
        while l1 or l2 or carry_over:
            if l1:
                carry_over = carry_over + l1.val
                l1 = l1.next
            if l2:
                carry_over = carry_over + l2.val
                l2 = l2.next
            current.next = ListNode(carry_over % 10)
            current = current.next
            carry_over = int(carry_over / 10)
        return dummy.next

if __name__ == '__main__':
    l1 = l1_head = ListNode(2)
    l1.next = ListNode(4)
    l1 = l1.next
    l1.next = ListNode(3)
    l2 = l2_head = ListNode(5)
    l2.next = ListNode(6)
    l2 = l2.next
    l2.next = ListNode(4)
    solution = Solution().addTwoNumbers(l1_head, l2_head)
    while solution:
        print(solution.val)
        solution = solution.next

'''
iterate through each linked list while there are still nodes available
add both values togetther to get the value of the next node
value of next node = sum modulus 10
carry_over keeps track of whether or not the value was greater than or equal 10
if carry_over and no nodes are available it still adds a 1 at the end of the 
new linked list
'''