class Car():
    wheel = 4
    def __init__ (self, color,brand):
        self.color = color
        self.brand = brand  

    def car_info(self):
       print(f"{self.brand} {self.color} car has {self.wheel} wheels")

car = [["red","BMW"],
       ["blue","Audi"]]

for c in car:
    car_details = Car(*c)
    car_details.car_info()
#========================================================================================

class Car():
    wheel = 4
    def __init__ (self,data):
        self.data = data

    def car_info(self):
       for i in self.data:
        print(f"{i[1]} {i[0]} car has {self.wheel} wheels")


car = [["red","BMW"],
       ["blue","Audi"]]

for c in car:
    car_details = Car(car)
    car_details.car_info()