# 16. Find second largest number


# def findSecondLargest(numbers):
# x = [80,10,8,50]
# first = 0 
# second = 0
# for i in (x):
#     if i > first:
#         second = first 
#         first = i 
#     elif i > second:
#         i != second 
#         second = i 
# print(second)





# # 1. Get input, 2. split by space, 3. convert to int, 4. make a list
# user_input = input("Enter numbers separated by space: ")
# numbers_list = [int(x) for x in user_input.split()]
# print(numbers_list)
# # Pass the list directly (don't wrap it in brackets [])
# findSecondLargest(numbers_list)

# numbers = list(int,input("enter your number"))
# findSecondLargest([numbers])

# # question 2
# num1 = [1,2,3,4,5,6]
# num2 = [2,3,4,5,6,6]


# def sum(num1 , num2):
#     a = num1 + num2
#     return a

# result = sum(num1 ,num2)
# print(result)






# # 18. Find common elements in two lists
# list1 = [12, 34, 35, 56, 67]
# list2 = [12, 22, 33, 67, 34]
# common = []
# def comman(list1,list2):
#     for i in list1:
#         if i in list2:
#            common.append(i)
# result = comman(list1,list2)
# print(common)



# # 19. Sort a list without using sort()
# x = [11,23,45,6,8,0]
# x=["green", "red", "blue","green"]
# n = len(x) 
# for i in range(n-1):  
#     for j in range(n-i-1):
#         if x[j] > x[j+1]:
#             temp =x[j]
#             x[j]=x[j+1]
#             x[j+1]=temp

#         j+=1
#     i+=1
# print (x)




# #  resolve question



# def withoutsort(x):
#     n = len(x) 
#     for i in range(n-1): 
#         for j in range(n-i-1):
#             if x[j] > x[j+1]:
#                 temp =x[j]
#                 x[j]=x[j+1]
#                 x[j+1]= temp

#             j+=1
#         i+=1
#     return(x)
# x = list(map(int, input("enter your number: ").replace(',',' ').split()))
# result = withoutsort(x)
# print(result)






# # 20. Move all zeros to end
# def move_zeros(arr):
#     j = 0  

#     for i in range(len(arr)):
#         if arr[i] != 0:
#             arr[j], arr[i] = arr[i], arr[j]
#             j += 1

#     return arr

# print(move_zeros([0, 1, 0, 3, 12]))




# #   Pattern Questions
# *
# **
# ***
# ****
def pattern(rows):
    for i in range(1,rows + 1):
        for j in range(i):
            print("*",end = "")
        print()

rows = int(input("Enter rows: "))
pattern(rows)


# # pattern question
# # ****
# # ***
# # **
# # *
def pattern(rows):
    for i in range(rows,0, -1):
        print(i * "*")
rows = int(input("Enter rows: "))
pattern(rows)

   


# # Question pattern
# #    *
# #   ***
# #  *****
# # ******* 
# def pattern(rows):
#     for i in range(1, rows + 1):
#         for j in range(rows - i):
#             print(" ", end="")
#         for k in range(2 * i - 1):
#             print("*", end="") 
#         print()
# rows = int(input("Enter rows: "))
# pattern(rows)



# # 24. Count frequency of each character



# def character(each):
#     freq = {}
#     for char in text:
#         if char in freq:
#             freq[char] += 
#         else:
#             freq[char] = 1
#         print(freq,end="\r")
# text = input("enter your character : ")
# character(text)


# # 25. Count words in a sentence
# def countwords(sentence):
#     words = sentence.split()
#     wordcount = len(words)

#     print(f"The sentence has {wordcount} words.")
# sentence = input("enter your text : ")
# countwords(sentence)


# # 26. Find first non-repeating character
# def firstnon
