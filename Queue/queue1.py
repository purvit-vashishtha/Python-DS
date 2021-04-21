class queue:
    def __init__(self):
        self.queue = list()

    def add(self, val):              # method to add elements to the queue
        if val not in self.queue:
            self.queue.insert(0, val)
            return True
        return False

    def remove(self):                   # method to remove elements from queue
        if len(self.queue) > 0:         # if queue is not empty
            return self.queue.pop()
        return "No elements in the queue"

    def size(self):                 # method to obtain size of queue
        return len(self.queue)

    def print(self):                # method to print the elements in queue
        for i in self.queue:
            print(i)


q = queue()
print("Elements in the queue:")
q.add("BMW")
q.add("Mercedes")
q.add("Audi")
q.print()
print("Size of queue:", q.size())
print("Removed element is:", q.remove())


""" 
Desired Output:

Elements in the queue:
Audi
Mercedes
BMW
Size of queue: 3
Removed element is: BMW

Process finished with exit code 0
"""