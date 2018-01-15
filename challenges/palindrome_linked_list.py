'''
Given a singly linked list, determine if it is a palindrome.
'''

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        elements = []
        while head:
            elements.append(head.val)
            head = head.next
        return elements == list(reversed(elements))