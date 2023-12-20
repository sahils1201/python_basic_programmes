#  3.⁠ ⁠Write a python function to multiply all numbers in a list
def prodList(size):
    lts=[]
    for i in range(size):
        x=int(input("Enter the numbers: "))
        lts.append(x)
    print(lts)

    prod=1
    for i in lts:
        prod*=i
    return prod
size=int(input("Enter number of elements: "))
print(prodList(size))
