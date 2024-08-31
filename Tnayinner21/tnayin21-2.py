# 21-2. Class Exercise:
# Create a Python class representing a basic calculator with methods for addition,
# subtraction, multiplication, and division.


class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"{self.x} {self.y}"
    
    def __add__(self, other):
        return self.x + other.x, self.y + other.y
        
    def __sub__(self, other):
        return self.x - other.x, self.y - other.y
    
    def __mul__(self, other):
        return self.x * other.x, self.y * other.y
    
    def __truediv__(self, other):
      return self.x / other.x, self.y / other.y
    
numbers1 = Calculator(10,2)
numbers2 = Calculator(1,5)

print(numbers1.x + numbers2.x)
print(numbers1 - numbers2)
print(numbers1 * numbers2)
print(numbers1 / numbers2)























