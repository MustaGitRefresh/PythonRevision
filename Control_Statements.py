# This was my try of control statements in sublime text 4.
# it is very good for beginners and intermediate user very much kind like VS Code
# control = 2

# for i in range(control):
# 	print(i)
# 	if i == 2:
# 		break
# 	else:
# 		print(i)
# 		continue
# else:
# 	print("The for loop is ended with condition")
# Practice starts here down below
# import math

# r = float(input("Enter the input radius:\n"))
# area = math.pi * (r**2)
# print(area)
# if else condition starts here down
# num = 1
# if num == 1:
# 	# all the group of statement is called 'suite' in python Indentation is required
# 	print("One")
# string_yes-no = 'yes' this will not work because of the - operator or minus operator in the variable name
# string_yes_no = 'yes'
# if string_yes_no:
# 	print("Yes")
# 	print("This what you said")
# 	print("Your response is good")
# very important
# This will work on the value of the variable
# x, y = 1, 0
# if x == 1:
# 	print('a')
# 	print('b')
# 	if y == 2:
# 		print('c')
# 		print('d')
# print('end')
# if with else
# number = 10
# number = int(input("Enter the number for checking:\n"))
# if number % 2 == 0:
# 	print(f"{number} is Even")
# else:
# 	print(f"{number} is Odd")
# Compound conditions with if and else
# x = int(input("Enter the number:\n"))
# if x >= 1 and x <= 10:
# 	print("The number {} is inclusive".format(x))
# else:
# 	print("The number {} is exclusive".format(x))
# if elif and else
# num = 5
# num = int(input("Enter the number:\n"))
# if num == 0:
# 	print(num, 'is Zero')
# elif num > 0:
# 	print(num, 'is Positive')
# else:
# 	print(num, 'is negative')
# put it in correct order and it is for printing the corresponding names of the number
# x = int(input("enter the number:\n"))
# if x == 0: print('One')
# elif x == 1: print('Two')
# elif x == 2: print('Three')
# elif x == 3: print('Four')
# elif x == 4: print('Five')
# elif x == 5: print('Six')
# elif x == 6: print('Seven')
# elif x == 7: print('Eight')
# elif x == 8: print('Nine')
# elif x == 9: print("Ten")
# else: print("Please enter digit between 0 and 9")
# import os
# path = r"E:\Python Revise"
# if os.getcwd() == path:
# 	print("Both are same")
# The While Loop
# printing 1 to 10
# a = 1
# while a <= 10:
# 	print(a)
# 	a+=1
# 	print("End")
# Even number printing
# a = 100
# while a>=100 and a<=200:
# 	print(f"{a} is even")
# 	a+=2
# making a program for printing the numbers between the user given input and if it is even than starting from there else starting by incrementing
# m, n = [int(i) for i in input("Enter the maximum and the minimum range:").split(',')]
# y = m

# if y % 2 != 0:
# 	y += 1

# while y>=m and y<=n:
# 	print(f"{y}")
# 	y+=2
# for loop
# string = 'Hello'
# for ch in string:
# 	print(ch)
# print(type(range(1, 10))) printing type of range function but it is a class
# string = 'Hello'
# n = len(string)
# for i in range(n):
# 	print(string[i])
# for i in range(10, 0, -1):
# 	print(i)
# list_ = [10, 20.5, 'A', "America"]
# for i in list_:
# 	print(i)
# numbers = [10, 20, 30, 40, 50]
# sums = 0
# for i in numbers:
# 	print(i)
# 	sums += i
# print(f"{sums} is the total of the numbers")
# i = 0
# while i< len(numbers):
# 	print(numbers[i])
# 	sums+= numbers[i]
# 	i+=1
# print(f"{sums} is the total of the numbers")
# nested loops
# for i in range(3):
# 	for j in range(4):
# 		print(f"i={i} and j={j}")
# print("for the loop")
# print('done')
# printing the stars and the patterns
# Logic
# for i in range(10):
# 	for j in range(1, i+1):
# 		print('*', end='')
# 	print()
# for i in range(11):
# 	print("*"*i)
# n = 40
# for i in range(11):
# 	print(' '*n, end='')
# 	print("* "*i)
# 	n-=1
# for i in range(11):
# 	print(' '*(n-i) + '* '*i)
# printing the 100 in 10 rows and their products
# Logic
# for x in range(1, 11):
# 	for y in range(1, 11):
# 		print(x*y, end='')
# 		print('{:8}'.format(x*y), end='')
# 	print()
# element finding the else suite with the for and while loops
# a = [int(i) for i in range(1, 6)]
# print(a)
# element = int(input("Enter the value to find:\n"))
# for i in a:
# 	if i == element:
# 		print("Element found")
# 		break
# else:
# 	print("Element not found")
# Break statement
# x = 10
# while x>=1:
# 	print('x = ', x)
# 	if x == 5:
# 		break
# 	x-=1
# Continue statement
# x = 0
# while x < 10:
# 	x+=1
# 	if x > 5:
# 		continue
# 	print('x = ', x)
# print("ENd")
# Pass statement
# x = 0
# while x<10:
# 	x+=1
# 	if x>5: # if x > 5 then continue next iteration
# 		pass
# 	print('x =', x)
# print("Out of the loop")
# getting the use of the pass statement
# numbers = [1, 2, 3, -4, -5, -6, -7, 8, 9]
# for i in numbers:
# 	if not i>0
# 	if i>0:
# 		pass
# 	else:
# 		print(i)
# x = int(input("User enter the number:\n"))
# assert x>0, 'Wrong input entered'
# print('U entered:', x)
# try:
# 	assert x>0
# 	print('U entered:', x)
# except AssertionError as e:
# 	print("Wrong input entered")
# The return statement in control statements
# def sum(a, b):
# 	return f'Sum = {a+b}'

# print(sum(1, 2))
# Upto what number and finding prime number
# maxs = int(input("Enter the max number limit:\n"))
# for i in range(2, maxs+1):
# 	print(i)
# 	for j in range(2, i):
# 		print(j)
# 		if j % j == 0:
# 			break
# 		else:
# 			print(i)
# Fibonacci series
# n = int(input("How many Fibonaccis?:\n"))
# print('='*10)
# f1 = 0
# f2 = 1
# c = 2
# if n==1:
# 	print(f1)
# elif n==2:
# 	print(f2)
# else:
# 	print("{}\n{}".format(f1, f2), sep='')
# 	while c<n:
# 		f= f1 + f2
# 		print(f)
# 		f1, f2 = f2, f
# 		c+=1
# For generating the alphabets using loop use the module String
