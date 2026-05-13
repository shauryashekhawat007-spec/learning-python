class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display_details(self):
        print("student name :",self.name)
        print("Age: ",self.age)
        print("marks",self.marks)


    def is_passed(self):
        return self.marks>=40
          