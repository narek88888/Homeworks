# Write a Class named TemperatureSensor that has the attribute
# temperature(private)., default value is 0:
# ● write a getter and setter for the temperature attribute. use the @property
# decorator for the getter and the @attribute.setter for setter
# ● if the temperature is less than 0 or greater than 100 raise a ValueError


class TemperatureSensor :
    def __init__(self, temperature) :
        
        if 0 <= temperature <= 100:
            self.__temperature = temperature
        else:
            raise ValueError("the temperature must be from 1 to 99")
                
    @property
    def temperature(self):
        return self.__temperature
    
    @temperature.setter
    def temperature(self, new_temperature) :
        if 0 <= new_temperature <= 100 :
            self.__temperature = new_temperature
        else:
            raise ValueError("the temperature must be from 1 to 99")
        
x = TemperatureSensor(245)
print(x.temperature)   
