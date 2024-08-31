# Exercise 3: Average Function
# Write a function that calculates the average of a list of numbers.

def average_number(number) :

    sum = 0
    
    x = len(number)
    
    for i in number :
       
        sum = sum + i

    return sum / x

list_of_numbers = [1, 2, 3, 4]

print(average_number(list_of_numbers))

        





