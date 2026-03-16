#========================================================================================

class Car():
    wheel = 4
    def __init__ (self,data):
        self.data = data

    def car_info(self):
       for i in self.data:
        print(f"{i[1]} {i[0]} car has {self.wheel} wheels")


car = [["red","BMW"],["blue","Audi"]]

car_details = Car(car)
car_details.car_info()