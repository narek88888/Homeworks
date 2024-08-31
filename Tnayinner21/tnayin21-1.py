# 21-1. Class Exercise:
# Create a Python class representing a Hospital account with methods to schedule visit
# and remove schedule

import datetime

scheduled_visits = []

class HospitalAccount:
    
    def __init__(self, patient_name):

        self.patient_name = patient_name

        
    def visit_schedule(self, visit_datetime):

        if visit_datetime in scheduled_visits:

            return "This visit time has already scheduled"
        
        else:
            scheduled_visits.append(visit_datetime)

            return f"This is your visit datetime {visit_datetime}"
        
        
    def remove_schedule(self, visit_datetime):

        if visit_datetime in scheduled_visits:

            scheduled_visits.remove(visit_datetime)

            return "Your visit datetime removed"
        
now  = datetime.now()
after = now.replace(hour = 15, minute = 0)        
 
person1 = HospitalAccount("Karen Abgaryan")
person2 = HospitalAccount("Armen Martirosyan")
person3 = HospitalAccount("Vazgen Pirumyan")


print(person1.visit_schedule(now))
print(person2.visit_schedule(after))
