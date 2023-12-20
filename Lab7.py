#Write a Python program to perform arithmetic calculation. 
#This program accepts two operands and an operator then displays the calculated result.
op=str(input("Enter operation you'd like to perform: "))
a=int(input("Enter value of a: "))
b=int(input("Enter value of b: "))
if (op=='+'):
    print (a+b)
elif(op=='-'):
    print(a-b)
elif(op=='*'):
    print(a*b)
elif(op=='/'):
    print(a/b)
elif(op=='%'):
    print(a%b)
elif(op=='power'):
    print(a**b)
elif(op=='floor division'):
    print(a//b)
