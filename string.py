# 1question
# x = "hello world"[::-1]
# print(x)


# 345678
# x = input("write your name :")
# vowel = ["a","e","i","o","u"]
# consto=["b","c","d"]
# x=x.lower()
# count_vowel=0
# count_consto=0
# for i in x:
#     if i in vowel:
#         count_vowel+=1
#     elif i in consto:
#         count_consto+=1 
# print(count_vowel,count_consto)



# 3question
# x = "hello world"
# for i in x:
#     print(i)


#4 Find length without using len()
# x = "match"
# count = 0
# for i in x:
#   count += 1

# print(count)

#5 check string is palindrome
def is_palindrome(s):
  return str(s) == str(s)[::-1]
print(is_palindrome("madam")) 
print(is_palindrome(121))     
print(is_palindrome("hello"))

#6. Remove spaces from string
# x = "helloworld   ".strip()
print(x,end= "  ")
