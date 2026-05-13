from studentmanager import Studentmanager
obj = Studentmanager() 
while True:
    print("\n1 add student")
    print("2 view all students")
    print("3 show passed students")
    print("4 show topper")
    print("5 delete student")
    print("6 count_student")
    print("7 exit")
    result = input("choice your number: ")
    
    if result == "1":
        name = input("enter student name: ")
        age = int(input("enter student age: "))
        marks = float(input("enter student marks: "))
        obj.add_function(name,age,marks)
        
    elif result == "2":
        obj.view_all_students()
        print("all student list")


    elif result == "3":
        obj.passed__student()


    elif result == "4":
        obj.find_topper()
        print("state topper")

    elif result == "5":
        obj.delete_student()
        print("student record deteted sucessfully")

    elif result == "6":
        obj.count_students()
        

    elif result == "7":
        print("exit your app")
        break

    else:
        print("Enter correct number")