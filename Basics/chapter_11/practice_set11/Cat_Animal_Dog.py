class animals:
    pass

class Pet(animals):
    pass

class Dog(Pet):
    @staticmethod
    def bark():
        print("bow bow..!")


groot = Dog.bark()