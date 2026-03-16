class Student:
    def __init__ (self,name , age, course):
        self.name = name
        self.age = age
        self.course = course
    
    def introduce(self):
        print (f"Hi I am {self.name} and I study {self.course}")

student1 = Student("Rahul", 20, "Python")
student1.introduce()