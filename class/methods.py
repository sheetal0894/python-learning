class User:
    class_variable = 5
    cass_username = "Rahul"
    class_password = "1234"

    def __init__(self, username, password):
        self.username = username
        self.password = password


     # instance method
    def login(self):
         if self.username == User.cass_username and self.password == User.class_password:
          print("Login successful")
         else:
          print("Login failed")

    @staticmethod
    def static_method(email):
       if email.endswith("@gmail.com"):
           print("Valid email")
       elif email.endswith("@yahoo.com"):
           print("Valid email")
       else:
           print("Invalid email")           

username = input("Enter username: ")
password = input("Enter password: ")

u1 = User(username, password)
u1.login()
User.static_method("test@gmail.com")