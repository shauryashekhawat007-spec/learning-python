from studentmanager import Studentmanager
while True:
    print("\n1 add student")
    print("2 view all students")
    print("3 show passed students")
    print("4 show topper")
    print("5 exit")
    result = input("choice your number")
    obj = Studentmanager() 
    if result == "1":
        