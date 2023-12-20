# class Student:
#     count=0
#     def __init__(self,name,age):
#         self.name=name=input('Enter name: ')
#         self.age=age=int(input('Enter age:'))
#         Student.count+=1
#     def display(self):
#         print('Name:',self.name,'Age:',self.age)

# ran=int(input('Enter the number of students you want to enter:'))
# for i in range(ran):
#     i=Student(__name__,0)
#     for i in range(ran):
#         i.display()
# print(Student.count)

# class ITM:
#     count = 0
#     pg=0
#     bt=0
#     def get(self):
#         self.name = input("Enter your name ")
#         self.age = int(input("Enter your age "))
#         self.department =input("Which department you want in\n1.PGdm\n""2.Btech\n ")
#         ITM.count +=1
#         if self.department== 1:
#             ITM.pg+=1
#         else:
#             ITM.bt+=1
#     def __del__(self):
#         print('Object destroyed.')
#     def display(self):
#         print("Name:-",self.name)
#         print("Age:-",self.age)
#         print("Department is",self.department)


# obj1 = ITM()
# obj1.get()
# obj2 = ITM()
# obj2.get()
# obj1.display()
# obj2.display()
# del obj1
# del obj2
# print("number of admissions are",ITM.count)
# print()

# class Student:  
#     count = 0
#     def __init__(self):
#         self.name = input("Enter Student Name: ")
#         self.age = int(input("Enter Student Age: "))
#         self.department = input("Enter Student Department (PGDM(p)/B.Tech(b)): ").capitalize()
#         Student.count += 1
#     def display(self):
#         print("Name:", self.name, "Age:", self.age, "Department:", self.department)
# print("""------ STUDENT ADMIT ------""")
# pgdm_students = []
# btech_students = []
# num_students = int(input("Enter the number of students: "))

# for _ in range(num_students):
#     new_student = Student()
#     new_student.display()
#     if new_student.department == 'P':
#         pgdm_students.append(new_student)
#     elif new_student.department == 'B':
#         btech_students.append(new_student)
# print("*****************************")
# print("\nPGDM Department Students:")
# for student in pgdm_students:
#     student.display()
# print("\nB.Tech Department Students:")
# for student in btech_students:
#     student.display()
# print("\nTotal number of students:", Student.count)


# WAP that has a class store which keeps a record of code and price of each product diplay amenu of all 
# products to the user and prompt him to enter the quantity of each item required and finally generate a bill and display
# the total amount. Private - Code and Amount

# class Store:
#     count=0
#     def getdata(self,name,id,price):
#         self.id=id
#         self.name=name
#         self.price=price
#     def dispdata(self):
#         print()