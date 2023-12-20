#  6.⁠ ⁠Write a python function to find square and cube of a number
def square(a):
    return a**2
def cube(a):
    return a**3
choice=int(input('Enter what you want to print:\n1.Square\n2.Cube\n3.Both\n'))
x=int(input('Enter Number:'))
if choice==1:
    print('The square of the number is:',square(x))
elif choice==2:
    print('The square of the number is:',cube(x))
elif choice==3:
    print('The square of the number is:',square(x))
    print('The square of the number is:',cube(x))
else:
    print('Enter 1, 2 or 3.')
