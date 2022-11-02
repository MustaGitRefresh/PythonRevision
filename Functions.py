"""
Doing functions
"""

#
#
# # :def :function name (a:params, b:params)
# def sums(a, b):
#     """
#     This function finds the sum of two numbers:Docstring
#     """
#     # Code
#     c = a + b
#     # print(c)
#     # with return statement
#     return c
#
#
# # print(sums(10, 15))
# # print(sums(1.5, 10.75))
# x = sums(10, 15)
# y = sums(1.5, 10.75)
# print(x)
# print(y)
#
#
# def even_odd(num):
#     if num % 2 == 0:
#         print(num, 'is even')
#     else:
#         print(num, 'is odd')
#
#
# even_odd(12)
# even_odd(13)
# def fact(n):
#     """
#     To find the factorial of the number
#     """
#     prod = 1
#     while n >= 1:
#         prod = prod * n
#         n -= 1
#
#     return prod
#
#
# lst_fact = []
# for i in range(1, 10000):
#     lst_fact.append(i)
#     print(fact(i))
# def prime_or_not(num):
#     """
#     Check whether num is prime or not
#     """
#     x = 1
#     for i in range(2, num):
#         if num % i == 0:
#             x = 0
#             break
#         else:
#             x = 1
#     return x
#
#
# number = int(input("Enter the number:\n"))
# result = prime_or_not(number)
# if result == 1:
#     print(number, 'is prime')
# else:
#     print(number, 'is not prime')
# write a function to get the prime numbers from the given range of numbers by the user
# def prime(n):
#     """
#     To check if n i s prime or not
#     """
#     x = 1
#     for i in range(2, n):
#         if n % i == 0:
#             x = 0
#             break
#         else:
#             x = 1
#     return x
#
#
# num = int(input("How many primes do you want? "))
# i = 2
# c = 1
# while True:
#     if prime(i):
#         print(i)
#         c += 1
#     i += 1
#     if c > num:
#         break
# print("Feeling of vomiting")
# Returning the multiple values from a function
# def sum_sub(a, b):
#     """
#     This function returns results of addition and subtraction of a, b
#     """
#     c = a + b
#     d = a - b
#     return c, d
#
#
# x, y = sum_sub(10, 5)
# print(x)
# print(y)
# def sum_sub_mul_div(a, b):
#     c = a + b
#     d = a - b
#     e = a * b
#     f = a / b
#     return c, d, e, f
#
#
# w, x, y, z = sum_sub_mul_div(10, 5)
# print(w, x, y, z)
# Function as objects
# def display(word):
#     def message():
#         return 'How are you '
#
#     return message() + word
#
#
# x = display("Krishna")
# print(x)
# passing a function as a object
# def display(fun):
#     return 'Hai ' + fun
#
#
# def message():
#     return "How are you"
#
#
# print(display(message()))
# function returning a function
# def display():
#     def message():
#         return "How are you ?"
#     return message
#
# fun = display()
# print(fun())
# Function by reference
#
#
# def modify(x_):
#     """
#     Reassign a value to the variable
#     """
#     x_ = 15
#     print(x, id(x))
#
#
# x = 10
# modify(x)
# print(x, id(x))
# Modifying the Mutable elements
#
#
# def modify(list_):
#     """
#     This function appends a new value to the list
#     """
#     list_.append(9)
#     print(list_, id(list_))
#
#
# lst = [1, 2, 3, 4]
# modify(lst)
# print(lst, id(lst))
# doing the previous code with the new object list
#
#
# def modify(lst_):
#     """
#     This function creates a new object of the given object reference to the function
#     """
#     lst_ = [10, 11, 12]
#     print(lst_, id(lst_))
#
#
# lst = [1, 2, 3]
# modify(lst)
# print(lst, id(lst))
# Types of arguments there in a function
#
#
# def attach(s1, s2):
#     """
#     This function concat the two strings
#     """
#     s3 = s1 + s2
#     print("Total strings are ", s3)
#
#
# attach("New", "Delhi")
# Keyword arguments and Default arguments
#
#
# def grocery(items, price=50):
#     """
#     To display the given arguments
#     """
#     print("Item = %s" % items)
#     print("Price = %.2f" % price)
#
#
# items_price_grocery = {
#     'Sugar': 150.85,
#     'Sauce': 150,
#     'Milk': 100,
#     'Grain': 53.5
# }
#
# for item in items_price_grocery:
#     if item == 'Milk':
#         grocery(items=item)
#         continue
#     grocery(items=item, price=items_price_grocery[item])
# Variable length arguments
# def add(arg, *args):
#     """
#     To add the given the numbers
#     """
#     print('Formal argument: ', arg)
#
#     sums = 0
#     for i in args:
#         sums += i
#     print('Sum of all numbers: ', (arg + sums))
#
#
# add(5, 10)
# add(5, 10, 20, 30)
# **kwargs
# def display(args, **kwargs):
#     """
#     To display given values
#     """
#     print('Formal argument: ', args)
#     for x, y in kwargs.items():
#         print('Value = {}, Key = {}'.format(y, x))
#
#
# display(5, rno=10)
# print()
# display(5, rno=10, name='Prakash')
# Local and Global variables
# def my_functions():
#     a = 1
#     a += 1
#     print(a)
#
#
# my_functions()
# print(a)
# another way
# a = 1
#
#
# def my_functions_():
#     b = 2
#     print(a)
#     print(b)
#
#
# my_functions_()
# print(a)
# print(b)
# The Global Keyword
# a = 1
#
#
# def my_functions_global():
#     global a
#     a += 1
#     print('Global a = ', a)
#     return id(a)
#
#
# print('Global a = ', a)
# a_func = my_functions_global()
# print('Global a = ', a)
# global_a = id(a)
# if a_func == global_a:
#     print("Pointing to the same address")
# else:
#     print("No! They are not pointing to the same address")
# globals function and use case
# a = 1
#
#
# def my_functions_global_funct():
#     a = 2
#     x = globals()['a']
#     print('global variable x = ', x)
#     print('local variable a = ', a)
#
#
# my_functions_global_funct()
# print('global variable a = ', a)
# Passing a group of elements
# print("Enter the numbers by space:\n")
# lst = [int(x) for x in input().split()]
#
#
# def calculate(elements):
#     """
#     To find the sum and average of all the elements
#     """
#     n = len(elements)
#     sums = 0
#     avg = 0
#     for i in elements:
#         sums += i
#         avg = sums/n
#     return sums, avg
#
#
# x, y = calculate(lst)
# print("Total: ", x)
# print("Average: ", y)
#
# passing the elements which are going to be the group of strings
#
#
# def display(elements_of_string):
#     """
#     To display the strings of the elements_of_string
#     """
#     for i in elements_of_string:
#         print(i)
#
#
# print("Enter strings separated by commas: ")
# lst_strings = [x for x in input().split()]
# display(lst_strings)
# Recursive Functions code trying with new start with refresh and less time
# Finding factorial
#
#
# def factorial(n):
#     """
#     Finding the factorial of x
#     """
#     if n == 0:
#         result = 1
#     else:
#         result = n*factorial(n-1)
#     return result
#
#
# for i in range(1, 11):
#     print("Factorial of {} is {}".format(i, factorial(i)))
# Hanoi Towers
#
#
# def towers(n, a, b, c):
#     if n == 1:
#         print('Move disk to %i from pole %s to pole %s' % (n, a, c))
#     else:
#         towers(n-1, a, b, c)
#         print("Move disk to %i from pole %s to pole %s" % (n, a, c))
#         towers(n-1, b, c, a)
#
#
# n = int(input("Enter the number of disks: "))
# towers(n, 'A', 'C', "B")
# Anonymous function or lambdas
# y = lambda x: x * x
# print(type(y))
# f = lambda x: x * x
# print("Square of 5 ", f(5))
# g = lambda x,y: x + y
# print(g(1, 2))
# Max = lambda x, y: x if x > y else y
# a, b, = [int(n) for n in input("Enter two number").split(',')]
# print(Max(a, b))
# filter
#
#
# def is_even(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False


