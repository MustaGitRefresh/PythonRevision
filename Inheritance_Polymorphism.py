# This file will have the inheritance in python
# from teacher import Teacher
#
#
#
#
# t = Teacher()
# t.set_id(10)
# t.set_name('Prakash')
# t.set_address('HNO-10, Mahjouri gardens, Delhi')
# t.set_salary(25000.25)
#
# print("Id = ", t.get_id())
# print("Name = ", t.get_name())
# print("Address = ", t.get_address())
# print("Salary = ", t.get_salary())
# class Student(Teacher):
#     def __init__(self):
#         super().__init__()
#         self.marks = None
#
#     def set_marks(self, marks):
#         self.marks = marks
#
#     def get_marks(self):
#         return self.marks
#
#
# s = Student()
# s.set_id(100)
# s.set_name('Rakesh')
# s.set_address('HNO-22, Ameer pet, Hyderabad')
# s.set_marks(970)
#
# print("Id = ", s.get_id())
# print("Name = ", s.get_name())
# print("Address = ", s.get_address())
# print('Marks = ', s.get_marks())
# Constructor in Inheritance and overriding the super class constructor
# class Father:
#     def __init__(self):
#         self.property = 800000.00
#
#     def display_property(self):
#         print('Father\'s property: ', self.property)
#
#
# class Son(Father):
#     # pass
#     def __init__(self):
#         self.property = 200000.00
#
#     def display_property(self):
#         print('Child\'s property: ',self.property)
#
#
# s = Son()
# s.display_property()
# super method and keyword and parameter passing to hte super class constructor
# class Father:
#     def __init__(self, get_property=0.0):
#         self.property = get_property
#
#     def display_property(self):
#         print('Father\'s property: ', self.property)
#
#
# class Son(Father):
#     def __init__(self, property1=0.0, total_property=0.0):
#         super(Son, self).__init__(total_property)
#         self.property1 = property1
#
#     def display_property(self):
#         print('Total property of child: ', self.property1 + self.property)
#
#
# s = Son(200000.00, 800000.00)
# s.display_property()
# Inheritance with the shapes
# class Square:
#     def __init__(self, x):
#         self.x = x
#
#     def area(self):
#         print('Area of square: ', self.x*self.x)
#
#
# class Rectangle(Square):
#     def __init__(self, x, y):
#         super().__init__(x)
#         self.y = y
#
#     def area(self):
#         super(Rectangle, self).area()
#         print('Area of rectangle: ', self.x*self.y)
#
#
# a, b = [float(x) for x in input("Enter two measurements: ").split()]
# r = Rectangle(a, b)
# r.area()
# Types of inheritance
# Single inheritance
# class Bank:
#     cash = 100000000
#
#     @classmethod
#     def available_cash(cls):
#         print(cls.cash)
#
#
# class AndhraBank(Bank):
#     pass
#
#
# class StateBank(Bank):
#     cash = 20000000
#
#     @classmethod
#     def available_cash(cls):
#         print(cls.cash + Bank.cash)
#
#
# a = AndhraBank()
# a.available_cash()
# s = StateBank()
# s.available_cash()
# Multiple inheritance
# class Father:
#     @staticmethod
#     def height():
#         print('Height is 6.0 foot')
#
#
# class Mother:
#     @staticmethod
#     def color():
#         print('Color is brown')
#
#
# class Child(Father, Mother):
#     pass
#
#
# c = Child()
# print('Child\'s inherited qualities: ')
# c.height()
# c.color()
# Problems in multiple inheritance
# And solving the methods resolution order
# class A(object):
#     def __init__(self):
#         self.a = 'a'
#         print(self.a)
#         super(A, self).__init__()
#
#
# class B(object):
#     def __init__(self):
#         self.b = 'b'
#         print(self.b)
#         super(B, self).__init__()
#
#
# class C(A, B):
#     def __init__(self):
#         self.c = 'c'
#         print(self.c)
#         super(C, self).__init__()
#
#
# o = C()
# print(C.mro())
# Another example of method resolution order
# class A(object):
#     def method(self):
#         print("A class method")
#         super().method()
#
#
# class B(object):
#     def method(self):
#         print("B class method")
#         super().method()
#
#
# class C(object):
#     def method(self):
#         print("C class method")
#
#
# class X(A, B):
#     def method(self):
#         print('X class method')
#         super().method()
#
#
# class Y(B, C):
#     def method(self):
#         print('Y class method')
#         super().method()
#
#
# class P(X, Y, C):
#     def method(self):
#         print('P class method')
#         super().method()
#
#
# p = P()
# p.method()
# print("______________________________________mro of python this____________________")
# for i in P.mro():
#     print(i)
# POLYMORPHISM
# Duck type philosophy
# class Duck:
#     def talk(self):
#         print("Quack, quack!")
#
#
# class Human:
#     def talk(self):
#         print("Hello, hi!")
#
#
# def obj_talk(obj):
#     obj.talk()
#
#
# x = Duck()
# obj_talk(x)
# y = Human()
# obj_talk(y)
# Another example with dog
# class Duck:
#     def talk(self):
#         print("Quack, quack!")
#
#
# class Human:
#     def talk(self):
#         print("Hello, hi!")
#
#
# class Dog:
#     # Error because of the bark method not the talk method name changes
#     def bark(self):
#         print("Bow, bow!")
#
# def obj_talk(obj):
#     if hasattr(obj, 'talk'):
#         obj.talk()
#     elif hasattr(obj, 'bark'):
#         obj.bark()
#     else:
#         print("Wrong object passed....")
#
#
# x = Duck()
# obj_talk(x)
# x = Human()
# obj_talk(x)
# x = Dog()
# obj_talk(x)
# Operator Overloading
# class BookX:
#     def __init__(self, pages):
#         self.pages = pages
#
#     def __add__(self, other):
#         return self.pages + other.pages
#
# class BookY:
#     def __init__(self, pages):
#         self.pages = pages
#
#
# b1 = BookX(100)
# b2 = BookY(150)
# print(b1+b2)
# Another example with the greater than operator
# class Ramayana:
#     def __init__(self, pages):
#         self.pages = pages
#
#     def __gt__(self, other):
#         return self.pages > other.pages
#
# class Mahabharata:
#     def __init__(self, pages):
#         self.pages = pages
#
#
# b1 = Ramayana(1000)
# b2 = Mahabharata(1500)
# if b1 > b2:  # This throws error
#     print('Ramayana has more pages')
# else:
#     print('Mahabharata has more pages')
# Another example with the multiple operator
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def __mul__(self, other):
#         return self.salary * other.days
#
#
# class Attendance:
#     def __init__(self, name, days):
#         self.name = name
#         self.days = days
#
#
# x1 = Employee('ring', 500.00)
# x2 = Attendance('ring', 25)
# print('This month salary ', x1*x2)
# Method overloading
# class MyClass:
#     @staticmethod
#     def sum(a=None, b=None, c=None):
#         if a is not None and b is not None and c is not None:
#             print('Sum of three: ', a+b+c)
#         elif a is not None and b is not None:
#             print('Sum of two: ', a+b)
#         else:
#             print('Please the fill the minimum two parameters')
#
#
# m = MyClass()
# m.sum(10, 15, 20)
# m.sum(10.5, 25.55)
# m.sum(100)
# Method overriding
# import math
#
#
# class Square:
#     @staticmethod
#     def area(x):
#         print('Square area %.4f' % x*x)
#
#
# class Circle(Square):
#     @staticmethod
#     def area(x):
#         print('Circle area %.4f' % (math.pi*x*x))
#
#
# c = Circle()
# c.area(15)
