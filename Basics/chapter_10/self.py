class Employee:
    language = "python"
    salary = 120000
    
    def getInfo(self):
        print(f"langauage is {self.language} and salary is {self.salary}")
    
    @staticmethod
    def greet():#here it is static method because it does not take any self parameter or requires object so we have some method to not get error 
        print("Hello, welcome to the company!")

shivam = Employee()
shivam.getInfo()  # Output: langauage is python and salary is 120000
 