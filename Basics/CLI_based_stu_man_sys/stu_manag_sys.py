student = []

run = True

def finStduByRollNo(froll):
    for i in range(len(student)):
        if(student[i].get("rollno") == froll):
            return i
        
    return 

def showStudent(sroll):
    idx = finStduByRollNo(sroll)
    if idx == None:
        print("invalid roll no")
        return none
    print(f"The name of student is {student[idx].get('name')}")
    print(f"The rollno of student is {student[idx].get('rollno')}")
    print(f"The age of student is {student[idx].get('age')}")

def viewStudent():
    see = int(input("Enter an rollno of student:"))
    idx = finStduByRollNo(see)
    if idx == None:
        print("invalid roll no")
        return 0
    print(f"The name of student is {student[idx].get('name')}")
    print(f"The rollno of student is {student[idx].get('rollno')}")
    print(f"The age of student is {student[idx].get('age')}")

def checkRollno(eroll):
    if eroll < 0:
        raise ValueError("Negative roll no not allowed")
    for i in range(len(student)):
        if eroll == (student[i].get("rollno")):
            raise ValueError("Student already exits with entered roll no ")
    return 0

def checkAge(eage):
    if eage < 6 or eage > 25:
        raise ValueError("Invalid Age for an valid Student")
    return 0    

def addStudent():
    print("DEBUG: addStudent CALLED")
    name = input("Enter a name:")
    try:
        rollno = int(input("Enter a roll number:"))
        checkRollno(rollno)
    except ValueError as e:
        print(e)
        return
    age = int(input("Enter age of student:"))
    checkAge(age)
    stu = {}
    stu.update({"name":name, "rollno":rollno, "age":age})
    if len(student) > 0:
        student.append(stu)
    else:
        student.append(stu)



def delStudent():
    droll = int(input("Enter the roll no of student:"))
    showStudent(droll)
    if showStudent(droll) == None:
        return None
    confirm = input("Are you sure you want to delete that student?\n")
    if confirm == "yes":
        student.pop(finStduByRollNo(droll))
    elif confirm == "no":
        print("Thanks for visiting")

def saveToFile():
    f = open("student.txt", "w")
    for i in range(len(student)):
        s = student[i]
        line = f"{s.get('name')},{s.get('rollno')},{s.get('age')}\n"
        f.write(line)
    f.close()
    print("Successfully saved changes")

def PrintFromFile():
    f = open("student.txt","r")
    text = f.read()
    print(text)
    f.close()

def userChoice():
    print("===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Student")
    print("3. Delete Student")
    print("4. Save to File")
    print("5. Print from File")
    print("6. Exit")
    print("=====================================")
    choice = int(input("Enter your choice: "))
    print("You entered:", choice, type(choice))
    if choice == 1:
        addStudent()
    elif choice == 2:
        viewStudent()
    elif choice == 3:
        delStudent()
    elif choice == 4:
        saveToFile()
    elif choice == 5:
        PrintFromFile()
    elif choice == 6:
        print("Thanks for visiting")
        return False
    else:
        print("Invalid choice")
    return True


while run:
    run = userChoice()
