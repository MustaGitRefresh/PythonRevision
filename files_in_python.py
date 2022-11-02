# Working with text files

# Program 1 to write into a file
# f = open('my file.txt', 'w')
# string_user = input("Enter the text:\n")
# f.write(string_user)
# f.close()
# Program 2 to read a file
# f = open("my file.txt", 'r')
# string_text = f.read() without mentioning the bytes
# string_text = f.read(4)  # mentioning the bytes
# f.close()
# print(string_text)
# Program 3 working with the text files containing strings
# Somehow storing the group of strings is not working
# f = open("my file.txt", 'w')
# print("Enter the text: (@ at the end) ")
# string_user = input()
# while string_user != '@':
#     string_user = input()
#     if string_user != '@':
#         f.write(string_user + '\n')
# f.close()
# Program 3 program to read all the strings from the text file and display them
# f = open('my file.txt', 'r')
# print('The file contents are:')
# str = f.read()
# print(str)
# print(f.readlines())
# print(str.splitlines())
# Python program 5 to append data to an existing fle and then displaying it into the screen
# f = open('my file.txt', 'a+')
# string_user = input()
# while string_user != '@':
#     if string_user != '@':
#         f.write(string_user + '\n')
#         continue
# f.seek(0, 0)
# print("The file contents are :")
# string_read = f.read()
# print(string_read)
# f.close()
# Knowing whether the file exists or not
# import os
# import sys

# file_name = input("Enter the file name:\n")
# if os.path.isfile(file_name):
#     f = open(file_name, 'r')
# else:
#     print(file_name + "does not exists")
#     sys.exit()

# print('The file contents are: ')
# string_user = f.read()
# print(string_user)
# f.close()
# Program 7 in which we will use a logic to get total numbers of characters, words and the lines
# import sys
# import os

# file_name = input("Enter the file name:\n")
# if os.path.exists(file_name):
#     f = open(file_name, 'r')
# else:
#     print(file_name, "does not exists")
#     sys.exit()


# cl = cw = cc = 0
# for line in f:
#     words = line.split()
#     cl += 1
#     cw += len(words)
#     cc += len(line)

# print('No. of lines: ', cl)
# print('No. of words: ', cw)
# print('No. of characters: ', cc)
# Working with binary files

# f1 = open("good_morning.jpg", 'rb')
# f2 = open("new.jpg", 'a+b')

