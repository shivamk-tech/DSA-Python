class Employee:
    def __init__(self, salary, increment):
        self.salary = salary
        self.increment = increment
        print("The salary is:", self.salary)
    
    @property
    def SalaryAfterIncre(self):
        return self.salary + ((self.salary)*(self.increment))/100

    @SalaryAfterIncre.setter
    def SalaryAfterIncre(self, value):
        self.increment = ((value/self.salary) -1) * 100
        print("The increment is set to:", self.increment)
    
    

shivam = Employee(120000,10)
print("the salary agter increment is : ", shivam.SalaryAfterIncre)
shivam.SalaryAfterIncre = 150000