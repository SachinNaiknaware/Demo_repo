

# Stack
# Queue
# Linked Lists
# Sorting
# Searching
# Linear Search
# Binary Search



#pendig understanding how it works
#------------------------------------------------------------------------
#------------------------------------------------------------------------



#1. Stack (LIFO - Last In First Out)

stack = []

# Push
stack.append(10)
stack.append(20)

# Pop
print(stack.pop())  # 20

# Peek
print(stack[-1])    # 10
#----------------------------
#2. Queue (FIFO - First In First Out)

from collections import deque

queue = deque()

# Enqueue
queue.append(10)
queue.append(20)

# Dequeue
print(queue.popleft())  # 10
#-----------------------------
# 3. Linked List
# Each element (node) contains data and a reference to the next node.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating nodes
node1 = Node(10)
node2 = Node(20)
node1.next = node2

# Traversing
current = node1
while current:
    print(current.data)
    current = current.next
#--------------------------------
#  4. Sorting Algorithms
#  a. Bubble Sort



def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#------------------------------------
# b. Insertion Sort

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
#c. Merge Sort

#---------------------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    def merge(left, right):
        sorted_list = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1
        sorted_list += left[i:]
        sorted_list += right[j:]
        return sorted_list

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
# 5. Searching Algorithms
# a. Linear Search
#-----------------------------
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
#------------------------------
# b. Binary Search
Works on sorted arrays only
Time Complexity: O(log n)

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
