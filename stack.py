# Program 2 creating stack class and making some methods for performing some operations
class Stack:
    def __init__(self):
        self.st = []

    def isEmpty(self):
        return self.st == []

    def push(self, element):
        self.st.append(element)

    def pop(self):
        if self.isEmpty():
            return -1
        else:
            return self.st.pop()

    def peep(self):
        n = len(self.st)
        return self.st[n-1]

    def search(self, element):
        if self.isEmpty():
            return -1
        else:
            try:
                n = self.st.index(element)
                # return len(self.st) - n
                return n+1
            except ValueError:
                return -2

    def display(self):
        return self.st
