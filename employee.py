from models.person import Person


class Employee(Person):
    def __init__(self, name, age, company, salary):
        super().__init__(name, age)  # Call the superclass constructor to set name and age
        self.company = company
        self.salary = salary

    def display(self):
        super().display()  # Call the superclass display method to print name and age
        print(f"Company: {self.company}, Salary: {self.salary}")
