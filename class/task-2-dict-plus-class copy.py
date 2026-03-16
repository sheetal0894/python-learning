employees = [
 {"name":"Rahul","skill":"Python","salary":50000},
 {"name":"Amit","skill":"DevOps","salary":70000}
]

class Company:
    company = "Microsoft"

    def __init__(self,name,skill,salary):
        self.name = name
        self.skill = skill
        self.salary = salary

    def details(self):
        print(f"{self.name} is working in {self.company} company with {self.skill} skill and salary is {self.salary}")

for emp in employees:
    emp_details = Company(**emp)
    emp_details.details()

    """
    **emp is used to unpack the dictionary emp. When we use **emp, it takes each key-value pair of the dictionary and passes it as a separate keyword argument to the constructor of the Company class. For example, if emp is {"name":"Rahul","skill":"Python","salary":50000}, then **emp will unpack it into three separate keyword arguments: name="Rahul", skill="Python", and salary=50000. This allows us to create an instance of the Company class for each employee in the list and call the details method to print their information.
    Example:
    emp = {"name":"Rahul","skill":"Python","salary":50000}
    emp_details = Company(**emp)  # This will unpack the dictionary and pass the values as keyword arguments to the constructor
    will create an instance of the Company class with name="Rahul", skill="Python",
    and salary=50000.
    Company(name="Rahul", skill="Python", salary=50000)
    """ 