"""
LinkedList Deletion
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        temp = self.head
        while temp is not None:  # loop till temp is not null
            print(temp.data)
            temp = temp.next

    def insertion(self, new):
        newnode = Node(new)
        newnode.next = self.head
        self.head = newnode

    def deletion(self, remove):     # method to delete node
        val = self.head             # initializing val to head or starting node
        if val is not None:
            if val == remove:               # if element found
                self.head = val.next        # skip the element we want to delete
                val = None
                return

        while val is not None:          # loop till null
            if val.data == remove:      # if element to be deleted found then break
                break
            prev = val
            val = val.next              # update val

        if val == None:                 # if linkedlist is empty
            return

        prev.next = val.next
        val = None                      # deleting the node


l = LinkedList()

l.head = Node("BMW")
e1 = Node("Mercedes")
e2 = Node("Audi")

l.head.next = e1
e1.next = e2

l.deletion("Audi")
l.insertion("Jaquar")
l.print()

"""
Desired Output:

Jaquar
BMW
Mercedes
"""