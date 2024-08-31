# 21-10. Class Exercise:
# Create a Python class representing a car with methods for accelerating and braking

class Car:
    def __init__(self, speed):
        self.speed = speed
    
    def accelerate(self, amount):

        self.speed += amount

        return f"The car is accelerating and already speed is {self.speed}km/h"
    
    def brake(self, amount):
        
            self.speed -= amount

            return  f"The car is braking and already speed is {self.speed}km/h " 

    def __repr__(self): 
        return f"{self.speed}"
        

car = Car(0)

print(car.accelerate(20))
print(car.accelerate(40))
print(car.accelerate(20))
print(car.brake(40))
print(car.brake(20))
print(car.brake(20))
print(car)
