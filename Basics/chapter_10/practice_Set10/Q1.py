class Microsoft:
    company_name = "Microsoft Corporation"

    def __init__(self, employee_name, salary, pin):
        self.employee_name = employee_name
        self.salary = salary
        self.pin = pin

p = Microsoft("John Doe", 75000, 1234)
print("Company Name:", p.company_name)
print("Employee Name:", p.employee_name)
print("Salary:", p.salary)