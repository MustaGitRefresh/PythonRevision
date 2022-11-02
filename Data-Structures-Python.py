# DSA in python
# Linked List
# Program 1 creating a linked list and performing the operations on it
# l1 = list()
# l1.append('America')
# l1.append('Japan')
# l1.append('India')
#
# # displaying the menu
# print("The existing list = {}".format(l1))
# choice = 0
# while choice < 5:
#     print("LINKED LIST OPERATION")
#     print('1 Add element')
#     print("2 Remove element")
#     print("3 Replace element")
#     print("4 Search for element")
#     print('5 Exit')
#
#     choice = int(input("Enter your choice:\n"))
#     if choice == 1:
#         element = input("Enter element: ")
#         pos = int(input("Enter the position: "))
#         l1.insert(pos, element)
#
#     elif choice == 2:
#         try:
#             element = input("Enter the element")
#             l1.remove(element)
#
#         except ValueError:
#             print("Element not found")
#
#     elif choice == 3:
#         element = input("Enter element: ")
#         pos = int(input("Enter the position: "))
#         l1.pop(pos)
#         l1.insert(pos, element)
#
#     elif choice == 4:
#         element = input("Enter element:\n")
#         try:
#             pos = l1.index(element)
#             print("Element found at position: ", pos)
#         except ValueError:
#             print("Element not found")
#     else:
#         break
#
# print('List = ', l1)
# Python program 3 using the stack class
# from stack import Stack
#
# s = Stack()
# choice = 0
# while choice < 5:
#     print("STACK OPERATIONS")
#     print("1 push element")
#     print("2 pop element")
#     print("3 peep element")
#     print("4 search for element")
#     print("5 Exit")
#     choice = int(input("Enter your choice:\n"))
#
#     if choice == 1:
#         element = int(input("Enter element: "))
#         s.push(element)
#     elif choice == 2:
#         element = s.pop()
#         if element == -1:
#             print("The stack is empty")
#         else:
#             print(f"Popped element is {element}")
#     elif choice == 3:
#         element = s.peep()
#         print('Topmost element = ', element)
#     elif choice == 4:
#         element = int(input("Enter element: "))
#         pos = s.search(element)
#         if pos == -1:
#             print("The stack  is empty")
#         elif pos == -2:
#             print('Element not found in the stack')
#         else:
#             print("Element found at position: ", pos)
#     else:
#         break
#     print(s.display())
#
# print('Stack= ', s.display())
# Queues
# from ques import Queue
#
# q = Queue()
# choice = 0
# while choice < 4:
#     print("STACK OPERATIONS")
#     print("1 add element")
#     print("2 delete element")
#     print("3 search element")
#     print("4 Exit")
#     choice = int(input("Enter your choice:\n"))
#
#     if choice == 1:
#         element = float(input("Enter element: "))
#         q.add(element)
#     elif choice == 2:
#         element = q.delete()
#         if element == -1:
#             print("The queue is empty")
#         else:
#             print(f"Removed element is {element}")
#     elif choice == 3:
#         element = float(input("Enter element: "))
#         pos = q.search(element)
#         if pos == -1:
#             print("Queue is empty")
#         elif pos == -2:
#             print("Element not found in the queue")
#         else:
#             print('Element found at position: ', pos)
#     else:
#         break
#     print(q.display())
#
# print('Queue= ', q.display())
# collection module
# in ipython
# Deque + s
# program 6 python program to create a deque and do operations
# from collections import deque
#
# d = deque()
#
# choice = 0
# while choice < 7:
#     print("DEQUE OPERATIONS")
#     print('1 Add element')
#     print('2 Remove element at front')
#     print('3 Add element at rear')
#     print('4 Remove element at rear')
#     print('5 remove element in the middle')
#     print('6 Search for an element')
#     print('7 Exit')
#
#     choice = int(input("Enter your choice:\n"))
#     if choice == 1:
#         element = input("Enter the element:\n")
#         d.appendleft(element)
#     elif choice == 2:
#         if len(d) == 0:
#             print("Deque is empty")
#         else:
#             d.popleft()
#     elif choice == 3:
#         element = input("Enter element:\n")
#         d.append(element)
#     elif choice == 4:
#         if len(d) == 0:
#             print("Deque is empty")
#         else:
#             d.pop()
#     elif choice == 5:
#         element = input("Enter element:\n")
#         try:
#             d.remove(element)
#         except ValueError:
#             print("Element not found")
#     elif choice == 6:
#         element = input("Enter element:\n")
#         c = d.count(element)
#         print(f'No of times element found: {c}')
#         index = d.index(element) + 1
#         print(f'The index of {element} is {index}')
#
#     else:
#         break
#
#     print('Deque - ', end='')
#     for i in d:
#         print(i, ' ', end='')
#     print()
