# Task 1: Student Class
#  Create a class Student

# attributes: name, age, marks
# method: display_details()


# class Student:
#     def __init__(self,name,age,marks):
#         self.name = name
#         self.age = age 
#         self.marks = marks 

#     def display(self):
#         print(self.name)
#         print(self.age)
#         print(self.marks)

# x = Student("ajay",21,67)
# x.display()

# ====================================================================================================================================================================

# Task 2: Car Class
#  Create a class Car
# attributes: brand, speed
# methods:

# start()
# accelerate()

# stop()

# class car:
#     def __init__(self,brand,speed):
#         self.brand = brand
#         self.speed = speed

#     def start(self):
#         print(" Your car name is " + self.brand , "now start your car")

#     def accelerate(self):
#         print(" Put your leg on accelerator and drive the car with speed " , self.speed )
    
#     def stop(self):
#         print(" stop the car ")

#     def display(self):
#         print(self.brand)
#         print(self.speed)

# value = car("BMW M5 COMPETETION", 100)
# value.start()
# value.accelerate()
# value.stop()


# ==================================================================================================================================================================


# Task 3: Rectangle Class
#  Create a class Rectangle
# attributes: length, width
# methods:

# area()

# perimeter()

# class rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
     
#     def area(self):
#         print(self.length)

#     def perimeter(self):
#         print(self.width)
         
#     def display(self):
#         print(self.length)
#         print(self.width)

# x = rectangle(4 , 7)
# x.area()
# x.perimeter()

# =====================================================================================================================================================================

# Task 4: Calculator Class
#  Create a class Calculator
# methods:

# add(a, b)
# subtract(a, b)
# multiply(a, b)

# divide(a, b)

# class calculator:
    
#     def add(self, a,b):
#         return a+b

#     def subtract(self, a , b):
#         return a-b
    
#     def multiply(self, a , b):
#       return a * b

#     def divide(self,a,b):
#         return a/b
# calc = calculator()
    
# print(calc.add(10, 5))
# print(calc.subtract(10, 5))
# print(calc.multiply(10, 5))
# print(calc.divide(10, 5))


# =====================================================================================================================================================================

#Task 5: BankAccount Class
#  Create a class BankAccount
# attributes: name, balance
# methods:

# deposit(amount)
# withdraw(amount)

# check_balance()
# Condition:

# Do not allow withdrawal if balance is low


# :fire: Bonus (if time left)
# • Print messages after each transaction


# class Bankaccount:

    
    
#     def __init__(self,name,balance):
#         self.name = name 
#         self.balance = balance 
     

#     def deposit(self, amount):     
#         print("deposit amount is" ,amount)
#         self.balance = self.balance + amount
#         self.mybalance()

#     def withdraw(self,value):
#         if value > self.balance:
#             print("insufficiant balance withdraw is cancled")
#         else:
#             print("withdraw amount", value)
#             self.balance = self.balance - value
#         self.mybalance()

#     def mybalance(self):
#         print("your account balance is ", self.balance)

# x = Bankaccount("Shaurya", 20000)

# print(x.name)
# print(x.balance)
# x.deposit(3000)
# x.withdraw(4000)


# class student:
#     def __init__(self,name,age,section,marks):
#         self.name = name
#         self.age = age 
#         self.section = section
#         self.marks = marks 

#     def display(self):
#         print(self.name)
#         print(self.age)
#         print(self.section)
#         print(self.marks)

#     def ispass(self):
#         if self.marks >= 40:
#             print("Pass")

#         else:
#             print("fail")   

# x = student("shaurya",18,"B",45)
# y = student("naman",45,"a",30)
# x.display()
# x.ispass()
# y.display()
# y.ispass()



# class student:
#     def __init__(self,marks):
#         self.marks = marks
         
#     def mark(self,marks):
#         if marks > self.marks:
#             print("pass")
        
#         else:
#             print("fail")

#     def display(self):
#         print(self.marks)

# x = student(46)
# x.display()

# ================================================================================================================================================================

# Task : Shopping Cart 
# Create class ShoppingCart:

# attribute: items (list)
# Methods:

# add_item(item_name)
# remove_item(item_name)
# show_items()

class ShoppingCart:
    def __init__(self):
        self.items = []   

    def add_item(self, item_name):
        self.items.append(item_name)
        print(item_name + " added ")

    def remove_item(self, item_name):
            self.items.remove(item_name)
            print(item_name + " removed")

    def show_items(self):
        if len(self.items) == 0:
            print("Nothing is there in list")
        else:
            print("Items in cart:")
            for item in self.items:
                print(item)

cart = ShoppingCart()
cart.add_item("Apple")
cart.show_items()
cart.remove_item("Apple")
cart.show_items()
