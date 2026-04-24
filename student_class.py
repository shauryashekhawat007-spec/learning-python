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

# ===================================================================

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

# =========================================================================


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

# class ShoppingCart:
#     def __init__(self):
#         self.items = []   

#     def add_item(self, item_name):
#         self.items.append(item_name)
#         print(item_name + " added ")

#     def remove_item(self, item_name):
#             self.items.remove(item_name)
#             print(item_name + " removed")

#     def show_items(self):
#         if len(self.items) == 0:
#             print("Nothing is there in list")
#         else:
#             print("Items in cart:")
#             for item in self.items:
#                 print(item)

# cart = ShoppingCart()
# cart.add_item("Apple")
# cart.show_items()
# cart.remove_item("Apple")
# cart.show_items()



# Task : Employee Bonus
# Create class Employee:

# attributes: name, salary
# Methods:

# calculate_bonus() → 10% of salary
# display_details()


# -------------------------------

# class Employee:
#     def __init__(self,name,salary):
#         self.name = name 
#         self.salary = salary 


#     def details(self):
#         print(self.name)
#         print(self.salary)


#     def calculate_bonus(self):
#         bonus = self.salary * 0.10
#         print("Bonus amount is" ,bonus)
#         print(self.calculate_bonus
#               )
        
  
# e1 = Employee("harsh",66000)

# e1.details()
# e1.calculate_bonus()

# ====================================================================================================================================================================       

# Task : Password Checker
# Create class PasswordChecker:

# method: is_valid(password)
# Conditions:

# length >= 8
# must contain at least 1 digit

class passwordchecker:
    def is_valid(self,password):
        if len(password) < 1:
            return

        elif len(password)>= 8: 
            print("INVALID make your password strong")

        else:
            print("Your password is correct")
            print(self.is_valid)
x = passwordchecker()
x.is_valid("wt6")



# Task : Movie Ticket System
# Create class MovieTicket:

# attributes: movie_name, available_seats
# Methods:

# book_ticket(count)
# cancel_ticket(count)
# show_available_seats()
# Conditions:

# cannot book more than available
# cannot cancel more than booked

# class Movieticket:
#     def __init__(self,movie_name,available_seats):
#         self.movie_name = movie_name
#         self.available_seats = available_seats
#     def display(self):
#             print("MOVIE NAME :"  ,self.movie_name)
#             print("AVAILABLE SEATS FOR THIS SHOW IS ",self.available_seats)

#     def bookticket(self,count):
#         if count > (self.available_seats):
#             print("HOUSEFULL")
        
#         else:
#             print("BOOK YOUR TICKET NOW")

#     def cancle_ticket(self,count):
#         if count > (self.available_seats):
#             print("SORRY YOU CANNOT CANCLE MORE THAN BOOKED")

#         else:
#             print("YOUR TICKET IS CANCLED SUCESSFULLY")

 
# P = Movieticket("ATONMENT",124)
# P.display()
# P.bookticket(23)
# P.cancle_ticket(125)




