class Company:
    company = "microsoft"

    def __init__(self,name,skill, salary, pincode):
         self.name = name
         self.skill = skill
         self.salary = salary
         self.pincode = pincode
    def details(self):
         print(f"{self.name} is working in {self.company} company with {self.skill} skill and salary is{self.salary} and pincode is {self.pincode}")

employee = [["Rahul", "Python", 50000, 560001],["Sheetal", "Java", 60000, 560002]]
for emp in employee:
     print(emp)
     emp_details = Company(*emp)
     emp_details.details()


     """
     *emp is used to unpack the list and pass the values as arguments to the constructor of the Company class. It allows us to create an instance of the Company class for each employee in the list and call the details method to print their information.
     
     explanation of *emp:
     The * operator is used to unpack the list emp. When we use *emp, it takes each element of the list and passes it as a separate argument to the constructor of the Company class. For example, if emp is ["Rahul", "Python", 50000, 560001], then *emp will unpack it into four separate arguments: "Rahul", "Python", 50000, and 560001. This allows us to create an instance of the Company class for each employee in the list and call the details method to print their information.   
     Example:
     emp = ["Rahul", "Python", 50000, 560001]     
     emp_details = Company(*emp)  # This will unpack the list and pass the values as arguments to the constructor
     will create an instance of the Company class with name="Rahul", skill="Python", salary=50000, and pincode=560001.
     Company("Rahul","Python",50000,560001)
     """