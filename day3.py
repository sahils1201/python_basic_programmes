# x=[1,"hello",(3+2j)]
# print (x[0:2])

# Modifying and changing lists
# x=[1,2,3]
# y=x
# z=x.append(12)
# z==None
# True
# print (y)
# x=x+[9,10]
# print(x)
# print(y)
# print(z)
# x=(1,2,3)
# print (x[1:])
# y=(2,)
# print(y)

# Dictionaries
# In dictionaries the content always comes in key and value pair (key:value)
# d={1:'hello','two':42,'blah':[1,2,3],'new':{10:'yo bro wassup',11:'wasgood'}}
# print(d)
# print(d['blah'])
# print(d['new'])
# print(d['new'][10])
# # to delete smn specific we first write the dictionary name then 
# del(d['new'][10])
# print(d['new'])
# print(d)

#1. WAP to create list tuple and disctionary of 7 elements.
#2. WAP to create tuple with different data types.
#3. WAP to arrange list in descending order.
#4. WAP to demonstrate control statement break.
#5. DAP to manage a Library Catalog.Use control statement


# # 1.
# my_list=[1,2,3,4,5,6,('I','II','III','IV','V','VI',{1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven'})]
# print(my_list)
# print(my_list[6])
# print(my_list[6][6])

# 2.
# my_tuple=(10,'Sahil Sable', 9.6,)
# 3.
# n=int(input("Enter range of list: "))
# lis=[]
# for i in range(n):
#     lis.append(int(input(f"Enter {i} value: ")))

# print(f"List before sort: {lis}")
# for i in range(n - 1):
#         for j in range(0, n - i - 1):
#             if lis[j] < lis[j + 1]:
#                 lis[j], lis[j + 1] = lis[j + 1], lis[j]

# print(f"List after sorting: {lis}")