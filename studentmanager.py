from student import Student

class Studentmanager:
    def __init__(self):
        self.students = []

    def add_function(self,name,age,marks):
        students = Student(name,age,marks)
        self.students.append(students)
        print("student added sucessfully")



    def view_all_students(self):
        print(self.students)
        for student in self.students:
            student.display_details()

        


    def passed__student(self):
        for student in self.students:
            if student.is_passed():
                student.display_details()

    
#     4. Find Topper
# - Student with highest marks
    def find_topper(self):
        topperstudent = self.students[0]
        for student in self.students:
            if student.marks > topperstudent.marks:
                topperstudent = student
        print(topperstudent.display_details())


    def delete_student(self):   
        deletestudent = input("enter student name you want to delete:  ")
        for student in self.students:
            if student.name == deletestudent:
                self.students.remove(student)
                student.display_details()
                return

            else:
                print("check student name")

    def count_students(self):
        countstudents = len(self.students)
        print("Total students: ", countstudents)

    def delete_all_students(self):
        self.students.clear()

manager = Studentmanager
print(manager.students)   
        self.students.clear()

