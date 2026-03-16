class Calculator():
    def __init__(self, number):
        self.number = number

    def square(self):
        s = self.number*self.number
        print(f"square of {self.number} is {s}")

    def cube(self):
        c = self.number*self.number*self.number
        print(f"square of {self.number} is {c}")

    def squareRoot(self):
        sr = self.number
        print(f"square of {self.number} is {sr}")

cal = Calculator(4)
cal.square()
cal.cube()
cal.squareRoot()
