#WAP that creates a list of random integer
#to print index at which particular value exits . if value exists at multiple location in the list , 
# then print all the indices also count the number of times the value is repeated in the list

# import random
# def print_random_numbers(count):
#     for i in range(count):
#         print(random.randint(1, 1000))  # Change the range as per your requirement

# # Example: Print 5 random numbers
# print_random_numbers(5)


# num_list = [1, 2,3,4,5,6,5,4,3,2,1]
# num = int(input("Enter the value to be searched: "))
# i=0
# count =0
# while i<len(num_list):
#     if num == num_list[i]:
#         print(num, "found at location", i)  
#         count +=1
#     i+=1
# print(num, "appears", count, "times in the list")

# words=['sahil','ayush','prem','chonky','ashlin','bhagyashoo','akku','riya']
# charlist=[]
# for i in words:
#     charlist.append(i[0])
# print(charlist)

# WAP to add two matrices
# matrix_a=[[1,2,3],[4,5,6],[7,8,9]]
# matrix_b=[[1,2,3],[4,5,6],[7,8,9]]
# result=[[0,0,0],[0,0,0],[0,0,0]]
# for i in range(len(matrix_a)):
#     for j in range(len(matrix_a[0])):
#         result[i][j]=matrix_a[i][j] + matrix_b[i][j]
# print(result)

# thistuple=('apple','banana','cherry')
# print(len(thistuple))

n=int(input('enter number of emails: '))
mail =[]
for i in range (n):
    mail.append(input(f'Enter {i+1}st email: '))
print(mail)
dom=()
for i in range(0,len(mail)):
    if(mail[i]=='@'):
        dom = mail[i:]
        username = mail[:i]
print("Username",username)
print("Domain",dom)
