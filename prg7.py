class calculator:
    def __init__(self, value):
        self.value=value 

    def square(self):
        square=self.value*self.value
        return square
    
    def cube(self):
        cube=self.value*self.value*self.value
        return cube
    
a=calculator(9)
print(a.square())
print(a.cube())