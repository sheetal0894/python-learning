class Vehicle():
    def start(self):
        print("The cars has started")

class Car(Vehicle):
    def drive(self):
        print("The car is driving")

car = Car()
car.start()
car.drive()