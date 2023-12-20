#Write a progrm to find the largest among three numbers.
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=int(input("Enter a number: "))

if a>b and a>c:
    print(a, 'Is the largest number.')
elif b>a and b>c:
    print(b, 'Is the largest number.')
elif c>a and c>b:
    print(c, 'Is the largest number.')
