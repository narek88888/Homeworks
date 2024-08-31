# Tnayin 11-3
# 3.Factorial
# Write a Python function to calculate the factorial of a number (a non-negative integer).
# The function accepts the number as an argument.


def factorial_number(number) :
    
    i = 1
    factorial = 1
    while  i <= number :
        factorial *= i
        i+=1
    
    return factorial
print(factorial_number(5))


