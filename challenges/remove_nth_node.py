'''
Given a linked list, remove the nth node from the end of list and return its head.

For example,

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
'''

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

def remove_nth_node(head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        values = []
        while head:
            values.append(head.val)
            head = head.next
        values.pop(-1 * n)
        dummy = ListNode(0)
        dummy_head = dummy
        for i in values:
            dummy.next = ListNode(i)
            dummy = dummy.next
        return dummy_head.next

if __name__ == '__main__':
    head = tail = ListNode(1)
    nodes = [2, 3, 4, 5]
    for i in nodes:
        tail.next = ListNode(i)
        tail = tail.next
    head = remove_nth_node(head, 2)
    while head:
        print(head.val)
        head = head.next