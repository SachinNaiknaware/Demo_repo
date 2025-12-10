# 1. stack LIFO (last in first out)

# stack = []
# stack.append(10)   # push
# stack.append(20)
# print(stack.pop()) # pop → 20
# print(stack[-1])   # peek → 10
# print(stack)


# 2. Queue (FIFO – First In, First Out)
# from collections import deque
# queue = deque()
# queue.append("A")   # enqueue
# queue.append("B")
# print(queue.popleft())  # dequeue → A


#3. Linked List
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def insert_front(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node

#     def display(self):
#         cur = self.head
#         while cur:
#             print(cur.data, end=" -> ")
#             cur = cur.next
#         print("None")

# ll = LinkedList()
# ll.insert_front(10)
# ll.insert_front(20)
# ll.display()  # 20 -> 10 -> None


