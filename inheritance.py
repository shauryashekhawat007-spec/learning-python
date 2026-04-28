# Task 1: Animal System
# Create class Animal:

# method: speak() → print “Animal sound”
# Create child classes:

# Dog → override speak() → “Dog barks”
# Cat → override speak() → “Cat 

class animal:
    def speak(self):
        print("ANIMAL SOUND")
    
class dog(animal):
    # def speak(self):
    #     print("dog barks")
    pass

class cat(animal):
    def speak(self):
        print("")

x = dog()
y = cat()
x.speak()
y.speak()




# # Task 3: Employee Hierarchy
# Task 3: Employee Hierarchy
# Create class Employee:

# attributes: name, salary
# Create child classes:

# Manager → bonus = 20%
# Developer → bonus = 10%
# Add method: calculate_bonus()

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary    
    def display(self):
        print("EMPLOYEE NAME IS" , self.name)
        print("SALARY" , self.salary)

class manager(Employee):
    def calculate_bonus(self):
        bonus = self.salary * 0.20
        print("Bonus amount is" ,bonus)
       
class developer(Employee):
    def calculate_bonus(self):
        bonus = self.salary * 0.10
        print("bonus ammount is", bonus)
       
        

x = manager("ANKIT",20000)
y = developer("manish",30000)
x.display()
x.calculate_bonus()
y.display()
y.calculate_bonus()





# Task 4: Shape System
# Create class Shape:

# method: area()
# Child classes:

# Rectangle
# Circle
# Override area()

class Shape:
    def area(self):
        print("shape")

class Rectangle(Shape):
    def area(self):
         print("area of rectangle is ")

class Circle(Shape):
    def area(self):
        print("area of circlr is" )

x = Rectangle()
y = Circle()
x.area()
y.area()


   



#    Task 2: Vehicle System
# Create class Vehicle:

# method: start()
# Create child classes:

# Car
# Bike
# Override start() with different messages

class Vehicle:
    def start(self):
        print("START")

class Car:
    def start(self):
        print("START YOUR CAR NOW")

class Bike:
    def start(self):
        print("START YOUR BIKE NOW")

x = Car()
y = Bike()
x.start()
y.start()        


# =================================================================================================================================================



# Task 5: Bank Account Types
# Create base class BankAccount:

# attributes: name, balance
# method: withdraw()
# Create:

# SavingsAccount → limit withdrawal (e.g. max 10k)
# CurrentAccount → no limit

class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
         
    def withdraw(self):
        print("WITHDRAW")

    def display(self):
        print("ACCOUNT HOLDER NAME IS : ",self.name )
        print("YOUR ACCOUNT BALANCE IS : ", self.balance)
class SavingsAccount:
    def withdraw(self):
        print("YOUR SAVINGS ACCOUNT WITHDRAW LIMIT IS 10K")

class CurrentAccount:
    def withdraw(self):
        print("THERE IS NO LIMIT IN CURRENT ACCOUNT PLEASE ENTER YOUR WITHDRAW AMOUNT")


x = BankAccount("TILAK VERMA",300000)
y = BankAccount("ANSH",400000)
x.display()   
x = SavingsAccount()

y.display()  
y = CurrentAccount()
x.withdraw()
y.withdraw()

