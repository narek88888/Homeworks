# Transport

from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def get_start(self):
        pass

    @abstractmethod
    def get_speed_now(self):
        pass

    @abstractmethod
    def get_stop(self):
        pass

    @abstractmethod
    def get_cooler_on(self):
        pass

    @abstractmethod
    def get_cooler_off(self):
        pass

    @abstractmethod
    def get_heater_on(self):
        pass

    @abstractmethod
    def get_heater_off(self):
        pass

   

class Car(Transport):
    def __init__(self, firm, speed, colour, the_form_of_recharge, number_of_seats):
        self.firm = firm
        self.colour = colour
        self.speed = speed
        self.the_form_of_recharge = the_form_of_recharge
        self.number_of_seats = number_of_seats


    def get_info(self):
        return  f"this {self.firm} max speed is {self.speed}km/h, his colour is {self.colour}, this car is recharged with {self.the_form_of_recharge} and this car has {self.number_of_seats} seats "
    
    def get_start(self):
        return "ready for driving"
    
    def get_speed_now(self,speed_now):
        self.speed_now = speed_now
        return f"{self.speed_now}km/h "
    
    def get_stop(self):
        return "the car is stopping"

    def get_cooler_on(self):
        return "the cooler turned on"
    
    def get_cooler_off(self):
        return "the cooler turned off"
    
    def get_heater_on(self):
        return "the heater turned on"
    
    def get_heater_off(self):
        return "the heater turned off"
    
        
class AirPlane(Transport):
      
      def __init__(self, firm, speed, colour, the_form_of_recharge, number_of_seats):
        self.firm = firm
        self.colour = colour
        self.speed = speed
        self.the_form_of_recharge = the_form_of_recharge
        self.number_of_seats = number_of_seats
        

      def get_info(self):
        return  f"this {self.firm} max speed is {self.speed}km/h, his colour is {self.colour}, this airplane is recharged with {self.the_form_of_recharge} and this ariplane has {self.number_of_seats} seats "
 
      def get_start(self):
            return "ready for driving"
      
      def get_speed_now(self, speed_now):
            self.speed_now = speed_now
            return f"{self.speed_now}km/h "
    
      def get_stop(self):
            return "the car is stopping"

      def get_cooler_on(self):
            return "the cooler turned on"
    
      def get_cooler_off(self):
            return "the cooler turned off"
    
      def get_heater_on(self):
            return "the heater turned on"
    
      def get_heater_off(self):
            return "the heater turned off"
    

car = Car("Mercedes", 280, "black", "fuel", 7)
airplane = AirPlane("Boeing", 975, "white", "A-1 fuel", 138)  

print(car.get_info())
print(car.get_speed_now(60))
print(car.get_cooler_on())

print(airplane.get_info())
print(airplane.get_speed_now(720))
print(airplane.get_heater_on())

        

    

    
        


