# Student List
# student = [10, 'Venus gopal', 'M', 50, 55, 62, 74, 66]
# print(student)
# print(student[1])
# print(student[0:3:1])
# print(student[:3:])
# print(student[::])
# num = [10, 20, 30, 40, 50]
# print("Total list = ", num)
# print("First = %d, Last = %d" % (num[0], num[4]))
# names = ['Raju', 'Van', 'Gopal', "Laxmi"]
# print("Total list = ", names)
# print("First = %s, Last = %s" % (names[0], names[3]))
# x = [10, 20, 10.5, 2.55, 'Ganesh', 'Vishnu']
# print("Total list = ", x)
# print("First = %d, Last = %s" % (x[0], x[5]))
# Creating the list using the range function
# List1 = range(10)
# for i in List1:
#     print(i, ', ', end='')
# print()
#
# List2 = range(5, 10)
# for i in List2:
#     print(i, ', ', end='')
# print()
#
# List3 = range(5, 10, 2)
# for i in List3:
#     print(i, ', ', end='')
# print()
# list and len function with while and for loop
# list_num = range(10, 60, 10)
# print("Using while loop")
# i = 0
# while i < len(list_num):
#     print(list_num[i])
#     i += 1
# print("Using for loop")
# for i in list_num:
#     print(i)
# Updating the elements of the list
# list_update = list(range(1, 5))
# print(list_update)
# list_update.append(9)
# print(list_update)
# list_update[1] = 8
# print(list_update)
# list_update[1:3] = 10, 11
# print(list_update)
# del list_update[1]
# print(list_update)
# list_update.remove(11)
# print(list_update)
# list_update.reverse()
# print(list_update)
# Our own logic for reverse method of a list
# days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# print("\nIn reverse order")
# i = len(days)-1
# while i >= 0:
#     print(days[i])
#     i -= 1
#
# print("\nIn reverse order new")
# i = -1
# while i >= -len(days):
#     print(days[i])
#     i -= 1
# Concatenation of Two Lists
# x = [10, 20, 30, 40, 50]
# y = [100, 110, 120]
# print(x+y)
# Repetition of Lists
# x = [10, 20, 30, 40, 50]
# print(x*2)
# Membership in lists
# x = [10, 20, 30, 40, 50]
# a = 20
# print(a in x)
# print(a not in x)
# Aliasing and Cloning Lists
# x = [10, 20, 30, 40, 50]
# y = x
# print(x)
# print(y)
# x[1] = 99
# print(x)
# print(y)
# Copying
# y = x[:]
# print(x)
# print(y)
# x[1] = 98
# print(x)
# print(y)
# copy method is also a solution for this problem
# Some methods to process list
# numbers = [10, 20, 30, 40, 50]
# n = len(numbers)
# print("No. of elements in list: ", n)
# numbers.append(60)
# print('Number after appending 60: ', numbers)
# numbers.insert(0, 60)
# print('Number after inserting 5 at 0th position: ', numbers)
# numbers1 = numbers.copy()
# print("Newly created list: ", numbers1)
# numbers.extend(numbers1)
# print("Numbers after extending numbers1: ", numbers)
# n = numbers.count(50)
# print('No. of times 50 came in the lists: ', n)
# numbers.remove(50)
# print('After removing 50 from the list: ', numbers)
# numbers.pop()
# print('Number after removing ending elements: ', numbers)
# numbers.sort()
# print("Numbers after sorting: ", numbers)
# numbers.reverse()
# print("Numbers after reversing: ", numbers)
# numbers.clear()
# print("Number after clearing: ", numbers)
# Finding the biggest and smallest elements in the lists
# Our own logic not min and max builtin functions
# x = []
#
# n = int(input())
# for i in range(n):
#     print("Enter the element: ", end='')
#     x.append(int(input()))
# print('The list is: ', x)
# big = x[0]
# small = x[0]
# for i in range(1, n):
#     if x[i] > big:
#         big = x[i]
#     elif x[i] < small:
#         small = x[i]
#
#
# print("The maximum is: ", big)
# print("The minimum is: ", small)
# Sorting the list with our own logic
# x = []
# print("How many elements? ", end='')
# n = int(input())
# for i in range(n):
#     print("Enter the element: ",end='')
#     x.append(int(input()))
# print('Original list is: ',x)
# flag = False
# for i in range(n-1):
#     for j in range(n-1-i):
#         if x[j] > x[j+1]:
#             t = x[j]
#             x[j] = x[j+1]
#             x[j+1] = t
#             flag = True
#     if not flag:
#         break
#     else:
#         flag = False
# print('Sorted list: ', x)
# Number of occurring of an elements in the lists
# x = []
# n = int(input('How many elements? '))
# for i in range(n):
#     print("Enter the element: ", end='')
#     x.append(int(input()))
# print('The list is: ', x)
# y = int(input("Enter the element to count: "))
# c = 0
# for i in x:
#     if y == i:
#         c += 1
# print('{} is found {} times.'.format(y, c))
# Finding the common elements in the two list
# scholar1 = ['Vinay', 'Krishna', 'Rasalgethi', 'Govind']
# scholar2 = ['Rosy', 'Govind', 'Christianus', 'Vinay', 'Visual']
# s1 = set(scholar1)
# s2 = set(scholar2)
#
# s3 = s1.intersection(s2)
# common = list(s3)
# print(common)
# Storing different types of data in a list
# emp = []
# n = int(input('How many employees? '))
# for i in range(n):
#     print("Enter the id: ", end='')
#     emp.append(int(input()))
#     print("Enter the name: ", end='')
#     emp.append(input())
#     print("Enter the salary: ", end='')
#     emp.append(float(input()))
# print("The list is created with the employee data.")
# ID = int(input("Enter the employee id: "))
# for i in range(len(emp)):
#     if ID == emp[i]:
#         print('Id = {:d}, Name = {:s}, Salary = {:.2f}'.format(emp[i], emp[i+1], emp[i+2]))
#
# Nested Lists
# a = [80, 90]
# b = [10, 20, 30, 40, a]
# print('Total List: {}'.format(b))
# print("First element= {}".format(b[0]))
# print("Last element is nested list = {}".format(b[4]))
# for x in b[4]:
#     print(x)
# print(b[4][0])
# print(b[4][1])
# Matrices through lists
# mat = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# print('Display the list as it is {}'.format(mat))
# print('Displaying row by row')
# for r in mat:
#     print(r)
# print('Display each column in row 0: ')
# for c in mat[0]:
#     print('%d' % c, end=' ')
# print()
# print('Display each column in row 1: ')
# for c in mat[1]:
#     print('%d' % c, end=' ')
# print()
# print('Display each column in row 2: ')
# for c in mat[2]:
#     print('%d' % c, end=' ')
# print()
#
# print('Display all elements using for:')
# for r in mat:
#     for c in r:
#         print(c, end=' ')
#     print()
# print('Display all elements using for range:')
# for i in range(len(mat)):
#     for j in range(len(mat[i])):
#         print('%d ' % mat[i][j], end=' ')
#     print()
# Matrices adding with simple logic of assigning
# m1 = [
#     [1, 2, 3, 0],
#     [4, 5, 6, 0],
#     [7, 8, 9, 0]
# ]
#
# m2 = [
#     [1, 2, 3, 4],
#     [1, 0, 1, 0],
#     [2, -1, -2, 1]
# ]
#
# m3 = [4 * [0] for i in range(3)]
#
# # Adding logic
# for i in range(3):
#     for j in range(4):
#         m3[i][j] = m1[i][j] + m2[i][j]
#
# # displaying the new matrix
# for i in range(3):
#     for j in range(4):
#         print('%d' % m3[i][j], end=' ')
#     print()
# List comprehension
# squares = []
# for x in range(1, 11):
#     squares.append(x ** 2)
# print(squares)
#
# squares_comprehension = [x ** 2 for x in range(1, 11)]
# print(squares_comprehension)
# even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
# print(even_squares)
# even_squares_mine = [i for i in squares_comprehension if i % 2 == 0]
# print(even_squares_mine)
# x = [10, 20, 30]
# y = [1, 2, 3, 4]
# lst = [i+j for i in x for j in y]
# for i in x:
#     for j in y:
#         lst.append(i + j)
# print(lst)
# print(lst)
# lst = [i+j for i in [10, 20, 30] for j in [1, 2, 3, 4]]
# print(lst)
# lst = [i+j for i in 'ABC' for j in 'DE']
# print(lst)
# with words
# words = ['Apple', 'Grapes', 'Banana', 'Orange']
# lst = []
# for w in words:
#     lst.append(w[0])
# print(lst)
# lst = [w[0] for w in words]
# print(lst)
# colour_file = open('colours.txt')
# colours_list = colour_file.readlines()
# colour_list_no = [colour.replace('\n', '') for colour in colours_list]
# first_colour_letter = [letter[0] for letter in colour_list_no]
# print(first_colour_letter)
# num1 = [1, 2, 3, 4, 5]
# num2 = [10, 11, 1, 2]
# num3 = [i for i in num1 if i not in num2]
# for i in num1:
#     if i not in num2:
#         num3.append(i)
# print(num3)
# Dictionary Comprehension
# dict_hall_ticket_student = {
#     1001: 'Prat ap',
#     1002: 'Mohan',
#     1003: 'Ankita'
# }
#
# dict1 = {value: key for key, value in dict_hall_ticket_student.items()}
# print(dict1)
# TUPLES
# tup1 = ()
# tup2 = (20, )
# tup3 = (10, 20, -30.1, 40.5, 'Hyderabad', 'New Delhi')
# tup4 = (10, 20, 30, 40)
# tup5 = 1, 2, 3, 4
# print(tup1, tup2, tup3, tup4, tup5)
# list to tuple
# list_num = [1, 2, 3]
# tp1 = tuple(list_num)
# print(tp1)
# tp2 = tuple(range(4, 9, 2))
# print(tp2.__sizeof__())
# Accessing the Tuple elements
# tup = (50, 60, 70, 80, 90, 100)
# print(tup[0])
# print(tup[5])
# print(tup[-1])
# print(tup[-6])
# print(tup[:])
# print(tup[1:4])
# print(tup[::2])
# print(tup[::-2])
# print(tup[-4:-1])
# Student details in tuple
# student = (10, 'Vinay Kumar', 50, 60, 65, 61, 70)
# rno, name = student[0:2]
# print(rno)
# print(name)
# marks = student[2:7]
# for i in marks:
#     print(i)
# Basic operations on tuples
# student = (10, 'Vinay Kumar', 50, 60, 65, 61, 70)
# print(len(student))
# fees = (25000.00, )*2
# student1 = student + fees
# print(student1)
# name = 'Vinay kumar'
# print(name in student1)
# print(name not in student1)
# tp1 = (10, 11, 12)
# tpl1 = tp1*3
# print(tpl1)
# finding the average and sum of the given elements in the tuple
# numbers_tup = eval(input("Enter the elements(): "))
# sum_tup_numbers = 0
# n = len(numbers_tup)
# for i in range(n):
#     sum_tup_numbers += numbers_tup[i]
# print('Sum of numbers: ', sum_tup_numbers)
# print('Average of numbers: ', sum_tup_numbers/n)
# Adding a search facility in the tuple box
# user_string_input = input("Enter the elements separated by comma ").split(',')
# int_lst_tup_values = [int(num) for num in user_string_input]
# tuple_int_nums = tuple(int_lst_tup_values)
# print("The tuple is {}".format(tuple_int_nums))
# ele = int(input("Enter the element to search:\n"))
# try:
#     pos = tuple_int_nums.index(ele)
#     print('Found at the position {}'.format(pos+1))
# except ValueError:
#     print('Element not found in tuple')
# Nested Tuples
# tup_nest = (50, 60, 70, 80, 90, (200, 201))
# print(tup_nest[5])
# print(tup_nest[6]) This index is out of range.
# employee data storing in nested tuples
# employee_data = (
#     (10, 'Vijay', 9000.90),
#     (20, 'Ihar', 5500.75),
#     (30, 'Naja', 89000.00),
#     (40, 'Kapor', 5000.50)
# )
# # Sorting the tuples
# print(sorted(employee_data, key=lambda x: x[1]))
# print(sorted(employee_data, key=lambda x: x[2]))
# print(sorted(employee_data, reverse=True))
# Inserting the Elements in the tuples
# names = ('Vishnu', 'Anupam', 'Lakshmi', 'Mahesh')
# print(names)
# lst = [input("Enter the new name: ")]
# new = tuple(lst)
# pos = int(input("Enter the position: "))
# names1 = names[0: pos-1]
# names1 = names1 + new
# names = names1 + names[pos-1:]
# print(names)
# Modifying the tuple elements
# num = (10, 20, 30, 40, 50)
# print(num)
# lst = [int(input("Enter a new element: "))]
# new = tuple(lst)
# pos = int(input("Enter the position no: "))
# num1 = num[0: pos-1]
# num1 = num1 + new
# num = num1 + num[pos:]
# print(num)
# Deleting the elements from the tuple
# num = (10, 20, 30, 40, 50)
# print(num)
# pos = int(input("Enter the position no: "))
# num1 = num[0: pos-1]
# num = num1 + num[pos:]
# print(num)
