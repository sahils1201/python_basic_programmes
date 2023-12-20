# class Parent:
#     def add(self,x,y):
#         return x+y
    
# class Child(Parent):
#     def getdata(self):
#         self.x=int(input('Enter value: '))
#         self.y=int(input('Enter value: '))

# obj1 = Child()
# obj1.getdata()
# result = obj1.add(obj1.x, obj1.y)
# print("Sum of the values:", result)

# class Area:
#     def prod(self,a,b):
#         return a*b
    
# class Rect(Area):
#     def getdata(self):
#       self.a=int(input("Enter the side a:"))
#       self.b=int(input("Enter the side b:"))

# class Square(Area):
#     def getdata(self):
#       self.a=int(input("Enter the side of square:"))
#       self.b=self.a
     
# obj1 = Rect()
# obj2=Square()
# obj1.getdata()
# obj2.getdata()
# print("Area of the square:",obj2.prod(obj2.a,obj2.b))
# result = obj1.prod(obj1.a, obj1.b)
# print("Area of the rectangle:", result)

# class Area:
#     def area(self,a):
#         return a**2
# class Square(Area):
#     def getdata(self):
#       self.a=int(input("Enter the side a:"))
# obj1=Square()
# obj1.getdata()
# print('The area of the square is:',obj1.area(obj1.a))

# class LetsUpgrade:
#     def __init__(self):
#         self.subjects = {1: 'AIDS', 2: 'AIML', 3: 'Full-Stack', 4: 'UI/UX'}
#         self.trainer = 'Sahil Sable'
#         self.duration = {1: 1, 2: 1, 3: 0.5, 4: 0.5}

# class ITM:
#     def __init__(self):
#         self.subjects = {1: 'Bsc Finance', 2: 'Hotel Management', 3: 'Health and Science', 4: 'Fashion and Design'}
#         self.trainer = 'Ayush Aryan'
#         self.duration = {1: 3, 2: 3, 3: 3, 4: 3}

# class Child(LetsUpgrade, ITM):
#     def __init__(self):
#         super().__init__()

#     def get_subject_details(self, choice):
#         if choice in self.subjects:
#             print(f"Subject: {self.subjects[choice]}")
#             print(f"Trainer: {self.trainer}")
#             print(f"Duration: {self.duration[choice]} months")
#         else:
#             print("Invalid choice")

# def main():
#     child_obj = Child()

#     print("\nChoose a subject:")
#     print("1. AIDS\n2. AIML\n3. Full-Stack\n4. UI/UX\n"
#           "5. Bsc Finance\n6. Hotel Management\n7. Health and Science\n8. Fashion and Design\n"
#           "9. Exit")

#     choice = int(input("Enter your choice (1-9): "))

#     if choice == 9:
#         print("Exiting program.")
#     else:
#         child_obj.get_subject_details(choice)

# if __name__ == "__main__":
#     main()

# class LetsUpgrade:
#     lu_courses=[{'Subject': 'Math', 'Trainer': 'Saikiran', 'Duration': 100},
#                 {'Subject': 'Python', 'Trainer': 'Saikiran', 'Duration': 150},
#                 {'Subject': 'Web design', 'Trainer': 'Prasad', 'Duration': 130}]

# class ITM:
#     itm_courses=[{'Subject': 'Math', 'Trainer': 'Sheetal', 'Duration': 90},
#                 {'Subject': 'DSA', 'Trainer': 'Sumit', 'Duration': 200},
#                 {'Subject': 'Computer Fundamentals', 'Trainer': 'Sumit', 'Duration': 150}]

# class CourseSelector(LetsUpgrade, ITM):
#     def print_subjects(self, selected_class):
#         if selected_class == 'letsupgrade':
#             subjects = [course['Subject'] for course in self.lu_courses]
#         elif selected_class == 'itm':
#             subjects = [course['Subject'] for course in self.itm_courses]
#         else:
#             subjects = []

#         if not subjects:
#             print(f"No subjects available for {selected_class}")
#             return

#         print(f"Available subjects for {selected_class}: {subjects}")

#         selected_subject = input("Enter the subject you want details for: ")

#         if selected_subject.lower() in subjects:
#             if selected_class == 'letsupgrade':
#                 selected_course = next(course for course in self.lu_courses if course['Subject'] == selected_subject)
#             elif selected_class == 'itm':
#                 selected_course = next(course for course in self.itm_courses if course['Subject'] == selected_subject)

