class Programmer:
    def __init__(self, name, empid, salary):
        self.name=name
        self.empid=empid
        self.salary=salary
    
    def getInfo(self):
        print(f"name = {self.name}")
        print(f"empid = {self.empid}")
        print(f"salary = {self.salary}")
    

prog1=Programmer("Vatsal",19,90000)
prog2=Programmer("Milind",20,9000000)
prog3=Programmer("Soniya",19,90000)

prog1.getInfo()
prog2.getInfo()
prog3.getInfo()