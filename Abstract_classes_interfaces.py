# Abstract classes working area
# class MyClass:
#     @staticmethod
#     def calculate(x):
#         print(f'Square value of x is {x*x}')
#
#
# obj1 = MyClass()
# obj1.calculate(2)
# obj1 = MyClass()
# obj1.calculate(3)
# obj1 = MyClass()
# obj1.calculate(4)
# with the abstract way
# from abc import ABC, abstractmethod
# import math
#
#
# class MyClass(ABC):
#
#     @abstractmethod
#     def calculate(self, x):
#         pass
#
#
# class Sub1(MyClass):
#     def calculate(self, x):
#         print("Square value= ", x * x)
#
#
# class Sub2(MyClass):
#     def calculate(self, x):
#         print('Square root= ', math.sqrt(x))
#
#
# class Sub3(MyClass):
#     def calculate(self, x):
#         print('Cube root is ', x**3)
#
#
# obj1 = Sub1()
# obj1.calculate(2)
# obj2 = Sub2()
# obj2.calculate(3)
# obj3 = Sub3()
# obj3.calculate(4)
# Car example in abstraction and classes
# from abc import ABC, abstractmethod
#
#
# class Car(ABC):
#     def __init__(self, register_no):
#         self.register_no = register_no
#
#     def openTank(self):
#         print('Fill the fuel into the tank')
#         print('For the car with register number ', self.register_no)
#
#     @abstractmethod
#     def steering(self):
#         pass
#
#     @abstractmethod
#     def braking(self):
#         pass
#
#
# class Maruti(Car):
#     def steering(self):
#         print('Maruti uses manual steering')
#         print('Drive the car')
#
#     def braking(self):
#         print('Maruti uses hydraulic brakes')
#         print("Apply brakes and stop it")
#
#
# class Santo(Car):
#     def steering(self):
#         print('Santo uses power steering')
#         print('Drive the car')
#
#     def braking(self):
#         print('Santo uses gas brakes')
#         print('Apply brakes and stop it')
#
#
# m = Maruti(1001)
# s = Santo(7879)
# m.openTank()
# m.steering()
# m.braking()
# s.openTank()
# s.steering()
# s.braking()
# A python program to make a interface which can connect to the any database
# from abc import ABC, abstractmethod
#
#
# class MyClass(ABC):
#     @abstractmethod
#     def connect(self):
#         pass
#
#     @abstractmethod
#     def disconnect(self):
#         pass
#
#
# class Sybase(MyClass):
#     def connect(self):
#         print('Connecting to the Sybase database')
#
#     def disconnect(self):
#         print('Disconnecting from the Sybase database')
#
#
# class Oracle(MyClass):
#     def connect(self):
#         print('Connecting to the Oracle database')
#
#     def disconnect(self):
#         print('Disconnecting from the Oracle database')
#
#
# class Database:
#     string_user_database_name = input("Enter the database name: ")
#     print(globals())
#     class_name = globals()[string_user_database_name]
#     x = class_name()
#     x.connect()
#     x.disconnect()
# A python program which contains a printer interface and its sub classes to send next to any printer
# from abc import ABC, abstractmethod
#
#
# class Printer(ABC):
#     @abstractmethod
#     def printIt(self, text):
#         pass
#
#     @abstractmethod
#     def disconnect(self):
#         pass
#
#
# class IBM(Printer):
#     def printIt(self, text):
#         print(text)
#
#     def disconnect(self):
#         print("printing completed on IBM Printer")
#
#
# class Epson(Printer):
#     def printIt(self, text):
#         print(text)
#
#     def disconnect(self):
#         print("printing completed on Epson  Printer")
#
#
# class UsePrinter:
#     with open("config.txt") as f:
#         string_file: str = f.readline()
#     object_name_from_file = globals()[string_file]
#     x = object_name_from_file()
#     x.printIt("hello this is sent to printer")
#     x.disconnect()
