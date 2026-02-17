class Employee: #this is noun
    language = "python" #these are class attributes
    salary = 120000

shivam = Employee()
print(shivam.language)  # Output: python #these are object adttributes
print(shivam.salary)    # Output: 120000 #these are object adttributes

babu_bhai = Employee()
babu_bhai.lamguage = "java" #this is instance attribute,which take preference over the class attributes