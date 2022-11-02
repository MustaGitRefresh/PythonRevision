class Emp:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):
        print('{:5d} {:20s} {:10.2f}'.format(self.id, self.name, self.salary))
