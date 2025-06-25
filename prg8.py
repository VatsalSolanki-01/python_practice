class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
        print("parent constructor called")

class Programmer(Employee):
    def __init__(self, name, salary, tech):
        super().__init__(name, salary)
        self.tech=tech
        print("child constructor called")

    def show(self):
        print(f"name :- {self.name}, salary :- {self.salary}, tech :- {self.tech}")

name=input("enter name :- ")
salary=int(input("enter monthly salary :- "))
tech=input("enter technology name :- ")
emp1=Programmer(name,salary,tech)
emp1.show()

