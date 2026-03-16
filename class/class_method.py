class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split(",")
        return cls(name, int(age))
    
    def normal_fuct(self,details):
        name, age = details.split(",")
        return self.name,self.age
    

u = User.from_string("Rahul,25")
print(u.name)
print(u.age)

user = User("Amit, 30")
print(user.normal_fuct("Amit, 30"))

#class method is used to create an object of the class using a string data. It is a factory method that takes a string as input and returns an object of the class.