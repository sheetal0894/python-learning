# class Employee:

#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

# class Developer(Employee):

#     def __init__(self, name, salary, language):
#         super().__init__(name, salary) #super() is used to call the parent class constructor and initialize the name and salary attributes
#         self.language = language
#     def dev_info(self):
#         print(self.name, self.salary, "works with", self.language)

# dev1 = Developer("Rahul", 50000, "Python")
# dev1.dev_info()


class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        super().__init__()  #super() is used to call the parent class constructor and execute the code inside it, which prints "A". After that, it continues to execute the code in the B class constructor
        print("B")

b = B()



