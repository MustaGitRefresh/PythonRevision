# This all are compiled time errors
# x = 10
# raises SyntaxError
# if x == 1
#     print("where is colon?")
# if x % 2 == 0:
#     print('x is divisible')
#         print("Note")
# RuntimeErrors
# TypeError
# def concat(a, b):
#     print(a+b)
#
#
# concat('Hai', 22)
# IndexError
# animal = ['dog', 'cat', 'Horse', 'Donkey']
# print(animal[4])
# LogicalErrors
# def increment(sal):
#     # sal = sal * 15/100 This produce different answer
#     sal = sal + sal * 15/100
#     return sal
#
#
# sal = increment(5000.00)
# print("incremented salary", sal)
# Understanding it causes
# f = open('my file.txt', 'w')
# a, b = [int(x) for x in input("enter two numbers: ").split()]
# c = a/b
# f.write("writing %d into my file" %c)
# f.close()
# improvement with exception
# f = open('my file.txt', 'w')
# try:
#     a, b = [int(x) for x in input("enter two numbers: ").split()]
#     c = a / b
#     f.write("writing %d into my file" %c)
#
# except ZeroDivisionError:
#     print("'Division by zero is not allowed")
#     print("Do not enter 0 in input")
#
# finally:
#     f.close()
#     print("file closed")
# Python program to handle syntax error given by eval functions
# try:
#     date = eval(input("Enter date: "))
#
# except SyntaxError:
#     print("Invalid date")
#
# else:
#     print("You entered: " , date)
# A python program to handle IOError produces by open function
# solve the f is not defined
# try:
#     name = input("Enter the filename: ")
#     f = open(name, 'r')
# except IOError as e:
#     print('File not found: ', name)
#     f.close()
# else:
#     n = len(f.readlines())
#     print(name, 'has', n, 'lines')
# finally:
#     f.close()
# A python program to handle multiple exceptions
# def avg(list):
#     tot = 0
#     for x in list:
#         tot += x
#     avg = tot/len(list)
#     return tot, avg
#
#
# try:
# t,a = avg([1, 2, 3, 4, 5])
# t, a = avg([]) # ZeroDivisionError, Please do not give empty list
# t, a = avg([1, 2, 3, 4, 5, 'a']) # Type Error, Please provide numbers,
#     print('Total = {}, Average = {}'.format(t, a))
# except TypeError:
#     print("Type Error, Please provide numbers, ")
# except ZeroDivisionError:
#     print('ZeroDivisionError, Please do not give empty list')
# The Except block
# try:
#     a = int(input("Enter the number:\n"))
# except Exception as e:
#     print(e)
# try block without catching the exceptions
# try:
#     x = int(input("Enter a number:\n"))
#     y = 1 / x
# finally:
#     print('we are not catching the exceptions:')
# print(f"The inverse of {x} is {y}")
# The assert statement
# try:
#     x = int(input("Enter the number between 5 and 10: "))
#     assert x >= 5 and x <= 10
#     print('the number which entered: ', x)
# except Exception as e:
#     print("The condition is not fulfilled")
# The another way with the message parameter
# try:
#     x = int(input("Enter the number between 5 and 10: "))
#     assert x >= 5 and x <= 10, "Your input is incorrect"
#     print('the number which entered: ', x)
# except Exception as e:
#     print(e)
# creating the User-defined exceptions
# class MYExceptions(Exception):
#     def __init__(self, arg):
#         self.msg = arg
#
# def check(dict):
#     for k, v in dict.items():
#         print("Name = {:15s} Balance = {:10.2f}".format(k, v))
#         if v < 2000.00:
#             raise MYExceptions("Balance amount is less in the account "+k)
#
#
# bank = {
#     'Raj': 15000.00,
#     'Van': 8900.50,
#     'Naresh': 3000.00,
#     'Ajay': 1990.00,
# }
#
#
# try:
#     check(bank)
# except MYExceptions as me :
#     print(me)
# Logging the exceptions
# import logging

# logging.basicConfig(filename='my file.txt', level=logging.INFO)
# logging.error('There is an error in the program')
# logging.critical("There is a problem in the design")
# logging.warning("The project is going slow")
# logging.info('You are a junior programmer')
# logging.debug('Line no. 10 contains syntax error.')

# logging with exceptions
# import logging

# logging.basicConfig(filename='my file.txt', level=logging.ERROR)

# try:
#     a = int(input("Enter the number: \n "))
#     b = int(input("Enter the number:\n"))
#     c = a/b
# except Exception as e:
#     logging.exception(e)
# else:
#     print("the result is {}".format(c))
