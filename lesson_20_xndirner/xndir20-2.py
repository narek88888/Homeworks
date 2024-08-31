# Write an abstract class with name GeometricFigure
# Write 2 geometric figure classes by inheriting from GeometricFigure
# Write 2 functions
# get_perimeter -> return perimeter of figure
# get_area -> return area of figure


from abc import ABC, abstractmethod


class GeometricFigure(ABC):

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod    
    def get_area(self):
        pass

class Square(GeometricFigure):
    def __init__(self, side ):
        self.side = side

    def get_perimeter(self):
       
        return 4 * self.side
        
    def get_area(self):
        return self.side**2
    

class Rectangle(GeometricFigure):
    def __init__(self, length, width): 
        self.length = length
        self.width = width

    def get_perimeter(self):
        return self.length + self.width * 2
    
    def get_area(self):
        return self.length * self.width
            

square = Square(12)
rectangle = Rectangle(10, 5)

print(square.get_perimeter())
print(square.get_area())

print(rectangle.get_perimeter())
print(rectangle.get_area())
