# vehicle parent class & other are child class using override 

# class Vehicle:
#     pass 

# class Bike:
#     pass

# class Car:
#     pass

# class Cycle:
#     pass 

import math  # For circle area calculation

class Vehicle:  # Parent class
    def __init__(self, name):
        self.name = name

    def start(self):
        print(f"{self.name} is starting...")

    def stop(self):
        print(f"{self.name} has stopped.")

    def display_info(self):
        print("Not implemented")


class Bike(Vehicle):  # Child class 1 - inherits from Vehicle
    def __init__(self, name, wheels=2):
        super().__init__(name)
        self.wheels = wheels

    def display_info(self):
        # Override: Bike-specific info
        print(f"{self.name}: {self.wheels}-wheeler bike")

    def wheelie(self):
        print(f"{self.name} is doing a wheelie!")


class Car(Vehicle):  # Child class 2 - inherits from Vehicle
    def __init__(self, name, doors=4):
        super().__init__(name)
        self.doors = doors

    def display_info(self):
        # Override: Car-specific info
        print(f"{self.name}: {self.doors}-door car")

    def honk(self):
        print(f"{self.name}: Beep beep!")


class Cycle(Vehicle):  # Child class 3 - inherits from Vehicle
    def __init__(self, name, gears=1):
        super().__init__(name)
        self.gears = gears

    def display_info(self):
        # Override: Cycle-specific info
        print(f"{self.name}: {self.gears}-gear cycle")

    def pedal(self):
        print(f"{self.name}: Pedaling fast!")


# Test all vehicles
print("=== Vehicle Hierarchy Demo ===\n")

# Base class test
vehicle = Vehicle("Generic Vehicle")
vehicle.start()  # Inherited from Vehicle
vehicle.display_info()  # Not implemented

print("\n--- Bike ---")
bike = Bike("Yamaha R15")
bike.start()  # Inherited
bike.display_info()  # Overridden
bike.wheelie()  # Bike-specific
bike.stop()  # Inherited

print("\n--- Car ---")
car = Car("Toyota Corolla")
car.start()
car.display_info()  # Overridden
car.honk()  # Car-specific
car.stop()

print("\n--- Cycle ---")
cycle = Cycle("Mountain Cycle", 21)
cycle.start()
cycle.display_info()  # Overridden
cycle.pedal()  # Cycle-specific
cycle.stop()

# Polymorphism: Mixed list of vehicles
vehicles = [bike, car, cycle]
print("\n--- All Vehicles ---")
for v in vehicles:
    v.start()
    v.display_info()
    v.stop()


