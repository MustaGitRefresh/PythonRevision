# class Student:
#     """
#     This is a class name student which contains the details of the student:
#     Like name, age, marks obtained of the student
#     :method It has a method name talk for printing out the variables
#     """
#     def __init__(self, name='.', marks=0):
#         # self.name = "Vishnu"
#         # self.age = 20
#         # self.marks = 900
#         # print(f'The self is {self}')
#         self.name = name
#         self.age = 20
#         self.marks = marks
#
#     def talk(self):
#         """
#         This is a method talk which prints the instance variables of the class Student
#         """
#         print('Hi, I am ', self.name)
#         print('My age is ', self.age)
#         print('My marks are ', self.marks)
#
#
# s1 = Student('Lakshmi roy', 880)
# print(id(s1))
# s1.talk()
# Types of variables
# Instance
# class Sample:
#     def __init__(self):
#         self.x = 10
#
#     def modify(self):
#         self.x += 1
#
#
# s1 = Sample()
# s2 = Sample()
# print('x in s1 = ', s1.x)
# print('x in s2 = ', s2.x)
# s1.modify()
# print('x in s1 = ', s1.x)
# print('x in s2 = ', s2.x)
# class variables or static variables
# class Sample:
#     x = 10
#
#     @classmethod
#     def modify(cls):
#         cls.x += 1
#
#
# s1 = Sample()
# s2 = Sample()
# print('x in s1 = ', s1.x)
# print('x in s2 = ', s2.x)
# s1.modify()
# print('x in s1 = ', s1.x)
# print('x in s2 = ', s2.x)
# NameSpaces
# class Student:
#     n = 10
#
#
# print(Student.n)
# Student.n += 1
# print(Student.n)
#
# s1 = Student()
# print(s1.n)
# s2 = Student()
# print(s2.n)
# s1.n += 1
# print(s1.n)
# Types of methods
# Instance methods: normal
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def display(self):
#         """
#         This displays the details of instance objects
#         """
#         print(f"Hi, {self.name}")
#         print(f"Your marks are {self.marks}")
#
#     def calculate(self):
#         """
#         This method calculates the marks and find out the grade
#         """
#         if self.marks >= 600:
#             print("You got first grade")
#         elif self.marks >= 500:
#             print('You got second grade')
#         elif self.marks >= 350:
#             print('You got third grade')
#         else:
#             print("You are failed")
#
#
# n = int(input("How many students? "))
# i = 0
# while i < n:
#     name = input("Enter name: ")
#     marks = int(input("Enter the marks: "))
#     s = Student(name, marks)
#     s.display()
#     s.calculate()
#     i += 1
#     print("_____________________________________________________________")
# Instance methods: setter and getter
# class Student:
#     def __init__(self):
#         self.name = None
#         self.marks = None
#
#     def setName(self, out_name):
#         self.name = out_name
#
#     def set_Marks(self, out_marks):
#         self.marks = out_marks
#
#     def getName(self):
#         return self.name
#
#     def getMark(self):
#         return self.marks
#
#     def calculate(self):
#         """
#         This method calculates the marks and find out the grade
#         """
#         if self.marks >= 600:
#             print("You got first grade")
#         elif self.marks >= 500:
#             print('You got second grade')
#         elif self.marks >= 350:
#             print('You got third grade')
#         else:
#             print("You are failed")
#
#
# n = int(input("How many students? "))
# i = 0
# while i < n:
#     s = Student()
#     name = input("Enter name: ")
#     s.setName(name)
#     marks = int(input("Enter the marks: "))
#     s.set_Marks(marks)
#     print(f'Hi, {s.getName()}')
#     print(f'Your marks are {s.getMark()}')
#     s.calculate()
#     i += 1
#     print("_____________________________________________________________")
# Class methods
# class Bird:
#     wings = 2
#
#     @classmethod
#     def fly(cls, name):
#         print('{} flies with {} wings'.format(name, cls.wings))
#
#
# Bird.fly('Sparrow')
# Bird.fly('Pigeon')
# Static methods
# class MyClass:
#     # This is a class var
#     n = 0
#
#     def __init__(self):
#         MyClass.n = MyClass.n + 1
#
#     @staticmethod
#     def noObject():
#         print('No. of instances create ', MyClass.n)
#
#
# obj1 = MyClass()
# print(id(obj1))
# obj2 = MyClass()
# print(id(obj2))
# obj3 = MyClass()
# print(id(obj3))
# obj4 = MyClass()
# print(id(obj4))
# obj5 = MyClass()
# print(id(obj5))
# obj6 = MyClass()
# print(id(obj6))
# obj7 = MyClass()
# print(id(obj7))
# obj8 = MyClass()
# print(id(obj8))
# obj9 = MyClass()
# print(id(obj9))
# obj10 = MyClass()
# print(id(obj10))
# obj11 = MyClass()
# print(id(obj11))
# MyClass.noObject()
# import math
#
#
# class Sample:
#     @staticmethod
#     def calculate(x):
#         result = math.sqrt(x)
#         return result
#
#
# num = float(input("Enter a number: "))
# res = Sample.calculate(num)
# print('The square root of {} is {:.2f}'.format(num, res))
# creating a simple bank program
# import sys
#
#
# class Bank:
#     """
#     Bank related transactions
#     """
#     def __init__(self, user_name, balance=0.0):
#         self.name = user_name
#         self.balance = float(balance)
#
#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance
#
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print('Balance amount is less, so no withdrawal.')
#         else:
#             self.balance -= amount
#         return self.balance
#
#
# name = input("Enter the name: ")
# b = Bank(name)
# while True:
#     print('d -Deposit, w -Withdraw, e -Exit')
#     choice = input("Your choice: ")
#     if choice == 'e' or choice == "E":
#         sys.exit()
#     amt = float(input("Enter the amount: "))
#
#     if choice == 'd' or choice == "D":
#         print('Balance amount after deposit: ', b.deposit(amt))
#     elif choice == 'w' or choice == "W":
#         print('Balance amount after withdraw: ', b.withdraw(amt))
# Passing Members of One class to Another Class
# class Emp:
#     def __init__(self, id, user_name, salary):
#         self.id = id
#         self.name = user_name
#         self.salary = salary
#
#     def display(self):
#         print('Id = ', self.id)
#         print('Name = ', self.name)
#         print('Salary = ', self.salary)
#
#
# class MyClass:
#     """
#     Retrieving the employee details by using the below static method
#     """
#     @staticmethod
#     def my_method(e):
#         e.salary += 1000
#         e.display()
#
#
# e = Emp(10, 'Raj Kumar', 15000.75)
# MyClass.my_method(e)
# Another program to calculate the power of the given number without using the class or instance variables
# class MyClass:
#     @staticmethod
#     def my_method(x, n):
#         result = x ** n
#         print('{} to the power of {} is {}'.format(x, n, result))
#
#
# MyClass.my_method(5, 3)
# MyClass.my_method(5, 4)
# Inner Classes
# class Person:
#     def __init__(self):
#         self.name = 'Charles'
#         self.db = self.Dob()
#
#     def display(self):
#         print('Name = ', self.name)
#
#     class Dob:
#         def __init__(self):
#             self.dd = 10
#             self.mm = 5
#             self.yy = 1998
#
#         def display(self):
#             print('Dob = {}/{}/{}'.format(self.dd, self.mm, self.yy))
#
#
# p = Person()
# p.display()
# x1 = p.db
# x1.display()
# x = Person().Dob()
# x.display()
# print(x.yy)
# This way you can create a instance variable using the with statement
# class B:
#     def __init__(self):
#         print("Object created")
#
#     def giver(self):
#         print("Give the message")
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self ,type, value, traceback):
#         return False
#
# b = None
#
# with B() as b:
#     b.giver()
