# my_string = "Hello World!"
# index = 0
# while index < len(my_string):
#     print(my_string[index])
#     index += 1

# def checkOccurence(str,ch,choice):
#     if choice==1:
#         if ch in str:
#             return str.index(ch)
#         else:
#             return -1
#     elif choice==2:
#         index = 0
#         for i in range(len(str)):
#             if str[i] == ch:
#                 index = i
#                 return index
        
#         return -1
    

# str = input("Enter string: ")
# choice = int(input("1)String\n2)Char\nEnter choice: "))

# if choice==1:
#     char = input("Enter substring to find for: ")
#     index = checkOccurence(str,char,choice)
#     if index==-1:
#         print(f"'{char}' not found in string '{str}'")
#     else:
#         print(f"'{char}' found from position {index} in '{str}'")
# elif choice==2:
#     count = 0
#     char = input("Enter character to find for: ")
#     index = checkOccurence(str,char,choice)
#     for i in range(len(str)):
#         if str[i]==char:
#             count+=1
#     if index==-1:
#         print(f"'{char}' not found in string '{str}'")
#     else:
#         print(f"'{char}' found at position {index} in '{str}', total of {count} times in string")

# def fun(string,char):
#     print(string)
#     for i in range(len(string)):
#         if char == string[i]:
#             print(i)
#     print("count is ",string.count(char))
# a = input("Enter the string ")
# b = input("Enter a char ")
# fun(a,b)

# s1='itm skills university'
# s2='sahil'


# Python program to count vowels both upper and lower case.
# WAP that takes in a sentence and counts the words in it.
# WAP to check if two stringa are anagrams of each other.
# WAP to convert camel case to snake case.
# Write a python program that takes a list of strings and sorts them based on their length.

# 1
# a=['a','e','i','o','u']
# str1=input('Enter String: ')
# count=0
# print(len(str1))
# for i in str1:
#     if i.lower() in a:
#         count=count+1
# print(count)

# 2
# def count(sentence):
#     words=sentence.split()
#     return len(words)
# user=input("Enter a sentence:")
# result=count(user)
# print("The number of words in the sentence is:",result)

# 4
# def camel_to_snake(camel_case):
#     snake_case = ''
#     for char in camel_case:
#         if char.isupper():
#             if snake_case:
#                 snake_case += '_'
#             snake_case += char.lower()
#         else:
#             snake_case += char
#     return snake_case
# c = input("Enter a camel case string: ")
# snake = camel_to_snake(c)
# print(f"Snake case string: {snake}")