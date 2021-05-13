"""
Merging two Linked List to one
1.) By Normal Function
2.) By Recursive function
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def Merge(l1, l2):
    ret = head = Node(0)
    while l1 and l2:
        if l1.data > l2.data:
            head.next = l1
            l1 = l1.next
        else:
            head.next = l2
            l2 = l2.next
        head = head.next
        head.next = l1 or l2
        return ret.next


def merge_two_list_recur(l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.data < l2.data:
        l1.next = merge_two_list_recur(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_list_recur(l1, l2.next)
        return l2