# bytes_ = f1.read()
# f2.write(bytes_)
# f2.write(bytes(23))
# print(f2.read())
# f1.close()
# f2.close()
# The with statement
# program 9
# with open('sample.txt', 'w') as f:
#     f.write('I am a learner\n python is attractive\n')
#
# Program 10
# with open('sample.txt', 'r') as f:
#     for i in f:
#         print(i)
# The pickle module
# Program 11 in the Emp file of python
# program 12
# import Emp
# import pickle
#
# f = open('emp.dat', 'wb')
# n = int(input("How many employees? "))
# for i in range(n):
#     emp_id = int(input("Enter id: "))
#     name = input("Enter name: ")
#     salary = float(input("Enter salary: "))
#
#     e = Emp.Emp(emp_id, name, salary)
#     pickle.dump(e, f)
# f.close()
# program 13 unpickling the pickle object
# import pickle
#
# f = open('emp.dat', 'rb')
# print("The details of the employees")
# while True:
#     try:
#         obj = pickle.load(f)
#         obj.display()
#     except EOFError:
#         print("End of file reached...")
#         break
#
# f.close()
# The seek and tell methods
# program no numbers
# with open('line.txt', 'r+b') as f:
#     f.write(b'Amazing python')
#     f.seek(3)
#     print(f.read(2))
#     print(f.tell())
#     f.seek(-6, 2)
#     print(f.read(1))
#     print(f.tell()
# Random Accessing of the binary files
# Program 14 python program to create a binary file and store the data
# rec_len = 20
# with open('cities.bin', 'wb') as f:
#     n = int(input("How many entries? "))
#     for i in range(n):
#         city = input("Enter city name: ")
#         ln = len(city)
#         city = city + (rec_len - ln) * ' '
#         city = city.encode()
#         f.write(city)
# Program 15 python program to randomly accessing a record from a binary file
# rec_len = 20
# with open('cities.bin', 'rb') as f:
#     n = int(input("Enter record number: "))
#     f.seek(rec_len * (n-1))
#     string_data = f.read(rec_len)
#     print(string_data.decode())
# Program 16 python program to search for city name in the file
# import os
#
# rec_len = 20
# size = os.path.getsize('cities.bin')
# print(f'Size of the file {size} bytes')
# n = int(size/rec_len)
# print('No. of records = {}'.format(n))
# with open('cities.bin', 'rb') as f:
#     name = input("Enter the city name: ")
#     name = name.encode()
#     position = 0
#     found = False
#     for i in range(n):
#         f.seek(position)
#         string_data = f.read(20)
#         if name in string_data:
#             print('Found at record no: ', (i+1))
#             found = True
#         position += rec_len
#
#     if not found:
#         print('City not found')
# Program 17 python program to update or modify a record a binary file
# import os
#
# rec_len = 20
# size = os.path.getsize('cities.bin')
# print(f'Size of the file {size} bytes')
# n = int(size/rec_len)
# print('No. of records = {}'.format(n))
# with open('cities.bin', 'r+b') as f:
#     name = input("Enter city name: ").encode()
#     new_name = input("Enter the new city name: ")
#     ln = len(new_name)
#     new_name = new_name.encode()
#     position = 0
#     found = False
#     for i in range(n):
#         f.seek(position)
#         string_data_updating = f.read(20)
#         if name in string_data_updating:
#             print(f"Updated record no: {i+1}")
#             found = True
#             f.seek(-20, 1)
#             f.write(new_name)
#         position += rec_len
#     if not found:
#         print('CIty not found')
# Program 18 python program to delete a specific record from the binary file
# import os
#
# rec_len = 20
# size = os.path.getsize('cities.bin')
# n = int(size/rec_len)
# f1 = open('cities.bin', 'rb')
# f2 = open('file2.bin', 'wb')
# city = input("Enter city name to delete: ")
# ln = len(city)
# city = city + (rec_len-ln) * " "
# city = city.encode()
# for i in range(n):
#     string_data_delete = f1.read(rec_len)
#     if string_data_delete != city:
#         f2.write(string_data_delete)
# print('Record deleted: ')
# f1.close()
# f2.close()
# os.remove('cities.bin')
# os.rename('file2.bin', 'cities.bin')
# Random Accessing of Binary Files using mmap
# with open('phonebook.dat', 'wb') as f:
#     n = int(input("How many entries: "))
#     for i in range(n):
#         name = input("Enter the name: ").encode()
#         phone = input("Enter the phone number: ").encode()
#         f.write(name+phone)
# Program 20 python program to use mmap and performing various operations on a binary file
# import mmap, sys
#
# print('1 to display all the entries')
# print('2 to display phone number')
# print('3 to modify an entry')
# print('4 Exit')
# choice_user = input("Your choice: ")
# if choice_user == '4':
#     sys.exit()
#
# with open('phonebook.dat', 'r+b') as f:
#     mm = mmap.mmap(f.file-no(), 0)
#     if choice_user == '1':
#         print(mm.read().decode())
#     if choice_user == '2':
#         name = input("Enter name: ")
#         n = mm.find(name.encode())
#         n1 = n + len(name)
#         ph = mm[n1: n1 + 10]
#         print('Phone no: ', ph.decode())
#     if choice_user == '3':
#         name = input("Enter name: ")
#         n = mm.find(name.encode())
#         n1 = n + len(name)
#         ph1 = input('Enter new  phone number: ')
#         mm[n1: n1 + 10] = ph1.encode()
#
# mm.close()
# Zipping and Unzipping
# Program 21 python program to make a zip file
# import zipfile
#
# f = zipfile.ZipFile('test.zip', 'w', zipfile.ZIP_DEFLATED)
# f.write('arrays.py')
# f.write('Objects_classes.py')
# f.write('teacher.py')
# f.write('datatypes.py')
# f.close()
# Program 22 python program to unzip the file
# from zipfile import *
#
# z = ZipFile('test.zip', 'r')
# z.extractall()
# Working with directories
# Program 23 python program to know the currently working directory
# import os
#
# current = os.getcwd()
# print(current)
# Python program 24 python program to create a sub directory
# import os
#
# os.mkdir('my_sub')
# os.mkdir('my_sub/my_sub2')
# Python program 25 python program to create a sub directory using mkdirs
# import os
#
# os.makedirs('new_sub/new_sub2')
# os.mkdir('new_sub/new_sub2') This wil throw an error
# Program 26 python program to change the another directory
# import os
#
# os.chdir('my_sub/my_sub2')
# current = os.getcwd()
# print(current)
# python program to remove the directory from the area
# import os
#
# os.rmdir('/my_sub/my_sub2') This will only remove the last inner directory
# os.removedirs('my_sub/my_sub2') This will remove all the parent and inner directories
# Program 29 to rename the a directory and a file
# import os
#
# os.rename('PyPackage', 'PYPACK')
# Python program 30 python program to display all the contents of the current directory
# import os
#
# for dir_path, dir_names, file_names in os.walk('.'):
#     print(dir_path)
#     print(dir_names)
#     print(file_names)
#     print()
# Running other program from python program
# program 31 system function usage
# import os
#
# os.system('dir')
# os.system('python files_in_python.py')
# os.system('dir *.py')
