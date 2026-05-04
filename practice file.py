# 16. Find second largest number
# def second_lar(num):
#     first = 0 
#     second = 0
#     for i in (num):
#         if i > first:
#             second = first 
#             first = i 
          
#         elif i > second:
#              i != second 
#              second = i 

#     return second 
        
# print(second_lar([10,20,30]))









# 17. Merge two lists
# list1 = ["a","b","c","d"]
# list2 = [1 , 3 , 5, 6]
 
# for x in list2:
#     list1.append(x)
# print(list1)

# # 18. Find common elements in two lists
# list1 = ['apple','banana','cherry']
# list2 = ['apple','mango','orange','cherry']
# for i in (list1):
#     if i in list2:
#         print(i)


# 19. Sort a list without using sort()
# x = [1,2,4,53,52]
# n = len(x)
# for i in range(n-1):

#     for j in range(n-i-1):
                                                                                                    # I will solve this question with the hepl of google  
#         if x[j] > x[j+1]:
#             num = x[j]
#             x[j] = x[j+1]
#             x[j+1] =  num

# print(x)


         


# 20. Move all zeros to end
arr = [0,0,0,23,45,6,7,0]
j = 0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[i] , arr[j] = arr[j] , arr[i]
        j += 1
        i += 1
print(arr)
