#  2.⁠ ⁠Write a python function to sum all numbers in a list
def sumList(size):
    lts=[]
    for i in range(size):
        x=int(input("Enter the numbers: "))
        lts.append(x)
    print(lts)

    summ=0
    for i in lts:
        summ+=i
    return summ
size=int(input("Enter number of elements: "))
print(sumList(size))
