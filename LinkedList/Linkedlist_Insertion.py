"""
LinkedList Implementation
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        temp = self.head
        while temp is not None:     # loop till temp is not null
            print(temp.data)
            temp = temp.next        # traverse through all nodes

    def insertion(self, new):   # Method to insert at beginning of Linked list
        first = Node(new)           # inserting into list
        first.next = self.head      # updating position of new node
        self.head = first           # updating head node

    def insertatmid(self, mide, new):
        if mide is None:
            print("Node is not present")
            return
        newnode = Node(new)
        newnode.next = mide.next
        mide.next = newnode

    def insertatend(self, last):
        laste = Node(last)
        if self.head is None:
            self.head = laste
            return
        tmp = self.head
        while(tmp.next):
            tmp = tmp.next
        tmp.next = laste


l = LinkedList()        # creating object of linkedlist class

l.head = Node("BMW")    # Initializing head with first node
e1 = Node("Audi")
e2 = Node("Mercedes")
l.head.next = e1        # connecting head node to second node
e1.next = e2            # connecting second node to third node

print("LinkedList before Insertion:")
l.print()
l.insertion("Volvo")
l.insertatmid(l.head.next,"Jaquar")
l.insertatend("Kia")
print("\nLinkedList after Insertion:")
l.print()

"""
Desired Output:
LinkedList before Insertion:
BMW
Audi
Mercedes

LinkedList after Insertion:
Volvo
BMW
Jaquar
Audi
Mercedes
Kia

Process finished with exit code 0
"""