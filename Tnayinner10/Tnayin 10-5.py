# 10-5 Write a Python program that calculates the Fibonacci sequence up to a given number n
# using a while loop. The Fibonacci sequence is a series of numbers where each number
# is the sum of the two preceding ones.

n = int(input("write some number and the program will print Fibonacii sequence till given number "))

i = 0 

a, b, c = 0, 0, 1

while i < n :
    print(b)
    a = b 
    b = b + c   
    c = a 

    i+=1





