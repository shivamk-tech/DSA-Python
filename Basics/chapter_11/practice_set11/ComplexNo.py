class ComplexNo:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def display(self):
        print(f"{self.real} + {self.imag}i")
    
    def __add__(self, other):
        return ComplexNo(self.real + other.real, self.imag + other.imag)
    
    def __mul__(self, other):
        return ComplexNo(self.real * other.real - self.imag * other.imag,
                         self.real * other.imag + self.imag * other.real )
c1 = ComplexNo(2, 3)
c2 = ComplexNo(4, 5)

c3 = c1 + c2
c4 = c1 * c2

print(c3.real,c3.imag)
print(c4.real,c4.imag)

    