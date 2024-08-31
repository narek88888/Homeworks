# Exercise 5: Sum of Squares Function
# Write a function that calculates the sum of squares of numbers from 1 to n.

def sum_of_squares_function(number) :
    
    sum = 0
    i = 0
    
    while i <= number:
        sum += i**2
        i += 1
    return sum    

print(sum_of_squares_function(5))

        





