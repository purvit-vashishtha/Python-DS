"""Implementation of Priority Queue using Linear Array
Insertion time complexity= O(n)
"""
import itertools


class PriorityQueueNode:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority

    def __repr__(self):
        return "{}: {}".format(self.data, self.priority)


class PriorityQueue:
    def __init__(self, items=None, priorities=None):
        self.priorityqueuelist = []
        if items is None:
            return
        if priorities is None:
            priorities = itertools.repeat(None)
        for item, priority in zip(items, priorities):
            self.push(item, priority = priority)

    def __repr__(self):
        return "PriorityQueue({!r})".format(self.priorityqueuelist)

    def push(self, item, priority=None):            # method to push item in the queue and set priority accordingly
        priority = item if priority is None else priority
        node = PriorityQueueNode(item, priority)
        for index, current in enumerate(self.priorityqueuelist):
            if current.priority < node.priority:
                self.priorityqueuelist.insert(index, node)
                return

        self.priorityqueuelist.append(node)

    def pop(self):                          # pops the element which has higher priority
        return self.priorityqueuelist.pop().data

    def size(self):                     # returns the size of queue
        return len(self.priorityqueuelist)

    def print(self):                    # prints the Priority Queue
        for i in self.priorityqueuelist:
            print(i)


pq2 = PriorityQueue()
print("Priority Queue:")
pq2.push("A",9)
pq2.push("B",7)
pq2.push("N",5)
pq2.push("D",2)
pq2.push("S",1)
pq2.print()
print("Size of priority queue:", pq2.size())

print("\nFirst element deleted: ", pq2.pop())
print("Second Element deleted: ", pq2.pop())

"""
Desired Output:
Priority Queue:
A: 9
B: 7
N: 5
D: 2
S: 1
Size of priority queue: 5

First element deleted:  S
Second Element deleted:  D

Process finished with exit code 0


"""
