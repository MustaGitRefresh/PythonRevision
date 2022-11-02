class Queue:
    def __init__(self):
        self.q = []

    def isEmpty(self):
        return self.q == []

    def add(self, element):
        self.q.append(element)

    def delete(self):
        if self.isEmpty():
            return -1
        else:
            return self.q.pop(0)

    def search(self, element):
        if self.isEmpty():
            return -1
        else:
            try:
                n = self.q.index(element)
                return n+1
            except ValueError:
                return -2

    def display(self):
        return self.q
