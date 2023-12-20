#  5.⁠ ⁠Write a python function to calculate factorial of a number (non-negative integer)
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
n=int(input('enter number:'))
print(fact(n))