# lst = [i for i in range(100)]
# lst1 = list(filter(is_even, lst)) with normal def keyword
# lst1 = list(filter(lambda x: x % 2 == 0, lst))
# for i in lst1:
#     print(i)
# map
# lst = [1, 2, 3, 4, 5]
# lst1 = list(map(lambda x: x*x, lst))
# for i in lst1:
#     print(i)
# lst1 = [1, 2, 3, 4, 5]
# lst2 = [10, 20, 30, 40, 50]
# lst3 = list(map(lambda x, y: x*y, lst1, lst2))
# for i in lst3:
#     print(i)
# Reduce
# from functools import reduce
#
#
# lst = [1, 2, 3, 4, 5]
# result1 = reduce(lambda x, y: x*y, lst)
# result2 = reduce(lambda a, b: a+b, range(1, 51))
# print(result1)
# print(result2)
# Function decorator
# def decor(fun):
#     print(fun())
#     print(fun)
#
#     def inner():
#         value = fun()
#         return value + 2
#
#     return inner()
#
#
# def num():
#     return 10
#
#
# result_fun = decor(num)
# print(result_fun())
# with @ symbol
# def decor(fun):
#     def inner():
#         value = fun()
#         return value + 2
#     return inner
#
#
# @decor
# def num():
#     return 10
#
#
# print(num())
# @ multiple on single function
#
# def decor(fun):
#     def inner():
#         value = fun()
#         return value + 2
#
#     return inner
#
#
# def decor1(fun):
#     def inner():
#         value = fun()
#         return value * 2
#
#     return inner
#

# def num():
#     return 10
#
# @decor
# @decor1
# def num1():
#     return 10
#
#
# result_fun = decor(decor1(num))
# print(result_fun())
# print(num1())
# Generators in functions
# def mygen(x, y):
#     while x <= y:
#         yield x
#         x += 1
#
#
# g = mygen(50, 10000)
# for i in g:
#     print(i)
# l_gen = list(g)
# print(l_gen)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# Structured programming
# def da(basic):
#     da = basic * 80/100
#     return da
#
#
# def hra(basic):
#     hra = basic * 15/100
#     return hra
#
#
# def pf(basic):
#     pf = basic * 12/100
#     return pf
#
#
# def tax(gross):
#     tax = gross * 0.1
#     return tax
#
#
# basic = float(input("Enter the basic salary: "))
# gross = basic + da(basic) + hra(basic)
# print('Your gross salary: {:10.2f}'.format(gross))
# net = gross - pf(basic) - tax(gross)
# print("Your net salary: {:10.2f}".format(net))
# Creating our own modules in python
# from Employees import *
#
# basic = float(input("Enter the basic salary: "))
# gross = basic + da(basic) + hra(basic)
# print('Your gross salary: {:10.2f}'.format(gross))
# net = gross - pf(basic) - tax(gross)
# print("Your net salary: {:10.2f}".format(net))
# import one
#
# one.display()
