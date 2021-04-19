#Array Data Structure
from array import *
arr = array("i", [10, 20, 30, 40, 50])
#traverse
for z in arr:
    print(z)

#insertion
print("After inserting new element:")
arr.insert(5,60)
print(arr[5])

#deletion
print("After deleting 20:\n")
arr.remove(20)
for x in arr:
    print(x)

#search
print("Searching 60 in array:\n")
print("Found at index:", arr.index(60))

#updation
print("After updating 1st Index of array:")
arr[1] = 100
for y in arr:
    print(y)
