class calculator:
    def __init__(self,num1):
        self.num1=num1

    def square(self):
        print(f"square is {self.num1**2}")
    def cube(self):
        print(f"cube is {self.num1**3}")
    def squareroot(self):
        print(f"the squareroot {self.num1**0.5}")

a=calculator(16)
a.square()
a.cube()
a.squareroot()