# List=[10,20,30,40,50]
# print(List)
# print(List[0])
# print(List[1])
# print(List[2])
# print(List[3])
# print(List[4])
# print(List.index(10))
# print(List.index(20))
# print(List.index(30))
# print(List.index(40))
# print(List.index(50))

# cities=['New Delhi','Mumbai','Pune','Nasik']
# print(cities)

# new=[1,'Mumbai',2,'Sahil',3.14]
# print(new)

# l=[1,2,3,4,5,6,7,8,9]
# l.append(10)
# print(l) 
# l.sort(reverse=True)
# print(l)
# l.pop(0)
# print(l)

# List=[10,20,30,40,50,60,70,80,90,100]
# List.insert(5,100)
# print(List.count(100))
# List.reverse()
# print(List)

# print(List)
# count=0
# for i in range(List):
    
# odev=[1,22,33,44,55]
# odd=[]
# even=[]
# for i in (odev):
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(odd)
# print(even)

#WAP

# list.sort(reverse = True)
# print(list)
# print(list[:-1])
# z = list + list1
# list.append(list1)
# print(z)
# print(list)

matrix_a=[[1,2,3],[4,5,6],[7,8,9]]
matrix_b=[[1,2,3],[4,5,6],[7,8,9]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(matrix_a)):
    for j in range(len(matrix_a[0])):
        result[i][j]=matrix_a[i][j] + matrix_b[i][j]
print(result)