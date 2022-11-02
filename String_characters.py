# string_triple_quotes = '''
#             Welcome to core python, a book on python language that discusses all important
#             concepts of python in a lucid
#             and comprehensive manner
#         '''
# strings_with_multiple_quotes = 'The hello world "in python"' # and quotes can be use vice versa
# Escape characters
# a = 'a'
# b = 'b'
# print(f'Bell or alert {a}\a{b}')
# print(f'Backspace {a}\b{b}')
# print(f'New line {a}\n{b}')
# print(f'Horizontal tab space {a}\t{b}')
# print(f'Vertical tab space {a}\v{b}')
# print(f'Enter button {a}\r{b}')
# # print(character x {a}\x{b}) This throws error
# print(f'Displays single \\ {a}\\{b}')
# printing the core python in hindi many possibilities are there
# name = u'\u0912\u095b\u0930 \u092b\u0950\u0925\u0964\u0928'
# print(name)
# getting the length of the string
# string_ = 'core python'
# print(len(string_))
# Indexing the string
# string = 'core python'
# n = len(string)
# i = 0
# while i < n:
#     print(string[i], end=' ')
#     i += 1
# print()
# i = -1
# while i >= -n:
#     print(string[i], end=' ')
#     i -= 1
# print()
# i = 1
# n = len(string)
# while i <= n:
#     print(string[-i], end='')
#     i += 1
# for i in string:
#     print(i, end='')
# print('\n new')
# for i in string[::]:
#     print(i, end='')
# print("\n new")
# for i in string[::-1]:
#     print(i, end='')
# Slicing the strings
# string_python = 'core python'
# print(string_python[0:9:2])
# print(string_python[::])
# print(string_python[2:4:1])
# print(string_python[::2])
# print(string_python[2::])
# print(string_python[:4:])
# print(string_python[-4:-1])
# print(string_python[-6::])
# print(string_python[-1:-4:-1])
# print(string_python[-1::-1]) # This is important for reversing the string through slicing
# Repeating the strings
# string_repeat = 'core python'
# print(string_repeat*2)
# s = string_repeat[5:7]*3
# print(s)
# Concatenation of strings
# s1 = 'core '
# s2 = 'python'
# string_whole = s1+s2
# print(string_whole)
# Checking the membership
# super_string = input("Enter the main string:\n")
# sub_string = input("Enter the sub string:\n")
# if sub_string in super_string:
#     print(sub_string + ' is found in main string')
# else:
#     print(sub_string + ' is not found in the main string')
# Comparing the strings : python does it in the dictionary order A is less than B
# s1 = 'Box'
# s2 = 'Boy'
# if s1 == s2:
#     print('Both are same')
# else:
#     print("Not same")
# if s1 < s2:
#     print("s1 less than s2")
# else:
#     print("s1 is greater than or equal to s2")
# Removing Spaces from the strings
# if 'Mukesh ' == 'Mukesh':
#     print('Welcome')
# else:
#     print("Name not found")
# name = "    Mukesh    "
# print(name.lstrip())
# print(name.rstrip())
# print(name.strip())
# Finding the sub strings
# string_user = input("Enter the main string:\n")
# sub_string = input("Enter the sub string to find:\n")
# with find()
# n = string_user.find(sub_string, 0, len(string_user))
# if n == -1:
#     print("Sub string not found")
# else:
#     print("Sub string found at position: ", n+1)
# with index()
# try:
#     n = string_user.index(sub_string, 0, len(string_user))
# except ValueError:
#     print("Sub string not found")
# else:
#     print('Sub string found at position: ', n+1)
# displaying the all the position of the strings
# string_user = input("Enter the main string:\n")
# sub_string = input("Enter the sub string:\n")
# i = 0
# flag = False
# n = len(string_user)
# while i < n: This code has to be study
#     pos = string_user.find(sub_string, i, n)
#     if pos != -1:
#         print("Found at the position ", pos+1)
#         i = pos + 1
#         flag = True
#     else:
#         i += 1
# if not flag:
#     print('Sub string not found')
# with different logic
# string_user = input("Enter the main string:\n")
# sub_string = input("Enter the sub string:\n")
# pos = -1
# flag = False
# n = len(string_user)
# while True:
#     pos - string_user.find(sub_string, pos+1, n)
#     if pos == -1:
#         break
#     print("Found at position: ", pos+1)
#     flag = True
#
# if not flag:
#     print('Not found')
# Counting substrings in a string
# string_without_counting = 'New delhi'
# print(string_without_counting.count('delhi'))
# print(string_without_counting.count('e', 0, 3))
# print(string_without_counting.count('e', 0, len(string_without_counting)))
# Immutability of the strings
# string_abcd = 'abcd'
# print(string_abcd[0])
# string_abcd[0] = 'x'
# s1 = "One"
# s2 = "Two"
# print(id(s1))
# print(id(s2))
# s2 = s1
# print("After modification")
# print(id(s1))
# print(id(s2))
# Replacing the string with another string
# string_1 = "That is a beautiful girl"
# s1 = 'girl'
# s2 = 'flower'
# string_1.replace(s1, s2)
# print(string_1)
# string_2 = string_1.replace(s1, s2)
# print(string_2)
# Splitting and joining of strings
# string_user_splitting = input("Enter the numbers separated by spaces:\n")
# lst = string_user_splitting.split(' ')
# for i in lst:
#     print(i)
# join
# string_characters = ('one', 'two', 'three')
# print(':'.join(string_characters))
# Changing the case of the string
# upper method
# string_upper = 'python is the future'
# print(string_upper.upper())
# print(string_upper.lower())
# print(string_upper.swapcase())
# print(string_upper.title())
# checking the starting and ending of a string
# string_checking_ends_starts = 'This is python'
# print(string_checking_ends_starts.startswith('This'))
# print(string_checking_ends_starts.endswith('python'))
# String testing methods
# delhi = 'Delhi99'
# print(delhi.islower())
# print(delhi.isupper())
# print(delhi.isalpha())
# print(delhi.isalnum())
# print(delhi.isspace())
# print(delhi.istitle())
# print(delhi.isdigit())
# Formatting the string
# Id = 10
# name = 'Shankar'
# salary = 19500.75x
# string_formatted = '{one}\n{two}\n{three}'.format(one=Id, two=name, three=salary)
# print(string_formatted)
# num_value = 5000
# num1_value = 1000
# print('{:*>15d}'.format(num_value))
# print('{:*^15d}'.format(num_value))
# print('Hexadecimal= {:.>15x}\nBinary= {:.<15b}'.format(num1_value, num1_value))
# print('Hexadecimal= {:.>#15x}\nBinary= {:.<#15b}'.format(num1_value, num1_value))
# Working with the characters
# string_user_characters = input("Enter the string:\n")
# character = string_user_characters[0]
# if character.isalnum():
#     print("It is alphabet or numeric characters")
#     if character.isalpha():
#         print('It is an alphabet')
#         if character.isupper():
#             print("It is capital letter")
#         else:
#             print("It is lowercase letter")
#     else:
#         print('It is a numeric digit')
# elif character.isspace():
#     print('It is a space')
# else:
#     print("It may be a special characters")
# Sorting the string
# string_dictionary_sorter = []
# n = int(input("How many strings?"))
# for i in range(n):
#     print("Enter the string: ", end='')
#     string_dictionary_sorter.append(input())
# str1 = sorted(string_dictionary_sorter)
# print('Sorted list:')
# for i in str1:
#     print(i)
# Searching in the string
# string_user = []
# n = int(input("How many strings?"))
# for i in range(n):
#     print("Enter the string: ", end='')
#     string_user.append(input())
# s = input("Enter the string to search: ")
# flag = False
# for i in range(len(string_user)):
#     if s == string_user[i]:
#         print("Found at: ", i + 1)
#         flag = True
# if not flag:
#     print("Not found")
# Finding the number and characters and words
# string_to_find_characters = input("Enter a string:\n")
# i = 0
# for s in string_to_find_characters:
#     print(string_to_find_characters[i], end='')
#     i += 1
# print('\nNo. of characters: ', i)
# string_words_count = input("Enter the string:\n")
# i = c = 0
# flag = False
# for s in string_words_count:
#     if not flag and string_words_count[i] == ' ':
#         c += 1
#     if string_words_count[i] == ' ':
#         flag = True
#     else:
#         flag = False
#     i += 1
# print('No. of words: ', c+1)
# Inserting a sub string into a string
# string_user = input("Enter a string:\n")
# sub_string_user = input("Enter a sub string:\n")
# n = int(input("Enter position no:\n"))
# n -= 1
# l1 = len(string_user)
# l2 = len(sub_string_user)
# str1 = []
# for i in range(n):
#     str1.append(string_user[i])
# for i in range(l2):
#     str1.append(sub_string_user[i])
# for i in range(n, l1):
#     str1.append(string_user[i])
# str1 = ''.join(str1)
# print(str1)
