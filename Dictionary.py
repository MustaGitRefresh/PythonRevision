# Starting with Chapter 11 dictionaries
# basic dictionary
# dictionary_emp = {
#     'Name': 'Chandra',
#     'ID': 200,
#     'Salary': 9800.5
# }
# print('Name of employee = ', dictionary_emp['Name'])
# print('ID of employee = ', dictionary_emp['ID'])
# print('Salary of employee = ', dictionary_emp['Salary'])
# Operations on the dictionary
# finding the total numbers of key and value pairs in the dictionary
# n = len(dictionary_emp)
# print('No. of key-value pairs in dictionary = ', n)
# Updating the existing key value by this below code
# dictionary_emp['Salary'] = 10000.75
# Adding a new key with a new value using the below code
# dictionary_emp['Department'] = 'Finance'
# print(dictionary_emp)
# deleting the key and its value
# del dictionary_emp['ID']
# print(dictionary_emp)
# Checking whether key is there or not in the dictionary
# print('Department' in dictionary_emp)
# print('Gender' in dictionary_emp)
# print('Gender' not in dictionary_emp)
# Adding similar key will override the previous one by the new one. Key must be unique
# dictionary_emp['Name'] = 'Rahul'
# print(dictionary_emp)
# key cannot be mutable object like list or dict but string or int etc.
# dictionary_emp[['WHrs']] = 8
# print(dictionary_emp)
# Methods for dictionary manipulations
# printing entire dictionary
# print(dictionary_emp)
# displaying only keys
# print('keys in dictionary: ', dictionary_emp.keys())
# displaying only values
# print('Values in dictionary: ', dictionary_emp.values())
# display both key and value pairs as tuples
# print('Items in dictionary: ', dictionary_emp.items())
# Taking a dictionary and input and giving the user the sum of all the numerics values in the dict
# dictionary_sum = eval(input("Enter the elements in {}: "))
# s = sum(dictionary_sum.values())
# print('Sum of the values in the dictionary: ', s)
# creating a dictionary from the keyboard inputted values
# x = {}
# print('How many elements? ', end='')
# n = int(input())
# for i in range(n):
#     print("Enter the key: ", end='')
#     k = input()
#     print("Enter the Value: ", end='')
#     v = int(input())
#     x.update({k: v})
#
# print('The dictionary is: ', x)
# Making a dictionary from the user given cricket players runs and their names.
# Allowing the user to do the search operation on it
# x = {}
# print('How many players? ', end='')
# n = int(input())
# for i in range(n):
#     print("Enter the player name: ", end='')
#     k = input()
#     print("Enter the player runs: ", end='')
#     v = int(input())
#     x.update({k: v})
#
# print('\nPlayers in this match: ')
# for player_name in x.keys():
#     print(player_name)
#
# print('Enter player name: ', end='')
# name = input()
# runs = x.get(name, -1)
# if runs == -1:
#     print('Player not found')
# else:
#     print('{} made runs {}'.format(name, runs))
# Using for loop with dictionaries
# colors = {'r': 'Red', 'g': 'Green', 'b': 'Blue', 'w': 'White'}
# getting the keys and the values both using the for loop
# for k in colors:
#     print(k)
#     print(colors[k])
# getting both values and keys
# for k, v in colors.items():
#     print(f'Key = {k} Value = {v}')
# finding the total occurrence of the letters using dictionary
# dict_string = {}
# string_word = "Book"
# for x in string_word:
#     dict_string[x] = dict_string.get(x, 0) + 1
#
# print(dict_string)
# Finding how many times each letter found in the string
# string_book = 'Book'
# dict_string_occurrence = {}
# for x in string_book:
#     dict_string_occurrence[x] = dict_string_occurrence.get(x, 0) + 1
#
# for k, v in dict_string_occurrence.items():
#     print(f"Key = {k}\t Its occurrences = {v}")
# Sorting the dictionary using the lambda expression
# colors = {
#     10: "Red",
#     35: "Green",
#     15: "Blue",
#     25: "White"
# }
#
# c1 = sorted(colors.items(), key=lambda t: t[0])
# c2 = sorted(colors.items(), key=lambda t: t[1])
# print(c1)
# print(c2)
# Converting the list into a dictionary
# countries = ["USA", "India", "Germany", "France"]
# cities = ["Washington", "New Delhi", "Berlin", "Paris"]
# z = zip(countries, cities)
# dict_countries_cities = dict(z)
# print("{:15s} --{:15s}".format('COUNTRY', 'CAPITAL'))
# for k in dict_countries_cities:
#     print("{:15s} --{:15s}".format(k, dict_countries_cities[k]))
# Converting strings into dictionary
# string_details = "Vijay=23, Ganesh=20, Lakshmi=19, Nikhil=22"
# lst_strings = []
# for x in string_details.split(','):
#     y = x.split('=')
#     lst_strings.append(y)
#
# d_strings = dict(lst_strings)
# d1 = {}
# for k, v in d_strings.items():
#     d1[k] = int(v)
#
# print(d1)
# Passing the dictionary to the function
# def fun(dictionary):
#     for i, j in dictionary.items():
#         print(i, '--', j)
#
#
# d = {'a': "Apple", 'b': "Book", 'c': "Cook"}
# fun(d)
# Ordered dictionaries
# from collections import OrderedDict
#
# d = OrderedDict()
# d[10] = 'A'
# d[11] = 'B'
# d[12] = 'C'
# d[13] = 'D'
# 
# for i, j in d.items():
#     print(i, j)
