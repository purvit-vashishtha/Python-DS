"""
Given a list lst and a number N, create a new list
that contains each number of the list at most N times without reordering.
"""

import collections
from array import *

arr = [1, 2, 3, 1, 2, 1, 2, 3]

# time complexity = O(n)
def delete_nth(array, n):
    result = []
    counts = collections.defaultdict(int)

    for i in array:
        if counts[i] < n:
            result.append(i)
            counts[i] += 1

    print(result)

# time complexity = O(n^2)
def delete_nth_2(array, n):
    result = []
    for i in array:
        if result.count(i) < n:
            result.append(i)

    print(result)


#delete_nth(arr, 2)
delete_nth_2(arr, 2)