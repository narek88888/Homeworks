# Write an abstract class with name Employee
# Write 2 employee classes by inheriting from abstract Employee
# Write function
# get_info -> return string with name and position
# calculate_salary -> return float with information about employee salary
# Calculate salary should be different for 2 classes


from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def salary_calculate(self):
        pass
     
class Programmer(Employee): 
     
    def __init__(self, salary, bonus, position ): 
        self.bonus = bonus
        self.salary = salary
        self.position = position

    def get_info(self):
        return f"John is a programmer he is paid {self.salary} dolar and this month he will receive bonus {self.bonus} dolar, his position is {self.position}"
        
    def salary_calculate(self):
        self.salary += self.bonus
        return  f"Salary of John with bonus {self.salary} dolar" 

    
class Doctor(Employee):
     
     def __init__(self, salary, position):
        self.salary = salary
        self.position = position
          
     def get_info(self):
         return f"Bejamin is a doctor he is paid {self.salary} dolar and his position is {self.position} "
           
     def salary_calculate(self):
        return  f"Salary of Benjamin {self.salary} dolar"



programmer = Programmer(5000, 500, "software engineer")
doctor = Doctor(4000, "stomatologist")

print(programmer.get_info())
print(programmer.salary_calculate())

print(doctor.get_info())
print(doctor.salary_calculate())