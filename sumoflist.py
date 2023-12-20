lts=[]
size=int(input("Enter number of elements: "))
for i in range(size):
    x=int(input("Enter the numbers: "))
    lts.append(x)
print(lts)

sum=0
for i in lts:
    sum+=i
print('Sum is',sum)
