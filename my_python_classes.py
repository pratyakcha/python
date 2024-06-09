#
# My first classes
#Pratyakcha Upadhyay
#

class Vehicle ():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle

    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed

class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.wheels  = 4
        self.doors = 4
        self.enginetype = enginetype
    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "car at", self.speed)

class Motorcycle(Vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("Motorcycle")
        if (hassidecar):
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.enginetype = enginetype
    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "motorcycle at", self.speed)

car1 = Car("gas")
car2 = Car("Electric")
Mc1 = Motorcycle("Gas", True)


print(car1.enginetype)
print(car2.doors)
print(Mc1.wheels)

car1.drive(30)
car2.drive(40)
Mc1.drive(50)