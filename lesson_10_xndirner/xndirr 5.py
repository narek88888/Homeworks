# : Write a program that calculates the sum of
# numbers from 1 to a user-defined limit using a
# while loop.


x = int(input("Write some number and the program will count sum of number"))

number = 0
sum = 0

while number < x :
    number += 1
    sum+= number
print(sum)

