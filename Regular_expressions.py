# Regular expressions
#
# print('This is normal\nString')
# print(r'This is normal\nString')
# Example 1 of re-import regular_expression
#
# here it can be any word until and unless it is there in the string otherwise None will be returned
# prog = re.compile(r'm\w\w')
# string_re = 'cat mat bat'
# result = prog.search(string_re)
# print(result.group())
#
# string_re1 = 'Operating System Format'
# result = prog.search(string_re1)
# print(result.group())
# Program 1
# import re
#
# string_ = 'man sun mop run'
# result = re.search(r'm\w\w', string_)
# if result:
#     print(result.group())
# Program 2 using findall method
# import re
#
# string_ = 'man sun mop run'
# result = re.findall(r'm\w\w', string_)
# print(result)
# displaying the elements using for loop
# for i in result:
#     print(i)
# Program 3&4 using match method
# import re
#
# string_ = 'man sun mop run'
# if this is searched using match method it will return None as it is not in the beginning of the string ⬇
# string_1 = 'pan sun mop run'
# result = re.match(r'm\w\w', string_)
# print(result.group())
# Program 5 using split method
# import re
#
# string_ = 'This; is the: "Core" Python\'s book'
# result = re.split(r'\W+', string_)
# print(result)
# Program 6 python program to replace the string with content with new string
# import re
#
# string_ = 'Kumbhmela will be conducted at Ahmedabad in India'
# res = re.sub(r'Ahmedabad', 'Allahabad', string_)
# print(res)
# Program 7&7.1 all words starting with a
# import re
#
# string_ = 'an apple a day keeps the doctor away'
# result = re.findall(r'a[\w]*', string_)
# result = re.findall(r'\ba[\w]*\b', string_)
# for word in result:
#     print(word)
# Program 8 python program to create a regular expression to retrieve all words starting with a numeric digit
# import re
#
# string_digit_start = 'The meeting will be conducted on 1st and 21st of every month'
# result = re.findall(r'\d[\w]*', string_digit_start)
# for word in result:
#     print(word)
# Program 9 python program to retrieve all words having 5 characters length
# import re
#
# string_char = 'one two three four five six seven 8 9 10'
# result = re.findall(r'\b\w{5}\b', string_char)
# print(result)
# Program 10 python program to retrieve all words having 5 characters length using search method
# import re
#
# string_char = 'one two three four five six seven 8 9 10'
# result = re.search(r'\b\w{5}\b', string_char)
# print(result.group())
# Program 11 retrieving all the words that are having the length at least 4 characters
# import re
#
# string_ = 'one two three four five six seven 8 9 10'
# result = re.findall(r'\b\w{4,}\b', string_)
# print(result)
# Program 12 retrieving all the words that are having the length at least 3 or more 5 characters
# import re
#
# string_ = 'one two three four five six seven 8 9 10'
# result = re.findall(r'\b\w{3,5}\b', string_)
# print(result)
# Program 13 retrieving all the words that are having the length at least 4 characters
# import re
#
# string_ = 'one two three four five six seven 8 9 10'
# result = re.findall(r'\b\d\d\b', string_)
# print(result)
# Program 14 python program to create a regular expression to retrieve a last word of a string if it starts with t.
# import re
#
# string_ = 'one two three one two three'
# result = re.findall(r't[\w]*\Z', string_)
# print(result)
# Program 15&16 python program to create a regular expression to retrieve the phone number of a person
# import re
#
# string_ = 'Nagwares Rao: 9706612345'
# res = re.search(r'\d+', string_)
# print(res.group())
# res = re.search(r'\D+', string_)
# print(res.group())
# Program 17 python program to find all the words starting with an or ak
# import re
#
# string_ = 'anil akhil anent arun arith hardhat hijab rank'
# res = re.findall(r'a[nk][\w]*', string_)
# print(res)
# Program 18 python program to retrieve the dates from the strings
# import re
#
# string_dates = 'Vijay 20 1-5-2001, Rohit 21 22-10-1990, Sita 22 15-09-2000'
# res = re.findall(r'\d{2}-\d{2}-\d{2}', string_dates)
# res = re.findall(r'\d{1,2}-\d{1,2}-\d{1,2}', string_dates)
# print(res)
# Program 19&20&21 python program to create a regular expression to search whether the string is starting with He
# import re
#
# string_he = 'Hello World'
# res = re.search(r'^He', string_he)
# res = re.search(r'World$', string_he)
# There is a solution of using re.IGNORE CASE
# res = re.search(r' world $', string_he, re.IGNORE-CASE)  # This is getting confuse between the case of the word
# if res:
# print("String starts with 'He'")
# print("String ends with World")
# else:
# print("String does not starts with 'He'")
# print("String does not ends with World")
# Program 22 python program to create a regular expression to retrieve marks and ames from a given string
# import re
#
# string_names = "Rahul got 75 marks, Vijay got 55 marks, whereas Suburb got 98 marks"
# marks = re.findall(r'\d{2}', string_names)
# print(marks)
# names = re.findall(r'[A-Z][a-z]*', string_names)
# print(names)
# Python 23 program to retrieve the timings which is either am or pm
# import re
#
#
# string_times = "The meeting may be at 8am or 9am or 4pm or 5pm"
# res = re.findall(r'\dam|\dpm', string_times)
# print(res)
# Python program 24 that reads the mails.txt and search the mails from that file
# import re
#
# f = open('mails.txt', 'r')
# res = None
# for line in f:
#     res = re.findall(r'\S+@\S+', line)
# if len(res)>0:
#     print(res)
# f.close()
# Python program 25 searching the salaries.txt and writing it into the newfile.txt
# import re
#
# f1 = open('salaries.txt', 'r')
# f2 = open('newfile.txt', 'w')
# for line in f1:
#     res1 = re.search(r'\d{4}', line)
#     res2 = re.search(r'\d{4,}.\d{2}', line)
#     print(res1.group(), end='\t')
#     print(res2.group())
#     f2.write(res1.group() + '\t')
#     f2.write(res2.group() + '\n')
#
# f1.close()
# f2.close()
# Retrieving information from a HTML File
# import re
# import urllib.request
#
# f = urllib.request.urlopen(r' file:///E|Python Revise\breakfast.html')
# text = f.read()
# string_format = text.decode()
# result = re.findall(r'<td>\w+</td>\s<td>(\w+)</td>\s<td>(\d\d.\d\d)</td>', string_format)
# print(result)
# for item, price in result:
#     print('Item= %-15s Price= %-10s' % (item, price))
# f.close()
