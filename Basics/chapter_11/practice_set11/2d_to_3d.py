class TwoDVector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class ThreeDVector(TwoDVector):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z = z

Vec1 = ThreeDVector(1,2,3)
print(Vec1.x)
print(Vec1.y)
print(Vec1.z)