#             print(f"\nDetails of {selected_subject} in {selected_class}:")
#             print(f"Trainer: {selected_course['Trainer']}")
#             print(f"Duration: {selected_course['Duration']} hours")
#         else:
#             print(f"{selected_subject} is not available in {selected_class}")

# course_selector = CourseSelector()

# selected_class = input("Enter the class (LetsUpgrade or ITM): ")
# course_selector.print_subjects(selected_class.lower())

# class Grandfather:
#     def __init__(self, assets):
#         self.assets = assets

#     def display_info(self):
#         print(f"Grandfather's assets: ${self.assets}")


# class Father(Grandfather):
#     def __init__(self, assets, business):
#         Grandfather.__init__(self, assets)
#         self.business = business

#     def display_info(self):
#         Grandfather.display_info(self)
#         print(f"Father's business: {self.business}")


# class Child(Father):
#     def __init__(self, assets, business, education):
#         Father.__init__(self, assets, business)
#         self.education = education

#     def display_info(self):
#         Father.display_info(self)
#         print(f"Child's education: {self.education}")


# grandfather_assets = 1000
# father_assets = 5000
# business_info = "Family Business Inc."
# child_education = "College Graduate"

# # Creating instances
# grandfather = Grandfather(assets=grandfather_assets)
# father = Father(assets=father_assets, business=business_info)
# child = Child(assets=None, business=None, education=None)

# # Calculating and setting the child's assets
# child.assets = grandfather.assets + father.assets

# # Displaying information
# grandfather.display_info()
# print("\n")
# father.display_info()
# print("\n")
# child.display_info()


#Multi-Level Inheritance

# class Grandfather:
#     def __init__(self, assets):
#         self.assets = assets

#     def display_grandfather_assets(self):
#         print("Grandfather's Assets: ₹", self.assets)

# class Father(Grandfather):
#     def __init__(self, assets, income):
#         super().__init__(assets)
#         self.income = income

#     def display_father_income(self):
#         print("Father's Income: ₹", self.income)

# class Son(Father):
#     def __init__(self, assets, income, pocket_money):
#         super().__init__(assets, income)
#         self.pocket_money = pocket_money

#     def display_son_pocket_money(self):
#         print("Son's Pocket Money: ₹", self.pocket_money)


# grandfather = Grandfather(10000000)
# father = Father(500000, 75000)
# son = Son(200000, 30000, 5000)

# grandfather.display_grandfather_assets()
# father.display_father_income()
# son.display_son_pocket_money()


#Multi-Level Inheritance

# #CHAT GPT Code ⬇️
# class Grandfather:
#     def __init__(self, assets):
#         self.assets = assets

#     def display_grandfather_assets(self):
#         print("Grandfather's Assets: ₹", self.assets)

# class Father(Grandfather):
#     def __init__(self, assets, income):
#         super().__init__(assets)
#         self.income = income

#     def display_father_income(self):
#         print("Father's Income: ₹", self.income)

# class Son(Father):
#     def __init__(self, assets, income, pocket_money):
#         super().__init__(assets, income)
#         self.pocket_money = pocket_money

#     def display_son_pocket_money(self):
#         print("Son's Pocket Money: ₹", self.pocket_money)


# grandfather = Grandfather(1000000)
# father = Father(500000, 75000)
# son = Son(200000, 30000, 5000)

# grandfather.display_grandfather_assets()
# father.display_father_income()
# son.display_son_pocket_money()




#vrishank code ⬇️
# class Grandfather:
#     def __init__(self, assets):
#         self.assets = assets

# class Father(Grandfather):
#     def __init__(self, assets, business):
#         super().__init__(assets)
#         self.business = business

# class Child(Father):
#     def __init__(self, assets, business, education):
#         super().__init__(assets, business)
#         self.education = education

# grandfather_assets = 1000
# father_assets = 5000
# business_info = "Family Business"
# child_education = "Computer Science Engineer"
# #instance
# grandfather = Grandfather(assets=grandfather_assets)
# father = Father(assets=father_assets, business=business_info)
# child = Child(assets=None, business=None, education=None)

# child.assets = grandfather.assets + father.assets
# child.business = father.business
# child.education = child_education

