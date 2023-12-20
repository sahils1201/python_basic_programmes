# def hello():
#     print('Hello World!')
# hello()

# def addn(a,b):
#     print('The sum is',a+b)

# a=int(input('Enter value of a: '))
# b=int(input('Enter value of b: '))
# addn(a,b)

# def calc(a,b,op):
#     if op == '+':
#         print('The sum is',a+b)
#     elif op=='-':
#         print('The difference is',a-b)
#     elif op=='*':
#         print('The product is',a*b)
#     elif op =='/':
#         print('The quotient is',a/b)
#     elif op == '%':
#         print('The remainder is',a%b)
#     elif op =='power':
#         print('The exponentiation is',a**b)
#     elif op=='//':
#         print('The floor div is',a//b)

# a=int(input('Enter value of a: '))
# b=int(input('Enter value of b: '))
# op=input('Enter operation you would like to perform: ')
# calc(a,b,op)

# There are two types of arguments:
# 1.Positional arguments - No order flexibility
# def newfun(age,name):
#     print('Your name is:',name)
#     print('Your age is: ',age)
# newfun(18,'sahil')
# 2.Keyword based Arguments - Flexibility of order
# def newfun(age,name):
#     print('Your name is:',name)
#     print('Your age is: ',age)
# newfun(name='Sahil',age=18)



# def addn(*args):
#     sum=0
#     for i in args:
#         for i in lts:
#             sum=sum+i
#     print('The sum of the elements is',sum)

# n=int(input('Enter the number of numbers you want to add: '))
# lts=[]
# for j in range(n):
#     num=int(input('Enter number: '))
#     lts.append(num)
# addn(lts)
# a=int(input('Enter value of a: '))
# b=int(input('Enter value of b: '))
# addn(a,b)


# def add(*args):
#     sum1=sum(args)
#     return sum1


# l=int(input("Enter number of arguements: "))
# my_list=[]
# for i in range(l):
#     my_list.append(int(input("Enter value: ")))
# print(add(*my_list))


# def myfun(*args,**kwargs):
#     for key,value in kwargs.items():
#         print(key, '=', value)
#     for i in args:
#         print(i)

# myfun('hello','wassup',name='sahil',age=18,college='ITM')

# def namefun(**kwargs):
#     for key,value in kwargs.items():
#         print('Welcome',value, 'to ITM!') 
#         print(key,'=',value)
# choice=str(input('Would you like to enter a name?'))
# if choice=='yes':
#     n=str(input('What is your name?'))
# elif choice=='no':
#     choice=str(input('Would you like to enter an email?'))
#     if choice=='yes':
#         email=str(input('What is your email?'))
#     else:
#         pass
# else:
#     numb=int(input('What is your phone number?'))
# namefun(name=n,mail=email,number=numb)


# namefun(name = n)
# choice=str(input('Would you like to enter an email?'))



# def namefun(**kwargs):
#     for key, value in kwargs.items():
#         # print('Welcome', value, 'to ITM!')
#         print(key, '=', value)

# choice = input('Would you like to enter a name? ')
# count = 0
# if choice.lower() == 'yes':
#     name = input('What is your name? ')
#     namefun(name=name)
# if count == 0:
#     choice = input('Would you like to enter an email? ')
#     if choice.lower() == 'yes':
#         email = input('What is your email? ')
#         namefun(mail=email)
#     elif choice.lower()=='no':
#         pass
# if count==0:
#     number = input('What is your phone number? ')
#     namefun(number=number)


# def namefun(**kwargs):
#     for key, value in kwargs.items():
#         print('Welcome', value, 'to ITM!')
#         print(key, '=', value)
# details = {}
# choice = input('Would you like to enter a name? ')
# count = 0
# if choice.lower() == 'yes':
#     name = input('What is your name? ')
#     details['Name']=name
#     # namefun(name=name)
# if count == 0:
#     choice = input('Would you like to enter an email? ')
#     if choice.lower() == 'yes':
#         email = input('What is your email? ')
#         details['Email']=email
#         # namefun(mail=email)
#     elif choice.lower()=='no':
#         pass
# if count==0:
#     number = input('What is your phone number? ')
#     details['Phone Number']=number
#     # namefun(number=number)


# print("\nFull Details:")
# for key, value in details.items():
#     print(f"{key} = {value}")
# var1=10
# def func():
#     var1=3
#     print(var1)
#     def func2():
#         nonlocal var1
#         var1=4
#         print(var1)
#     func2()
#     print(var1)
# func()
# print(var1)

# def fun_name(name,age):
#     z=name+age
#     print(z)

# fun_name(name='ABC',age=32)
# fun_name('abc',32)
# fun_name('ABC',age=32)
# fun_name(48,age=32)
