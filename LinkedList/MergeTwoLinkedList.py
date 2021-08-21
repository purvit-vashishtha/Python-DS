"""Merge two sorted linked lists and return it as a sorted list.
The list should be made by splicing together the nodes of the first two lists.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def MergetwosortedLL(self, l1: ListNode,l2: ListNode) -> ListNode:
        if not l1 and l2:
            return l1
        elif not l1:
            return l2
        elif not l2:
            return l1

        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                tmp = l1.next
                curr.next = l1
                curr = l1
                curr.next = None
                l1 = tmp
            else:
                tmp = l2.next
                curr.next = l2
                curr = l2
                curr.next = None
                l2 = tmp

            if l1:
                curr.next = l1
            else:
                curr.next = l2

        return dummy.next