'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

def merge_two_lists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    dummy = ListNode(0)
    dummy_head = dummy
    while l1 or l2:
        l1_val = l2_val = None
        if l1:
            l1_val = l1.val
        if l2:
            l2_val = l2.val
        if l1_val != None and l2_val != None:
            if l1_val <= l2_val:
                dummy.next = ListNode(l1_val)
                l1 = l1.next
            elif l2_val < l1_val:
                dummy.next = ListNode(l2_val)
                l2 = l2.next
        else:
            if l1_val != None:
                dummy.next = ListNode(l1_val)
                l1 = l1.next
            elif l2_val != None:
                dummy.next = ListNode(l2_val)
                l2 = l2.next
        dummy = dummy.next
    return dummy_head.next

if __name__ == '__main__':
	l1 = l1_head = ListNode(0)
	l2 = l2_head = ListNode(0)
	l1_values = [1, 2, 3, 4]
	l2_values = [0, 2, 3, 5, 6]
	for v in l1_values:
		l1.next = ListNode(v)
		l1 = l1.next
	for v in l2_values:
		l2.next = ListNode(v)
		l2 = l2.next
	merged_list = merge_two_lists(l1_head, l2_head)
	while merged_list:
		print(merged_list.val, end=' ')
		merged_list = merged_list.next
