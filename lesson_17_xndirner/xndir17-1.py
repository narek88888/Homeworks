# Dog class
# Class variable
# number of dogs
# Instance variables
# breed
#  name
#  color
#  age
# Data methods
# bark
# sit


class Dog :
    number_of_dogs = 0
    def __init__(self, name, breed, color, age) :

        self.name = name # dzax koxmy petq e grenq te inchi vra enq kacnhum, isk aj koxmum lyuboi ban kap unecox
        self.breed = breed
        self.color = color
        self.age = age

        Dog.number_of_dogs+=1
       
        

    def bark(self) :
        print(f"{self.breed} hachum e ")
    def sit(self) : 
        print(f"{self.breed} nstum e ")
           

x = Dog("Jeko", "avcharka", "black", 4)
y = Dog("Chalo", "pitbull", "white", 6)
z = Dog("Rex", "doberman", "brown", 3)

print(Dog.number_of_dogs)


# menq petqa initi vra += 1 anenq
         
