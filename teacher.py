class Teacher:

    def __init__(self):
        self.salary = None
        self.id = None
        self.name = None
        self.address = None

    def set_id(self, t_id):
        self.id = t_id

    def get_id(self):
        return self.id

    def set_name(self, para_name):
        self.name = para_name

    def get_name(self):
        return self.name

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

    def set_salary(self, salary):
        self.salary = salary

    def get_salary(self):
        return self.salary