class Animal:

    def __init__(self, name) :

        self.name = name    

class Dog(Animal) :

    def __init__(self, name, breed):
        
        super().__init__(name)

        self.breed = breed
        
    def make_voice(self) :
        print(f"{self.name} haf-haf")
        
class Cat(Animal) :

    def __init__(self, name, color) :
        super().__init__(name)
        self.color = color

    def make_voice(self) :
        print(f"{self.name} myau")

x = Dog("Rex", "pitbull")        

# et nuynnna inch-vor self ket breed        27-rd toxi graci masin e xossqy