# print(f"\nGrandfather's assets: ₹{grandfather.assets}")
# print(f"Father's assets: ₹{father.assets}")
# print(f"Child's assets: ₹{child.assets}")
# print(f"\nChild's business: {child.business}")
# print(f"\nChild's education: {child.education}\n")




# # Raheel Code ⬇️
# class GrandFather:
#     def __init__(self):
#         self.name = " GrandFather"
#         self._assets = 1500000

# class Father(GrandFather):
#     def __init__(self):
#         super().__init__()
#         self.name = self.name + " Father"
#         self._inharitedAssets = self._assets 
#         self._purchasedAssets = 200000
#         self._totalAssets = self._inharitedAssets + self._purchasedAssets

# class Child(Father):
#     def __init__(self, name, assets):
#         super().__init__()
#         self.name = self.name + " " + name
#         self.__inharitedAssets = self._totalAssets
#         self.__purchasedAssets = assets
#         self._totalAssets = self.__inharitedAssets + self.__purchasedAssets
    
#     def displayData(self):
#         print("Name: ", self.name)
#         print("Assets: ", self._totalAssets)

# obj = Child("Child",100000)
# obj.displayData()


# 1.⁠ ⁠Design a library catalogue system using inheritance. 
# take base class library item and derieved classes book, dvd and journal. 
# each derived class should have unique attributes and methohds 
# and system should support checking in nd checking out System.

# import random
# class libraryItem:
#     def code(self,id):
#         self.id=random(1,100)

# class book(libraryItem):
#     def book(self,name,code):
#         print('')

class LibraryItem:
    library_items = []


    def __init__(self, item_type, item_name, item_id, item_count=0):
        self.item_type = item_type
        self.item_name = item_name
        self.item_id = item_id
        self.item_count = item_count

        item_data = {
            'item_type': self.item_type,
            'item_name': self.item_name,
            'item_id': self.item_id,
            'item_count': self.item_count
        }

        if self.item_type == 'book':
            self.author_name = input("Enter author's name for the book: ")
            item_data['author_name'] = self.author_name
        elif self.item_type == 'journal':
            self.publisher_name = input("Enter publisher's name for the journal: ")
            item_data['publisher_name'] = self.publisher_name
        elif self.item_type == 'dvd':
            self.director_name = input("Enter director's name for the DVD: ")
            item_data['director_name'] = self.director_name
        else:
            raise ValueError("Invalid item_type. Please retry with 'book', 'journal', or 'dvd'.")

        self.library_items.append(item_data)

    def display_info(self):
        for item_data in self.library_items:
            print("Information about library items:")
            for key, value in item_data.items():
                print(f"{key}: {value}")
            print("\n")

    def check_out(self, item_name):
        for item_data in self.library_items:
            if item_data['item_name'] == item_name:
                if item_data['item_count'] > 0:
                    print(f"Checking out {item_name}")
                    item_data['item_count'] -= 1
                else:
                    print(f"All copies of {item_name} are checked out.")
                return
        
        print(f"{item_name} not found in the library.")

    def check_in(self, item_name):
        for item_data in self.library_items:
            if item_data['item_name'] == item_name:
                print(f"Checking in {item_name}")
                item_data['item_count'] += 1
                return
        
        self.__init__(self.item_type, item_name, len(self.library_items) + 1, item_count=1)


class Book(LibraryItem):
    def __init__(self, item_name, item_id):
        super().__init__('book', item_name, item_id)


class DVD(LibraryItem):
    def __init__(self, item_name, item_id):
        super().__init__('dvd', item_name, item_id)


class Journal(LibraryItem):
    def __init__(self, item_name, item_id):
        super().__init__('journal', item_name, item_id)


book = Book('The Great Gatsby', 1)      #item_name and item_id
dvd = DVD('Inception', 2)
journal = Journal('Scientific American', 3)

book.check_in('The Great Gatsby')       #plus 1 to item_count
book.check_in('The Great Gatsby')
book.check_in('The Great Gatsby')
book.check_in('The Great Gatsby')
book.check_in('The Great Gatsby')
book.display_info()
book.check_out('The Great Gatsby')
book.display_info()
book.display_info()

dvd.check_in('Inception')
dvd.display_info()

journal.check_out('Scientific American')
journal.display_info()