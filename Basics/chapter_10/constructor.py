class Employee:
    def __init__(self, name, salary, langauage): #dunder method which is automatically run during an program without calling and can take parameters other that self 
        self.name = name
        self.salary = salary
        self.langauage = langauage
        print("running the constructor") 


    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Hello, welcome to the company!")


shivam = Employee("shivam", 120000, "Python") #here __init__ method is called automatically
print(shivam.name,shivam.salary,shivam.langauage) #Output: shivam 120000 Python