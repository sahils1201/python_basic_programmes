num=int(input("Enter number of rows: "))
# new=""
# for i in range(num):
#     new+="*"
#     print(new)

# for i in range(num,0,-1):
#     for j in range(0,i):
#         print("*",end="")
#     print()

# num=int(input("Enter number of rows: "))
# # new=""
# k=num-1
# for i in range(0,num-1):
#     for j in range(0,k):
#         print(end=" ")
#     k=k-1
#     for j in range(0,i+1):
#         print("* ",end="")

#     print("\r")

# k=num-1
# for i in range(num,0,-1):
#     for j in range(0,num-i):
#         print(" ",end= "")
  
#     for j in range(0,i):
#         print("*",end= " ")
#     print()


    # new+="*"
    # print(new)



# n=str(input("Enter name: "))
# length=len(n)
# for i in range(0,length):
#     for j in range(0,i+1):
#         print(n[i],end="")
#     print()

# n=int(input("Enter number of rows: "))
# val=65
# for i in range (0,n):
#     for j in range(0,i+1):
#         alph=chr(val)
#         print(alph,end=" ")
#     val=val+1
#     print()



# # Diamond Boder Pattern

# n = int (input ("Enter number of rows: "))

# for i in range (1, n + 1):
#     for j in range (1, n -  i + 1):
#         print (" ", end = " ")
    
#     for j in range (1, 2 * i):
#         if j == 1 or j == 2 * i - 1:
#             print ("*", end = " ")
#         else:
#             print (" ", end = " ")
#     print()

# for i in range (n - 1, 0, -1):
#     for j in range (1, n - i + 1):
#         print (" ", end = " ")
#     for j in range (1, 2 * i):
#         if j == 1 or j == 2 * i - 1:
#             print ("*", end = " ")
#         else:
#             print (" ", end = " ")
#     print()

# n=int(input("Enter number of rows: "))
# val=65
# for i in range (0,n):
#     for j in range(0,i+1):
#         alph=chr(val)
#         print(alph,end=" ")
#     val=val+1
#     print()

# abcde pattern

# for char5 in range(ord('C'),ord('E')+1):
#     print(" ",chr(char5),end="")
# print('\n')


# for char4 in range(ord('B'),ord('E')+1):
#     print("",chr(char4), end=' ')
# print('\n')

# for char in range(ord('A'),ord('E')+1):
#     print(chr(char),end="  ")
# print("\n")

# for char1 in range(ord('B'),ord('E')+1):
#     print("",chr(char1), end=' ')
# print('\n')

# for char3 in range(ord('C'),ord('E')+1):
#     print(" ",chr(char3),end="")

# rows = int(input("Enter the number of rows: "))

# for i in range(1, rows + 1):
#     for j in range(i, rows):
#         print(" ", end="")
    
#     for j in range(1, 2 * i):
#         print("*", end="")
    
#     for j in range(2 * i, 2 * rows):
#         print(" ", end="")
    
#     for j in range(1, 2 * i):
#         print("*", end="")
    
#     print()

# rows = int(input("Enter the number of rows: "))

# for i in range(1, rows + 1):
#     for j in range(i, rows):
#         print(" ", end="")
    
#     for j in range(1, 2 * i):
#         print("*", end="")
    
#     for j in range(2 * i, 2 * rows):
#         print(" ", end="")
    
#     for j in range(1, 2 * i):
#         print("*", end="")
    
#     print()
