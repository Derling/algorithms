'''
Reverse a singly linked list.
'''


class ListNode(object):
     def __init__(self, x):
       self.val = x
       self.next = None

def reverse_list(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    values = []
    while head:
        values.append(head.val)
        head = head.next
    dummy = ListNode(0)
    dummy_head = dummy
    for i in reversed(values):
        dummy.next = ListNode(i)
        dummy = dummy.next
    return dummy_head.next
        
if __name__ == '__main__':
    dummy = dummy_head = ListNode(0)
    list_values = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    for i in list_values:
        dummy.next = ListNode(i)
        dummy = dummy.next
    reversed_list = reverse_list(dummy_head.next)
    while reversed_list:
        print(reversed_list.val, end=' ')
        reversed_list = reversed_list.next
