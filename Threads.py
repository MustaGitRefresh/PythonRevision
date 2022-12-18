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
class MyThread(threading.Thread):

    def __init__(self, str):
        super().__init__()
        print(str)

    def run(self):
        for i in range(1, 6):
            print(i)


tmy = MyThread("Hello")
tmy.start()
tmy.join()

