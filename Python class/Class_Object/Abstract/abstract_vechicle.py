## Abstract structure

from abc import ABC,abstractmethod 
class Vechicle (ABC):
    @abstractmethod
    def start():
        pass

    @abstractmethod
    def stop():
        pass

    @abstractmethod
    def drive():
        pass
    

class Car(Vechicle):
## we need above 3 methods or else it will not compile 

    def start(self):
        # self.start = start
        print ("Start the engine then Car will be started")

    def drive(self):
        print("After start the engine drive the Car")
    
    def stop(self):
        print("Stop the Car when you reach the destination")
    

class Bike(Vechicle):
     
    ## we need above 3 methods or else it will not compile we will have a error 
    def start(self):
        # self.start = start
        print ("Start the engine then bike will be started")

    def drive(self):
        print("After start the engine drive the bike")
    
    def stop(self):
        print("Stop the bike when you reach the destination")
     

car = Car() ## object consturction / object initialization  

car.start()
car.drive()
car.stop()

bike = Bike()

bike.start()
bike.drive()
bike.stop()


## vechicle = Vechicle()

## TypeError: Can't instantiate abstract class Vechicle without an implementation for abstract methods 'drive', 'start', 'stop'


