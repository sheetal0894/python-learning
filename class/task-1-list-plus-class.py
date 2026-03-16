class Student:
    def __init__ (self,name, age, city):
        self.name=name
        self.age=age
        self.city=city

    def details(self):
        print(f"{self.name} lives in {self.city} and age is {self.age}")

students = [
 ["Rahul",22,"Pune"],
 ["Amit",24,"Mumbai"],
 ["Neha",21,"Delhi"]
]

for s in students:
    student_details = Student(*s)
    student_details.details()