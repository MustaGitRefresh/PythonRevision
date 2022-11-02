# print()
# print("HELLO WORLD".lower())
# print()
# print('hello world'.upper())
# Using the escape characters with print function and its output
# print('\nAND\nThis is the first line')
# print('\nTab line \t tab')
# print('\\n gives the new line')
# print('\\t gives the tab')
# printing the string for multiple times as wished
# print('Something ' * 3)
# string concatenation with comma and the + operator
# print('City is ' + 'delhi')
# print('city name is =', 'newfoundland')
# printing string with variables and its values
# a, b = 2, 1
# print(a)
# print(b)
# print(a, b)
# # printing strings only
# print("Hello")
# print("Dear")
# print("How are you")
# print("Separators")
# print(a, b, sep=':')
# print(a, b, sep=',')
# print(a, b, sep='--------------------')
# End parameter of the print function
# if you pass any escape characters it will be in action
# print('Hello', end='')
# print(",How are you", end='')
# print(" Fine!", end='')
# The string would be ended with given end parameter
# print('Done', end='fire')

# any object can be print using print function and its elements
# wonder = [i for i in range(10)]
# print('\n')
# print(wonder)
#
# print()
# b = 24
# print(b, 'is the even number')
# print((b / 2), 'is the even number')
# print('The value total is ', (2 + 4))
# % operator for formatting the string output in the print function
# print('Hello %d' % b)
# print("How are you %s" % wonder) This will not throw an error because list is acceptable
# but %d will not work with list it only require a integer number otherwise
# TypeError: % d
# format: a
# number is required, not list
# a, b = 1, 2
# This will not work without parenthesis for more than one values for the string formation.
# print('x and y is %d %d' % a, b)
# print('x and y is %d %d' % (a, b))
# name = "Linda" # declaring the variable with value Linda
# print('Hi %s ' % name)  # %s for printing the string
# print('Hi |%20s|' % name)
# print('Hi |%-20s|' % name)

# printing the characters by formatting the string
# name, salary = 'Ravi', 12500.75
# print('Hello, {} your salary is {}'.format(name, salary))
# print('Hello, {0} your salary is {1}'.format(name, salary))
# print('Hello, {n} your salary is {s}'.format(n=name, s=salary))
# print('Hello, {:s} your salary is {:.2f}'.format(name, salary))
# print('Hello, %s your salary is %.2f' % (name, salary))
# INPUTS Statements

# print(input()) This takes the input from the user and returns it in the form of the string
# string = input()  # Can be stored in the variable
# print(string)
# number = int(input("Enter the number:\n"))
# number = float(input("Enter the number:\n"))
# print(number)
# character = input("Enter the string:\n")
# print("You entered:" + character)
# print("You entered:", character)
# print("You entered:", character[0])
# Taking the two input from the user and display it
# x = int(input("Enter the number:\n"))
# y = int(input("Enter the number:\n"))
# print('The entered value are %d, %d, %d' % (x, y, x+y))
# print('The entered value are {} {} and the sum is  {}'.format(x, y, x+y))
# print('The sum of', x, 'and', y, 'is', x+y)
# print('The entered value are %d, %d, %d' % (x, y,  x*y))
# print('The entered value are {} {} and the product is  {}'.format(x, y, x*y))
# print('The sum of', x, 'and', y, 'product is', x*y)
# Python Program to convert numbers from other systems into decimal number system.
# input_str = input("Enter the hexadecimal number:\n")
# print(int(input_str, 16))  It will only convert the characters into hexadecimal till value 16 only till 'f'
# n = int(input_str, 16)
# print('Hexadecimal to Decimal = ', n)
# input_str = input("Enter the Octal number:\n")
# n = int(input_str, 8)
# print('Octal to Decimal = ', n)
# input_str = input("Enter the Binary number:\n")
# n = int(input_str, 2)
# print('Binary to Decimal = ', n)
# Accepting the numbers in the list and giving the sum total of the list elements as output
# total_numbers = [int(x) for x in input("Enter the number:\n").split()]
# total_numbers = [int(x) for x in input("Enter the number:\n").split(',')]
# var1, var2, var3 = total_numbers
# print('Sum = ', var1+var2+var3)
# print("Sum is {}".format(sum(total_numbers)))
# Now here taking the string as input and splitting it with comma and store it in a list
# total_strings = [x for x in input("Enter the names:\n").split(',')]
# print('You entered this names')
# for i in total_strings:
#     print(i)
# Eval function introduction
# a, b = 5, 10
# print(eval('a+b-4'))
# import sys
#
#
# def sum_doer(number):
#     return int(number)
#
#
# args = sys.argv[1:]
# print(args)
# print(sum(list(map(sum_doer, args))))
# import argparse
#
# parser = argparse.ArgumentParser(description='This code is an example')
# parser.add_argument('num', type=int, help='Please input the integer type number')
# parser.add_argument('num1', type=int, help='Please input the integer type number')
# args = parser.parse_args()
# print(int(args.num)+int(args.num1))
