# Threading Program 1
import threading

#
# print("Let us find the current thread")
# print('Current Thread: ', threading.current_thread().name)
#
# if threading.current_thread() == threading.main_thread():
#     print("the current is main")
# else:
#     print("Another")

# Program 2, 3
# def display(string):
#     print("Hello world I am running", string)
#
#
# for i in range(5):
#     t = threading.Thread(target=display, args=('rahul',))
#     t.start()

# Program 4 creating through subclass
# class MyThread(threading.Thread):
#
#     def __init__(self, str):
#         super().__init__()
#         print(str)
#
#     def run(self):
#         for i in range(1, 6):
#             print(i)
#
#
# tmy = MyThread("Hello")
# tmy.start()
# tmy.join()

# Program 6 creating thread without subclass
# class MyThread:
#     def __init__(self, str):
#         self.str = str
#
#     def display(self, x, y):
#         print(self.str)
#         print('Args ', x, y)
#
#
# obj = MyThread('hello')
# t1 = threading.Thread(target=obj.display, args=(1, 2))
# t1.start()
# Program 7 single tasking with thread
import time


class MyThread:
    def prepareTea(self):
        self.task1()
        self.task2()
        self.task3()

    def task1(self):
        print('Boil milk and tea powder for 5 minutes....', end='')
        time.sleep(5)
        print('Done')

    def task2(self):
        print('Add sugar and boil for 5 minutes....', end='')
        time.sleep(3)
        print('Done')

    def task3(self):
        print('Filter it and serve....', end='')
        print('Done')


obj = MyThread()
t = threading.Thread(target=obj.prepareTea)
t.start()